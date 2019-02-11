# pythonchallenge 10
# bull.html
# look and say sequence

a = [''] * 31
a[0] = '1'
result = {}

for number in range(30):
    current = ['', 0]

    for char in a[number]:
        position = 0
        if char == current[0]:
            current[1] += 1

        else:
            if current[0] != '': # record
                a[number+1] += (str(current[1]) + current[0])

            current[0] = char
            current[1] = 1

    a[number+1] += (str(current[1]) + current[0])

last = a[len(a) - 1]
print(len(last))
