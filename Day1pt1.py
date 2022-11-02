
# Open and read in input file
with open('input.txt') as my_file:
    testsite_array = my_file.readlines()

# noticed the input files come with the linebreak value so created a new array that sliced off the newline value as well as making the values int
arrayofnums = [int(z[:-1]) for z in testsite_array]


increases = 0
prevv = arrayofnums[0]

# Cycle through each value. If selected value is larger than prev than increment counter
# update prev value

for i in arrayofnums[0:]:
    if i > prevv:
        increases = increases + 1
    prevv = i

print(increases)


