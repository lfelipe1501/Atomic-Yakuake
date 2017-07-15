#!/usr/bin/python2

import os
import subprocess


def main():
    for inf in os.listdir('.'):
        if not inf.endswith('.svg'):
            continue
        outf = inf.replace('.svg', '.png')
        cmd = ("inkscape --export-png={0} --export-dpi=96 "
               "--export-background-opacity=0 --without-gui {1}").format(outf,
                                                                         inf)

        subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    main()
