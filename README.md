# KMKfw-POG
These are the "firmware" files for my custom hand wired ergonomic linear keyboards.

I am using [KMK](https://kmkfw.io/) and [POG](https://pog.heaper.de/) on a [Boardsource](https://www.boardsource.xyz) [Blok](https://www.boardsource.xyz/products/blok) controller.

The first board I've added is named BlueWaveEL, and is a 52 key (5 row, 12 column) single board, "split", column stagger layout.

The KMK files were downloaded from the KMK GitHub at 2024-06-01 11:50.

The POG v1.3.1 Linux AppImage was downloaded at 2024-06-01 10:59.

# Notes
To get the POG configuration to work, I needed to set the Pin Prefix to "board" because some of the Blok pins I wanted to use did not have a "GP" prefix.

I also had to comment out lines 111 and 112 in the generated pog.py because the Blok board does not have a VBUS_SENSE pin.

