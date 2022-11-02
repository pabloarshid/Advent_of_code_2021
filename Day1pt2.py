# Steps:
# 1. read in Values from File
# 2. update to slice of newline character and make into int
# 3. Use chunks funciton to create tuples of 3 values from the list of values
# 4. for loop through chunks array and check if the sum of i tuple is greater than prevvalue


def chunks(lst, n):
    # Yield successive n-sized chunks from lst.
    for i in range(0, len(lst)):
        yield lst[i:i + n]


with open('input.txt') as my_file:
    testsite_array = my_file.readlines()


arrayofnums = [int(z[:-1]) for z in testsite_array]
chunksarr = list(chunks(arrayofnums,3))

increases = 0
prevvalue = sum(chunksarr[0])

for i in chunksarr[1:]:
    if sum(i) > prevvalue:
        increases = increases + 1
    prevvalue = sum(i)

print(increases)


