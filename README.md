# <a href="https://www.lfsystems.com.co"><img src="https://cdn.rawgit.com/lfelipe1501/Atomic-Yakuake/537e149c/logo.svg" width="80" height="80"></a> <a href="https://store.kde.org/p/1153663/">Atomic Theme</a> in Yakuake Terminal

![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/lfelipe1501/Atomic-Yakuake/issues)
[![Python27](https://img.shields.io/badge/python-2.7-blue.svg)](convert.py)
[![Build Status](https://img.shields.io/travis/rust-lang/rust/master.svg)](https://github.com/lfelipe1501/Atomic-Yakuake/commits)

Atomic Yakuake Themes Collections

These themes were designed for version 3 of Yakuake

## Compile themes

### Python Script to convert SVG to PNG

You can compile SVG files from the comfort of your terminal by running the script that is in this repository.

This script contains an order for inkscape that compiles the svg files for a specific screen:

```python
cmd = ("inkscape --export-png={0} --export-dpi=96 "
         "--export-background-opacity=0 --without-gui {1}").format(outf,
                                                                   inf)
```

you can edit this line **--export-dpi=96** where you need to know the amount of dpi for the resolution of your screen.
To know the density of your screen you can run the following command from your linux terminal:

```bash
xdpyinfo | grep -B2 resolution

screen #0:
  dimensions:    1920x1080 pixels (508x285 millimeters)
  resolution:    96x96 dots per inch
```

Open a terminal and run the corresponding command from the version of python 2

To use this script you need to have [`inkscape`](https://inkscape.org/en/download/) installed on your distribution or windows operating system and place the script in the folders containing the SVG files, then execute it with the corresponding command.

Example in ArchLinux:

```bash
  $ python2 convert.py
```

### Contact / Social Media

*Get the latest News about Web Development, Open Source, Tooling, Server & Security*

[![Twitter](https://github.frapsoft.com/social/twitter.png)](https://twitter.com/lfelipe1501)
[![Facebook](https://github.frapsoft.com/social/facebook.png)](https://www.facebook.com/lfelipe1501)
[![Github](https://github.frapsoft.com/social/github.png)](https://github.com/lfelipe1501)

### Development by

Developer / Author: [Luis Felipe Sánchez](https://github.com/lfelipe1501)
Company: [lfsystems](https://www.lfsystems.com.co)

### License
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This work by [Luis Felipe Sánchez](https://github.com/lfelipe1501) is licensed under a Creative Commons Attribution 4.0 International License.
