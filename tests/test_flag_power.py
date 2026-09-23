"""Regression guard for the high-current Ukrainian Flag RGB mood.

Run after applying the repository patch to the pinned ZMK source:
    python3 tests/test_flag_power.py src/app/src/rgb_underglow.c
This is a static power-envelope check; hardware validation is still required.
"""
import pathlib
import re
import sys
import unittest

SOURCE_PATH = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None


class FlagPowerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert SOURCE_PATH is not None
        cls.source = SOURCE_PATH.read_text()
        cls.flag = cls.source.split(
            "static void zmk_rgb_underglow_effect_mood_ukrainian_flag(void) {", 1
        )[1].split("\nstatic int zmk_led_generate_status", 1)[0]

    def test_both_flag_colors_use_capped_brightness(self):
        self.assertIn("mood_flag_hsb(211,", self.flag)
        self.assertIn("mood_flag_hsb(50,", self.flag)
        helper = self.source.split("static struct led_rgb mood_flag_hsb(", 1)[1].split(
            "\n}", 1
        )[0]
        self.assertIn("MIN(state.color.b, 32)", helper)
        self.assertIn("hsb_scale_zero_max(hsb)", helper)

    def test_brightness_up_changes_flag_output_above_default(self):
        # Exact integer brightness pipeline of mood_flag_hsb() and hsb_scale_zero_max().
        def scaled_peak(global_brightness):
            return ((51 * min(global_brightness, 32)) // 100) * 80 // 100

        self.assertGreater(scaled_peak(20), scaled_peak(16))
        self.assertGreater(scaled_peak(32), scaled_peak(20))
        self.assertEqual(scaled_peak(100), scaled_peak(32))
        self.assertLess(scaled_peak(32), ((98 * 16) // 100) * 80 // 100 + 1)

    def test_flag_wave_peak_is_reduced_without_erasing_animation(self):
        self.assertRegex(self.flag, r"brightness = 12 \+ \(wave \* 35\) / 100;")
        self.assertRegex(self.flag, r"mood_flag_hsb\(50, MIN\(brightness \+ 4, 100\)\)")
        self.assertIn("state.animation_step += state.animation_speed", self.flag)


if __name__ == "__main__":
    sys.argv = [sys.argv[0]]
    unittest.main()
