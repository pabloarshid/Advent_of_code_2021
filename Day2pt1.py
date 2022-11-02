# def chunks(lst, n):
#     """Yield successive n-sized chunks from lst."""
#     for i in range(0, len(lst)):
#         yield lst[i:i + n]


with open('input.txt') as my_file:
    testsite_array = my_file.readlines()


arrayofnums = [z[:-1] for z in testsite_array]
depth = 0
hposition = 0

for i in arrayofnums:
    x = i.split()
    if x[0] == 'forward':
        hposition = hposition + int(x[1])
    elif x[0] == 'down':
        depth = depth + int(x[1])
    elif x[0] == 'up':
        depth = depth - int(x[1])

print(depth*hposition)


