import random

acronyms = open('acronyms.txt').read().splitlines()

while True:
    acronym = random.choice(acronyms)
    acronym_and_meaning = acronym.split(" - ")
    print(acronym_and_meaning[0], end = '')
    input("")
    print(acronym)
    input("")
