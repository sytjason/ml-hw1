import numpy as np

#open ans.txt file
f = open("./ans.txt")
w = f.readline()
f.close()
w = w.replace('%', '')

#open hw1_15_train.dat file
f = open("./hw1_15_train.dat")
data = f.readlines()
for i in np.arange(0, len(data)):
    data[i] = data[i].replace('\t', ' ')
    data[i] = data[i].replace('\n', '')

#insert x0 = 1 to every xn
for i in np.arange(0, len(data)):
    data[i] = '1 '+ data[i]

res = 1 

for i in np.arange(0, len(data)):
    tmp = 0
    for j in np.arange(0, 5):
        tmp += float(float(w.split(' ')[j])*float(data[i].split(' ')[j]))
    tmp = np.sign(tmp)
    if tmp == 0:
        tmp = -1
    if tmp != int(data[i].split(' ')[5]):
        res = 0
        break

print(res)


