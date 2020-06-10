import random
import argparse


def input_file(file_name):
    """File acronyms to be read from"""
    fo = open(file_name)
    acronyms = fo.read().splitlines()
    fo.close()
    return acronyms


def random_acronym(acronyms): 
    """
    Outputs random acronym read in from txt file.
    On user keyboard input, meaning of acronym is printed.
    """
    while True:
        acronym = random.choice(acronyms)
        acronym_and_meaning = acronym.split(" - ")
        print(acronym_and_meaning[0], end = '')
        input("")
        print(acronym)
        input("")


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
