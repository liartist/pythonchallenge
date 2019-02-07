# pythonchallenge 6
# channel.html

import os
import re
import zipfile

checker = re.compile('Next nothing is ')
nothing = re.compile('\d+')
PATH = os.getcwd()
zip = zipfile.ZipFile(PATH[:-7] + 'channel.zip', 'r')
files = os.listdir(PATH)
cursor = '90052.txt'
flag = zip.getinfo(cursor).comment

while (True):
    file = open(cursor, 'r')
    lines = file.readlines()
    cursor = ''.join(lines)
    if checker.search(cursor):
        next = nothing.findall(cursor)
        if len(next) > 1:
            print(cursor)
            next = input()
        else:
            print(cursor, flush=True)
    else:
        print(cursor)
        break
    cursor = next[0] + '.txt'
    flag += zip.getinfo(cursor).comment

print(flag.decode('ascii'))
