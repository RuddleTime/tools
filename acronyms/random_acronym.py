import random


def random_acronym(): 
    """
    Outputs random acronym read in from txt file.
    On user keyboard input, meaning of acronym is printed.
    """
    acronyms = open('acronyms.txt').read().splitlines()

    while True:
        acronym = random.choice(acronyms)
        acronym_and_meaning = acronym.split(" - ")
        print(acronym_and_meaning[0], end = '')
        input("")
        print(acronym)
        input("")


if __name__=='__main__':
    random_acronym() 
