# Read in data
with open('input.txt') as my_file:
    testsite_array = my_file.readlines()

# create array without newline character
arrayofinstructions = [z[:-1] for z in testsite_array]
depth = 0
hposition = 0
# added aim variable
aim = 0

# updated from Pt 1 to add aim and how it affects the depth and hposition
for i in arrayofinstructions:
    x = i.split()
    if x[0] == 'forward':
        hposition = hposition + int(x[1])
        depth = depth + (aim * int(x[1]))
    elif x[0] == 'down':
        aim = aim + int(x[1])
    elif x[0] == 'up':
        aim = aim - int(x[1])

print(depth*hposition)


