#http://www.pythonchallenge.com/pc/def/map.html

import string

s = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

url = 'http://www.pythonchallenge.com/pc/def/map.html'

encoded = [s, url]

for words in encoded:
    ns = ''
    print(words)
    # a = 97; z = 122; ' ' = 32
    for letter in words:
        advanced_letter = ord(letter[0])+2
        if advanced_letter > 122:
            difference = advanced_letter - 122
            advanced_letter = 96 + difference       
        
        ns += chr(advanced_letter)
    print(ns)


intab = string.ascii_lowercase
outtab = ''
for letter in intab:
    advanced_letter = ord(letter[0])+2
    if advanced_letter > 122:
        difference = advanced_letter - 122
        advanced_letter = 96 + difference       
    outtab += chr(advanced_letter)


adjusted_aplha = ''.join(intab[2:]+intab[0]+intab[1])
print(adjusted_aplha)
transtab = str.maketrans(intab, adjusted_aplha)
print(s.translate(transtab))
print('*****&&&&&&&&&&&&&&&&&&&**************')



transtab = str.maketrans(intab, outtab)
print(s.translate(transtab))
print(url)
print(url.translate(transtab))
