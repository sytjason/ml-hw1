import numpy as np

f = open('./hw1_15_train.dat')
data = f.readlines()

for i in np.arange(0, len(data)):
    data[i] = data[i].replace('\t', ' ')
    data[i] = data[i].replace('\n', '')

#insert x0 = 1 to every xn
for i in np.arange(0, len(data)):
    data[i] = '1 '+ data[i]

w = [0, 0, 0, 0, 0]
state = 0
change = 0
count = 0

#if nothing can be changed, exit while loop
while state == 0:
    change = 0
    # check the value of yn
    for i in np.arange(0, len(data)):
        tmp = 0
        for j in np.arange(0, 5):
            tmp += float(w[j]*float(data[i].split(' ')[j]))
        tmp = np.sign(tmp)
        if tmp == 0:
            tmp = -1
        if tmp != int(data[i].split(' ')[5]):
            for j in np.arange(0, 5):
                w[j] += float(data[i].split(' ')[5])*float(data[i].split(' ')[j])
                change = 1
            break
    count += 1 
    if change == 0:
        state = 1
f.close()

#create ans file
f = open("./ans.txt", "w+")
for i in np.arange(0, len(w)):
    f.write("%f " % w[i])
f.close()



