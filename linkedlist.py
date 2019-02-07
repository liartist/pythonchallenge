# pythonchallenge 4
# linkedlist.php

import urllib.request
import re

request = urllib.request
checker = re.compile('the next nothing is ')
nothing = re.compile('\d+')
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

for i in range(400):
    data = request.urlopen(url)
    datum = data.read().decode('utf-8')
    if checker.search(datum):
        next = nothing.findall(datum)
        if len(next) > 1:
            print(datum)
            next = input()
        else:
            print(next, end=' ', flush=True)
    else:
        print(datum)
        next = input()
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + next[0]
