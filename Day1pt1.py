


with open('input.txt') as my_file:
    testsite_array = my_file.readlines()


arrayofnums = [int(z[:-1]) for z in testsite_array]
# print(arrayofnums)
increases = 0
prevv = arrayofnums[0]

for i in arrayofnums[0:]:
    if i > prevv:
        increases = increases + 1
    prevv = i

print(increases)


