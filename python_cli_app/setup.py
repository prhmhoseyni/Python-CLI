import argparse
import os


def setup_argparse():

    parser = argparse.ArgumentParser(description="Python CLI Application")

    parser.add_argument(
        "--ls",
        nargs="?",
        const=os.getcwd(),
        default=None,
        metavar=("PATH"),
        help="List files in the specified path."
    )

    parser.add_argument(
        "--cd",
        type=str,
        metavar=("PATH"),
        help="Change the working directory to path."
    )

    parser.add_argument(
        "--mkdir",
        nargs=2,
        metavar=("PATH", "NAME"),
        help="Create a new directory at path."
    )

    parser.add_argument(
        "--rmdir",
        type=str,
        metavar=("PATH"),
        help="Remove the directory at path if it is empty."
    )

    parser.add_argument(
        "--rm",
        type=str,
        metavar=("FILE"),
        help="Remove the file specified by `file`."
    )

    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Remove directories and its contents recursively."
    )

    parser.add_argument(
        "--cp",
        nargs=2,
        metavar=("SRC", "DESTINATION"),
        help="Copy a file or directory from `source` to `destination`."
    )

    parser.add_argument(
        "--mv",
        nargs=2,
        metavar=("SRC", "DESTINATION"),
        help="Move a file or directory from `source` to `destination`")

    parser.add_argument(
        "--find",
        nargs=2,
        metavar=("PATH", "PATTERN"),
        help="Search for files or directories matching `pattern` starting from path."
    )

    parser.add_argument(
        "--cat",
        type=str,
        metavar=("FILE"),
        help="Output the contents of the file `file`."
    )

    return parser
