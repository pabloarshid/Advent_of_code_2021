def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
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


