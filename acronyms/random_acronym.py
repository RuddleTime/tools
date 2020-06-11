import sys
import random
import argparse


def input_file(file_name):
    """File acronyms to be read from"""
    try:
        with open(file_name) as fo:
            acronyms = fo.read().splitlines()
    except(FileNotFoundError) as err:
        print("File: \"{0}\" not found.\nExiting with error: \n{1}\n".format(file_name, err))
        sys.exit()
    return acronyms


def check_input():
    """ Checking for exit command from user"""
    user_input = input("")
    if user_input == 'c':
        return False
    return True


def random_acronym(acronyms): 
    """
    Outputs random acronym read in from txt file.
    On user keyboard input, meaning of acronym is printed.
    """
    user_input = True
    while user_input:
        acronym = random.choice(acronyms)
        acronym_and_meaning = acronym.split(" - ")
        print(acronym_and_meaning[0], end = '')
        input("")
        print(acronym)
        user_input = check_input()


def parse_args():
    """ Parses command line arguements """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file_name",
        type=str, help="File of acronyms to be read in."
    )
    args = parser.parse_args()
    return args


if __name__=='__main__':
    args = parse_args()
    file_name = args.file_name
    acronyms = input_file(file_name)
    random_acronym(acronyms) 
