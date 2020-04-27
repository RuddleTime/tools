#http://www.pythonchallenge.com/pc/def/map.html

s = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'


url = 'http://www.pythonchallenge.com/pc/def/map.html'

strings = [s, url]

for string in strings:
    ns = ''
    print(string)
    for letter in string:
        advanced_letter = chr(ord(letter[0])+2)
        ns += advanced_letter
    print(ns)


