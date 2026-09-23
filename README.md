# Constantine’s Glove80 Firmware

![MoErgo Logo](moergo_logo.png)

Custom ZMK firmware for Constantine’s Glove80. It preserves the five-layer ergonomic keymap while adding layer-aware per-key indicators, seven animated RGB moods, Gaming-specific guidance, and persistent lighting controls.

## Highlights

- Per-key RGB indicators for Lower, Gaming, and Lower Gaming.
- Seven Base-layer moods inspired by the WLED presets used at home.
- The selected mood and idle auto-off preference persist across power cycles.
- Gaming indicators stay identical regardless of the selected Base mood.
- A combined UF2 is built automatically by GitHub Actions for both halves.
- Firmware dependencies are pinned for reproducible builds.

## RGB controls

| Shortcut | Action |
|---|---|
| `Magic+G` | Cycle Aurora → Fire → Pacifica → Forest → Party → Colorloop/Stripe Flow → Ukrainian Flag |
| `Magic+T` | Toggle RGB power |
| `Magic+I` | Toggle the 30-second idle auto-off preference |

Aurora and RGB power are the reset-time defaults. There is deliberately no Off entry in the mood cycle; use `Magic+T` to turn lighting off.

### Base moods

- **Aurora:** slow cyan/green/purple waves.
- **Fire:** smooth WLED-inspired 2D heat field with independent flame columns, hot lower rows, and cooler rising tongues.
- **Pacifica:** slow layered blue/cyan waves.
- **Forest:** slow green movement at two-thirds of the original animation speed.
- **Party:** continuous saturated multicolor motion without flashing sparkles.
- **Colorloop / Stripe Flow:** flowing rainbow stripes at one-quarter of the original speed.
- **Ukrainian Flag:** blue upper half and yellow lower half with a slow, visible wave/breathing effect. Its per-effect brightness is capped to reduce the sustained two-channel LED load on USB/KVM and battery; this is a candidate mitigation for typing failures specific to this mood and still needs physical verification.

## Layers

### Base

The normal typing layer. It displays the selected animated mood.

### Lower

Functional color guidance:

- Media and utility controls: orange
- Navigation arrows: blue
- Numpad digits, including both zero keys: cyan
- Num Lock: purple
- Divide, Multiply, Minus, and Plus: yellow
- Decimal: pink
- Keypad Enter: green
- Keypad Equals: white
- Print Screen: red
- Layer key: white

### Magic

Retains the existing system controls and has no custom per-layer RGB map. `Magic+I` is the only added binding, used for the persistent idle auto-off toggle.

### Gaming

The physical `E/S/D/F` keys emit `W/A/S/D` and light cyan. Escape is red, Space is green, and Control is purple.

The shifted left edge restores occasionally needed keys:

- Grave position → `5`
- Tab position → `T`
- Caps Lock position → `G`
- Left Shift position → `B`

### Lower Gaming

The separate left-side number cluster is orange. The right-side numpad uses the same semantic colors as Lower. Gaming’s normal functional indicators are restored when returning to Gaming.

## Build and flash

Every push runs [`.github/workflows/build.yml`](.github/workflows/build.yml). A successful run publishes a `glove80.uf2` artifact.

1. Open the repository’s **Actions** tab.
2. Select the latest successful **Build** run.
3. Download the `glove80.uf2` artifact.
4. Flash the same combined UF2 to **both** Glove80 halves using the official [MoErgo firmware-loading instructions](https://docs.moergo.com/glove80-user-guide/customizing-key-layout/).
5. Test Base moods, all layers, idle/wake, power cycling, and both halves.

A configuration reset is normally unnecessary for an ordinary upgrade. Use it only when testing reset-time defaults or recovering stale settings; it clears stored preferences and may require Bluetooth re-pairing.

## Implementation

This repository intentionally owns only the configuration and a small source patch:

- [`config/glove80.keymap`](config/glove80.keymap): five layers, Gaming remaps, Magic controls, and 80-entry RGB maps.
- [`config/glove80.conf`](config/glove80.conf): RGB enablement, reset defaults, and 30-second idle timeout.
- [`patches/default-layer-effect.patch`](patches/default-layer-effect.patch): mood engine, layer-map composition, effect cycling, and persistent idle auto-off toggle.
- [`.github/workflows/build.yml`](.github/workflows/build.yml): checks out and patches the pinned firmware source, then builds the combined UF2.

The build uses [`darknao/zmk`](https://github.com/darknao/zmk) pinned to commit `8aeaaa66fbb4b94948c8763e06f1920ab0b69480`. The workflow applies the repository-owned patch with `git apply`, so an incompatible upstream change fails loudly rather than silently changing behavior.

### Important invariants

When changing this firmware:

- Preserve all five layers unless a remap is explicitly requested.
- Keep every RGB layer map at exactly 80 bindings.
- Author RGB maps in keymap-position order; the firmware resolves physical LEDs through the board pixel lookup.
- Keep Base moods independent from static layer maps.
- Keep Gaming styling identical across every mood.
- Append new effects instead of renumbering existing saved moods.
- Keep RGB power and idle auto-off as separate controls.
- Pin firmware sources to exact commits.
- Build in GitHub Actions and flash/test both halves before merging.

## Rollback

- Last stock-keymap rollback point: commit `07e08a5`.
- To roll back, build that commit and flash its combined UF2 to both halves.
- Keep a known-good UF2 available before testing firmware changes.

## References

- [Glove80 documentation](https://docs.moergo.com/glove80-user-guide/)
- [MoErgo support](https://moergo.com/glove80-support)
- [ZMK documentation](https://zmk.dev/docs)
