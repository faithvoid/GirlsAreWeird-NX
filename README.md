# GirlsAreWeird-NX
Unofficial port of the Ren'Py visual novel "Girls Are Weird" by bentosmile, using the Ren'Py Switch SDK. This repository does not include the renpy-switch.elf file as it's too large, and you'll probably want to use an updated version anyhow.

![A picture!](https://i.imgur.com/3qJoMT3.jpg)

## TODO:
Convert .rpy and .py files for faster boot times.
Make save data save in .nro folder instead of a folder on the SD card root.

## Build:
Once you have your DevkitPro environment set up and a copy of renpy-switch.elf from the Ren'Py Switch SDK, all you need to do is run these two commands (or your system's equivalent) and you're set!

'/opt/devkitpro/tools/bin/elf2nro' renpy-switch.elf TITLE.nro --icon=icon.jpg --nacp=TITLE.NACP --romfsdir=romfs

'/opt/devkitpro/tools/bin/nacptool' --create "TITLE" "AUTHORS" "VERSION" TITLE.NACP

Replacing "TITLE", "AUTHORS" and "VERSION" with whatever you want.


## Bugs:
You tell me!
