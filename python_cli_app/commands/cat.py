def run():
    try:
        with open(args.cat, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f'Error: The file "{args.cat}" does not exist.')
    except Execption as e:
        print(f'an error occurred: {e}')

