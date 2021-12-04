
with open('artifact1.txt', 'r') as f:
    data = f.read()

with open('artifact2.txt', 'w+') as f:
    f.write(data)
print('end of stage 3')