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

count_sum = 0
for k in np.arange(0, 1):
    # randomize the element order of data
    np.random.shuffle(data)

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
            tmp = np.dot(float(w), float(data[i].split(' ')))
            #for j in np.arange(0, 5):
            #    tmp += float(w[j]*float(data[i].split(' ')[j]))
            tmp = np.sign(tmp)
            if tmp == 0:
                tmp = -1
            
            # find out the mistake example
            if tmp != int(data[i].split(' ')[5]):
                for j in np.arange(0, 5):
                    w[j] += float(data[i].split(' ')[5])*float(data[i].split(' ')[j])
                    change = 1
                count += 1

        if change == 0:
            state = 1
    count_sum += count
res = count_sum / 2000
print(res)



