# MoErgo Glove80 Custom Configuration for ZMK

![MoErgo Logo](moergo_logo.png)

This repo is the official ZMK configuration of the MoErgo Glove80 wireless split contoured keyboard. Use it to develop your own keymap and easily build your own ZMK firmware to run on your Glove80.

**NOTE: You can also customize the layout of your Glove80 keyboard with the Glove80 Layout Editor webapp. For most users Glove80 Layout Editor is the recommended and simpler option. More information is available at the official MoErgo Glove80 Support site (see resources below).**

These steps will get you using your keymap on your keyboard in the fastest time possible. It uses the GitHub Actions feature to build your firmware online.

If you are looking to dig deeper into ZMK and develop new functionality, it is recommended to follow the steps of installing ZMK as found on the official ZMK documentation site (linked below).

## Resources
- The [official MoErgo Glove80 Support](https://moergo.com/glove80-support) web site. Glove80 documentation and other technical resources.
- The [official MoErgo Discord Server](https://moergo.com/discord). Instant conversations with other Glove80 users.

- The [official ZMK Documentation](https://zmk.dev/docs) web site. Find the answers to many of your questions about ZMK Firmware.
- The [official ZMK Discord Server](https://discord.gg/8cfMkQksSB). Instant conversations with other ZMK developers and users. Great technical resource!

- The [official Glove80 ZMK Distribution](https://github.com/moergo-sc/zmk). Repositiory for ZMK firmware customized for Glove80. 
 
## Instructions
1. Log into, or sign up for, your personal GitHub account.
2. Create your own repository using this repository as a template ([instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)) and check it out on your local computer.
3. Edit the keymap file(s) to suit your needs
4. Commit and push your changes to your personal repo. Upon pushing it, GitHub Actions will start building a new version of your firmware with the updated keymap.

## Firmware Files
To locate your firmware files and reflash your Glove80...
1. log into GitHub and navigate to your personal config repository you just uploaded your keymap changes to.
2. Click "Actions" in the main navigation, and in the left navigation click the "Build" link.
3. Select the desired workflow run in the centre area of the page (based on date and time of the build you wish to use). You can also start a new build from this page by clicking the "Run workflow" button.
4. After clicking the desired workflow run, you should be presented with a section at the bottom of the page called "Artifacts". This section contains the results of your build, in a file called "glove80.uf2"
5. Download the glove80.uf2
6. Flash the firmware to Glove80 according to the user documentation on the official Glove80 Glove80 Support website (linked above)

Your keyboard is now ready to use.

## Layer-aware RGB indicators

This configuration uses the per-layer RGB implementation from
[`darknao/zmk`](https://github.com/darknao/zmk), pinned in the build workflow to
an exact commit for reproducible firmware builds.

- **Base:** `Magic+G` cycles through Off, Aurora, Fire, Pacifica, Forest, Party,
  and Colorloop/Stripe Flow. The selected mood is saved across power cycles.
- **Lower:** amber media controls, cyan navigation/numpad keys, and a white layer key.
- **Magic:** no custom layer map; existing system controls remain, with `Magic+I` added for idle auto-off.
- **Gaming:** the physical `E`, `S`, `D`, and `F` keys light cyan because they emit
  `W`, `A`, `S`, and `D` on this layer. Escape is red, Space is green, and
  Control is purple. The physical Grave, Tab, Caps Lock, and Shift keys produce
  the otherwise missing `5`, `T`, `G`, and `B` keys.
- **Lower Gaming:** number controls light amber while the physical `E/S/D/F`
  anchors remain cyan.

On both Lower layers, the right-side numpad is cyan, keypad Enter is green,
keypad Equals is white, and Print Screen is red.

Aurora and RGB power are the firmware defaults after a configuration reset.
Layer indicators are independent of the selected Base mood: Gaming and Lower
Gaming always use the same functional colors, including when Base is set to
Off. RGB brightness remains controlled by the normal Magic-layer controls.
LEDs automatically turn off after 30 seconds of idle time to reduce battery
drain. `Magic+I` toggles this idle auto-off behavior, and the preference is
saved across power cycles. The regular RGB power toggle remains separate.

When changing between firmware versions, flash the same combined UF2 to both
halves and follow MoErgo's configuration reset and re-pair procedure. To roll
back, build and flash both halves from known-good commit `07e08a5`.
