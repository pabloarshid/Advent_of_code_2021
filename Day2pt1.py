

# Read in data
with open('input.txt') as my_file:
    testsite_array = my_file.readlines()

# create array without newline character
arrayofinstructions = [z[:-1] for z in testsite_array]
depth = 0
hposition = 0

# for loop through arrayofinstructions. first split the instruction into a tuple where first value is direction. Second is value;
# if statment for different cases  
for i in arrayofinstructions:
    x = i.split()
    if x[0] == 'forward':
        hposition = hposition + int(x[1])
    elif x[0] == 'down':
        depth = depth + int(x[1])
    elif x[0] == 'up':
        depth = depth - int(x[1])

print(depth*hposition)


