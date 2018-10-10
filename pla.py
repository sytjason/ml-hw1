import numpy as np

f = open('./hw1_15_train.dat')
data = f.readlines()
f.close()

for i in np.arange(0, len(data)):
    data[i] = data[i].replace('\t', ' ')
    data[i] = data[i].replace('\n', '')

# insert x0 = 1 to every xn
for i in np.arange(0, len(data)):
    data[i] = '1 '+ data[i]

# create x and y from data
x = [np.array(data[0].split(' ')[0:5])]
y = np.array(data[0].split(' ')[5])

for i in np.arange(1, len(data)):
    x = np.concatenate((x, [data[i].split(' ')[0:5]]), axis = 0) 
    x = x.astype(np.float)
    y = np.append(y, data[i].split(' ')[5])
    y = y.astype(np.int)

w = [0, 0, 0, 0, 0]
state = 0
change = 0
count = 0

# if nothing can be changed, exit while loop
while state == 0:
    change = 0
    # cyclic visit every example
    for i in np.arange(0, len(data)):
        tmp = 0

        # calculate the h(x)
        tmp = np.dot(w[0:5], x[i][0:5])
        tmp = np.sign(tmp)
        if tmp == 0:
            tmp = -1
        
        # find out the mistake example
        if tmp != y[i]:
            w = np.add(w, y[i]*x[i])
            change = 1
            count += 1

    if change == 0:
        state = 1
print(count)




