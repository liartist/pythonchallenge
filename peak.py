# pythonchallenge 5
# peak.html

import pickle

file = pickle.load(open('banner.p', 'rb'))

for list in file:
    for tuple in list:
        for i in range(tuple[1]):
            print(tuple[0], end = '')
    print()
