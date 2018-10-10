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
for k in np.arange(0, 2000):
    # randomize the element order of data
    np.random.shuffle(data)

    w = [0, 0, 0, 0, 0, 0] # w[5] is for mistake count
    wnew = [0, 0, 0, 0, 0, 0]
    count = 0
    

    # if update 50 times, then exit while loop
    while count != 50:
        change = 0
        # cyclic visit every example
        for i in np.arange(0, len(data)):
            tmp = 0

            # calculate the h(x)
			tmp = np.dot(float(w[0:5]), float(data[i].split(' ')[0: 5])
     #       for j in np.arange(0, 5):
     #           tmp += float(w[j]*float(data[i].split(' ')[j]))
            tmp = np.sign(tmp)
            if tmp == 0:
                tmp = -1
            
            # find out the mistake example
            if tmp != int(data[i].split(' ')[5]):
                #update wnew
                for j in np.arange(0, 5):
                    wnew[j] += float(data[i].split(' ')[5])*float(data[i].split(' ')[j])
					
                count += 1
                # calculate the mistake count
                for l in np.arange(0, len(data)):
                    for m in np.arange(0, 5):
						
		

                    

    count_sum += count
res = count_sum / 2000
print(res)



