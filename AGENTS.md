# Agent guidance

Read [README.md](README.md) before making changes; it is the project contract.

- [Important invariants](README.md#important-invariants) governs layers, RGB map size/order, saved-effect numbering, independent lighting controls, and exact source pins.
- [Implementation](README.md#implementation) maps the owned keymap, configuration, patch, and pinned build workflow.
- [Build and flash](README.md#build-and-flash) describes artifacts and both-half acceptance; [Rollback](README.md#rollback) describes recovery preparation.

## Validation and approval

For documentation-only changes, run `git diff --check` and verify relative links and anchors against the committed tree. No documentation checker is provided.

For firmware work, follow the pinned [workflow](.github/workflows/build.yml), whose build command is `nix-build config -o combined` after source checkout and patch application. A successful build proves artifact creation, not live keyboard behavior.

Flashing, configuration/Bluetooth resets, and physical testing require explicit approval for those actions. Build permission does not authorize them. Report build results separately from approved testing of both halves using the README acceptance steps; never claim unperformed device checks passed.
