#!/usr/bin/env python3

import filecmp
import os
import subprocess

# script to keep the examples in sync [fry 210808]


# when changes are found, stop and open a visual diff tool to examine
DIFF_THE_MODS = False

# contains Basics, Demos, Topics
EXAMPLES_DIR = os.path.realpath('../../processing-docs/content/examples')

# contains Basic Examples, Topic Examples
P4_DOCS_REPO = os.path.realpath('../../processing-other/website/content/examples')


# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


# location of the Kaleidoscope diff command
KSDIFF = '/usr/local/bin/ksdiff'

# location of the Xcode FileMerge command
# FILE_MERGE = '/Applications/Xcode.app/Contents/Applications/FileMerge.app'
# FILE_MERGE = '/Applications/Xcode.app/Contents/Applications/FileMerge.app/Contents/MacOS/FileMerge'
FILE_MERGE = '/usr/bin/opendiff'

if os.path.exists(KSDIFF):
    DIFF_TOOL = KSDIFF
else:
    DIFF_TOOL = FILE_MERGE


def run_command(args):
    # process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        # if output == '' and process.poll() is not None:  # hangs on Python 3
        if process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc


# walk two directories and match .pde files in both locations
def handle(examples_folder, web_folder):
    for root, dirs, files in os.walk(examples_folder):
        for file in files:
            if file.endswith('.pde'):
                ex_path = os.path.join(root, file)
                rel_path = ex_path[len(examples_folder)+1:]
                # print(rel_path)
                web_path = os.path.join(web_folder, rel_path)
                # print(web_path)
                status = '         '
                if not os.path.exists(web_path):
                    status = 'missing  '
                elif not filecmp.cmp(ex_path, web_path, shallow=True):
                    status = 'modified '
                    if DIFF_THE_MODS:
                        run_command([ DIFF_TOOL, ex_path, web_path ])
                        exit()
                print(f'{status} {rel_path}')


if __name__ == "__main__":
    handle(f'{EXAMPLES_DIR}/Basics', f'{P4_DOCS_REPO}/Basic Examples')
    handle(f'{EXAMPLES_DIR}/Topics', f'{P4_DOCS_REPO}/Topic Examples')
