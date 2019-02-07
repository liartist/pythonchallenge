# pythonchallenge 1
# map.html
import string

JUMP = 2
target = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
alphabet = string.ascii_lowercase

for char in target:
    if char in alphabet:
        print(alphabet[(alphabet.find(char) + JUMP) % len(alphabet)], end='')
    else:
        print(char, end='')
