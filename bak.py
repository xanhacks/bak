#!/usr/bin/env python3
"""
 Utility to create a copy of a file or a directory with a .bak extension.
"""
from sys import argv
from os.path import exists, isdir
from shutil import copy, copytree


def print_exit(msg):
    """ print the param and exit the program """
    print(msg)
    exit(0)


def bak(path):
    """ copy the file or the folder recursively with the .bak extension """
    if not exists(path):
        print_exit(f"The file '{path}' does not exists !")

    filename = path.rstrip("/") + ".bak"

    try:

        if isdir(path):
            copytree(path, filename)
        else:
            copy(path, filename)

    except FileExistsError:
        print_exit(f"The file '{filename}' already exists !")
    except PermissionError:
        print_exit(f"Unable to create '{filename}', permission denied !")


if __name__ == "__main__":

    if len(argv) != 2:
        print_exit(f"\nUsage : python3 {argv[0]} <path_to_file>\n")

    bak(argv[1])
