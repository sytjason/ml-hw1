import numpy as np
run = 2000
f = open('./hw1_15_train.dat')
data = f.readlines()
f.close()

for i in np.arange(0, len(data)):
    data[i] = data[i].replace('\t', ' ')
    data[i] = data[i].replace('\n', '')

# insert x0 = 1 to every xn
for i in np.arange(0, len(data)):
    data[i] = '1 '+ data[i]

# create x array from data and x[:][5] represent y
x = [np.array(data[0].split(' ')[0:6])]
for i in np.arange(1, len(data)):
    x = np.concatenate((x, [data[i].split(' ')[0:6]]), axis = 0) 
x = x.astype(np.float)
x[:, 5] = x[:, 5].astype(np.int)

count_sum = 0
for k in np.arange(0, run):
    # randomize the element order of data
    np.random.shuffle(x)

    w = [0, 0, 0, 0, 0]
    state = 0
    change = 0
    count = 0
	
    # if nothing can be changed, exit while loop
    while state == 0:
        change = 0
        # cyclic visit every example
        for i in np.arange(0, len(x)):
            tmp = 0

            # calculate the h(x)
            tmp = np.dot(w, x[i][0:5])
            tmp = np.sign(tmp)
            if tmp == 0:
                tmp = -1
            
            # find out the mistake example
            if tmp != x[i][5]:
                w = np.add(w, 0.5*x[i][0:5]*x[i][5]) 
                change = 1
                count += 1

        if change == 0:
            state = 1
    count_sum += count
res = count_sum / run
print(res)



