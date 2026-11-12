# Glove80 RGB Moods

**Animated RGB lighting and per-key layer indicators for the MoErgo Glove80, built on ZMK.**

Stock Glove80 firmware gives you a handful of basic underglow effects. This firmware adds a small animation engine: seven full-keyboard moods that run on your typing layer, plus per-key color maps that light up each extra layer's keys while you hold it. Every animation has been flashed and tested on a real Glove80, on both halves.

[**⬇ Download the latest firmware**](https://github.com/constantinchik/glove80-zmk-config/releases/latest) · [What's included](#features) · [Make it yours](#make-it-yours)

> If this is useful to you, please ⭐ **star the repo**. It helps other Glove80 owners find it.

## Features

- **Seven animated moods** on the base layer: Aurora, Fire, Pacifica, Forest, Party, Colorloop, and Ukrainian Flag. Cycle them with one shortcut.
- **Per-key layer indicators.** Hold a layer and only the keys that matter light up, color-coded by what they do: arrows, numpad, media, and so on.
- **Moods and indicators work together.** Layers without a color map keep showing the current mood, so the lighting never cuts out when you switch layers.
- **Your settings stick.** The selected mood and the idle auto-off preference survive power cycles.
- **Gentle on the hardware.** Each mood keeps its total LED load in the same range as the others, so heavy lighting doesn't make typing lag.
- **Built by CI, nothing to install.** GitHub Actions builds one combined UF2 for both halves from pinned sources. Every build is reproducible.

## Install

1. Download `glove80.uf2` from the [latest release](https://github.com/constantinchik/glove80-zmk-config/releases/latest).
2. Keep your current firmware file so you can roll back.
3. Flash the **same file to both halves** using MoErgo's [firmware-loading instructions](https://docs.moergo.com/glove80-user-guide/customizing-key-layout/).

You don't need a configuration reset to upgrade. A reset clears saved preferences and may require Bluetooth re-pairing, so use it only to recover from bad settings.

The release firmware includes the keymap shown [below](#layers). To use your own keymap, see [Make it yours](#make-it-yours).

## RGB controls

| Shortcut | Action |
|---|---|
| `Magic` + `G` | Next mood: Aurora → Fire → Pacifica → Forest → Party → Colorloop → Ukrainian Flag |
| `Magic` + `T` | Lighting on or off |
| `Magic` + `I` | Turn the 30-second idle auto-off on or off |

The standard Magic-layer brightness and speed controls work on every mood. Each mood sets its own colors, so the hue and saturation controls don't change it. Aurora is the default after a reset. The cycle has no "off" mood; use `Magic` + `T` instead.

### Moods

| Mood | Look |
|---|---|
| **Aurora** | Slow cyan, green, and purple waves |
| **Fire** | A 2D heat field with independent flame columns: hot at the bottom rows, cooler tongues rising |
| **Pacifica** | Layered blue and cyan ocean waves |
| **Forest** | Slow drifting greens |
| **Party** | Continuous saturated multicolor motion, with no flashing sparkles |
| **Colorloop** | Flowing rainbow stripes |
| **Ukrainian Flag** | Blue top rows over yellow bottom rows, with a wave moving across the board |

Several moods are inspired by [WLED](https://kno.wled.ge/) effects.

## Layers

The keymap has five layers. ▽ marks a transparent key, which falls through to the layer below. The images are redrawn by CI with [keymap-drawer](https://github.com/caksoylar/keymap-drawer) whenever the keymap changes.

### Base

![Base layer](docs/layers/base.svg)

The typing layer. It shows the selected mood.

### Lower

![Lower layer](docs/layers/lower.svg)

Media keys, navigation, and a full numpad, color-coded:

| Color | Keys |
|---|---|
| Orange | Media and utility controls |
| Blue | Arrow keys |
| Cyan | Numpad digits |
| Purple | Num Lock |
| Yellow | Divide, multiply, minus, plus |
| Pink | Decimal point |
| Green | Keypad Enter |
| White | Keypad Equals, layer key |
| Red | Print Screen |

### Magic

![Magic layer](docs/layers/magic.svg)

The standard Glove80 system layer: Bluetooth profiles, RGB controls, bootloader, and reset. It has no color map, so the mood keeps running.

### Gaming

![Gaming layer](docs/layers/gaming.svg)

Toggled from the right thumb cluster. The left side is shifted one column right, so your fingers rest on WASD at the usual home-row position. WASD lights cyan, Escape red, Space green, and Control purple. The outer column gives you `5`, `T`, `G`, and `B`.

### Lower Gaming

![Lower Gaming layer](docs/layers/lower-gaming.svg)

While gaming, hold the G-Lower thumb key (double-tap to lock it) to get a left-hand number cluster (orange) and the right-hand numpad, using the same colors as Lower.

## Make it yours

The whole firmware lives in a few files, and GitHub builds it for you.

1. **Fork** this repository.
2. **Edit your keymap** in [`config/glove80.keymap`](config/glove80.keymap). You can design it in the [Glove80 Layout Editor](https://my.glove80.com/) and paste the exported keymap in. Keep the `underglow-layer` block if you want per-key indicators.
3. **Push.** GitHub Actions builds `glove80.uf2`. Download it from the run's artifacts on the **Actions** tab, then flash it to both halves.

### Color your own layers

Per-key color maps live in the `underglow-layer` block of the keymap. Each map lists exactly 80 colors in key-position order, plus the layer it belongs to:

```dts
gaming_rgb {
    bindings = <
        &ug ___ &ug RED &ug ___ /* … 80 entries in total … */
    >;
    layer-id = <3>;
};
```

`___` leaves a key dark. Color names come from ZMK's `rgb_colors.h`, and you can `#define` your own as hex values (for example `#define CYAN 0x00ffff`). Layers without a map show the current mood.

### Add or change a mood

Moods are plain C functions in [`patches/default-layer-effect.patch`](patches/default-layer-effect.patch), applied to ZMK at build time. Each tick, a mood sets a color for every LED. Use the existing moods as templates, add the new one at the end of the effect list so saved settings keep working, and offset its brightness wave per key or per column so the whole board never brightens at once.

## How it works

- [`config/glove80.keymap`](config/glove80.keymap): the five layers and the per-key color maps.
- [`config/glove80.conf`](config/glove80.conf): RGB on at startup, default mood, and the 30-second idle timeout.
- [`patches/default-layer-effect.patch`](patches/default-layer-effect.patch): the mood engine, how moods and layer maps are combined, mood cycling, and the persistent idle toggle.
- [`.github/workflows/build.yml`](.github/workflows/build.yml): checks out the ZMK source, applies the patch, and builds the combined UF2.
- [`.github/workflows/draw.yml`](.github/workflows/draw.yml) and [`keymap_drawer.config.yaml`](keymap_drawer.config.yaml): redraw the layer images in [`docs/layers`](docs/layers).

Builds use [darknao's ZMK fork](https://github.com/darknao/zmk) with per-layer RGB support, pinned to commit `8aeaaa66fbb4b94948c8763e06f1920ab0b69480`. The patch is applied with `git apply`, so an incompatible upstream change fails the build instead of quietly changing behavior.

The `build.sh`, `build.bat`, and `Dockerfile` scripts come from MoErgo's template. They build stock MoErgo ZMK without this patch, so use GitHub Actions to build this firmware.

### Rules for contributors

- Keep every RGB layer map at exactly 80 entries, in key-position order.
- Keep moods independent from layer maps, and Gaming colors the same under every mood.
- Add new moods at the end of the list; never renumber existing ones.
- Keep each mood's total LED load in line with the others.
- Keep RGB power and idle auto-off as separate controls.
- Pin firmware sources to exact commits.
- Flash and test on both halves before merging.

## Credits

- [MoErgo](https://www.moergo.com/) for the Glove80 and the original [config template](https://github.com/moergo-sc/glove80-zmk-config)
- [ZMK](https://zmk.dev/) and [darknao/zmk](https://github.com/darknao/zmk) for per-layer RGB
- [WLED](https://kno.wled.ge/) for mood inspiration
- [keymap-drawer](https://github.com/caksoylar/keymap-drawer) for the layer images

This is a community project, not affiliated with or supported by MoErgo. Flash at your own risk and keep a known-good firmware file for rollback.

If these moods made your Glove80 a little more fun, a ⭐ goes a long way.
