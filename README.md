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

## Flashing Firmware to Glove80

**Prerequisites:**
- USB-C cable
- The downloaded `glove80.uf2` firmware file
- A backup input device (spare keyboard or on-screen keyboard)

**NOTE:** The firmware must be flashed to both halves of the keyboard separately.

### Flashing the Right Half

1. **Connect the right half**: Plug the USB-C cable into the **right** half of your Glove80 and connect it to your computer.

2. **Enter bootloader mode**: Use one of these methods:
   - Press `Magic + '` (single-quote) on the default layout, OR
   - Use the physical bootloader method: Hold the two furthest upper left keys (C6R6 + C3R3) while powering on the keyboard

3. **Verify bootloader mode**: Look for a slow pulsing red LED next to the power switch. A USB Mass Storage Device named `GLV80RHBOOT` will appear on your computer.

4. **Copy firmware**: Drag and drop (or copy) the `glove80.uf2` file onto the USB Mass Storage Device. The device will automatically disconnect once the firmware is successfully flashed.

### Flashing the Left Half

5. **Connect the left half**: Unplug the cable from the right half, then plug it into the **left** half of your Glove80.

6. **Enter bootloader mode**: Use one of these methods:
   - Press `Magic + Esc` on the default layout, OR
   - Use the physical bootloader method: Hold the two furthest upper right keys while powering on the keyboard

7. **Verify and flash**: A USB Mass Storage Device named `GLV80LHBOOT` will appear. Copy the same `glove80.uf2` file to this device.

8. **Finalize**: After both halves are flashed, if you changed the firmware version, perform a configuration factory reset and re-pair the halves.

Your keyboard is now ready to use.
