import random


def input_file():
    """File acronyms to be read from"""
    acronyms = open('acronyms.txt').read().splitlines()
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


if __name__=='__main__':
    acronyms = input_file()
    random_acronym(acronyms) 
