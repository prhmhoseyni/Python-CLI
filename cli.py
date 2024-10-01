import sys
from termcolor import colored
from python_cli_app import setup, utils
from python_cli_app.commands import cat, cd, cp, find, ls, mkdir, mv, rm, rmdir


def main():

    # Setup the parser
    parser = setup.setup_argparse()

    # Parse command line arguments
    args = parser.parse_args()

    # Log command
    utils.log_command()

    # Run command
    if args.ls:
        
        path = args.ls
        
        ls.run(path)

    elif args.cd:

        ...

    elif args.mkdir:
        path = args.mkdir

        mkdir.run(path)

    elif args.rmdir:

        path = args.rmdir
        
        rmdir.run(path)

    elif args.rm:

        path = args.rm
        
        rm.run(path, args.recursive)

    elif args.cp:
        path = args.cp

        cp.run(path)

    elif args.mv:

        source, destination = args.mv

        mv.run(source, destination)

    elif args.find:
        path = args.find
        
        find.run(path)

        

    elif args.cat:
        path = args.cat

        cat.run(path)

    else:

        print(colored("Command Not Found!", "red"))


if __name__ == "__main__":

    main()
