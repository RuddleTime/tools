# Acronym Tester

## Table of contents
* [General info](#general-info)
* [Tech](#tech)
* [To run](#to-run)

## General info
Script will read in a file, whose name can be passed via the command line. File should contain acronyms which:
* Acronym and meaning are dash seperated
 * Example: BEG - Big Evil Grin
* One acronym per line

### Functionality
1. A random acronym from the read in file will be printed to the console
2. On a key being hit the meaning of the acronym will be printed
3. On a key being hit again, a new acronym will be displayed
4. The above steps will be repeated until the running program is cancelled (Ctrl C)

## Tech
Project was written in:

* Python 3.6.9

## To run
Command to run:
```
$ python random_acronym.py -f <name_of_file>
```

Example command:
```
$ python random_acronym.py -f acronyms.txt
```
