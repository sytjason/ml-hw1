import numpy as np
import pandas as pd

def _readfile(filename):
    df = pd.read_table(filename, header=None, delim_whitespace=True)
    # insert 1 to every x
    df.insert(0, 0, 1, allow_duplicates=True)
    df.columns = np.arange(0, 6)
    df[[0]] = df[[0]].astype(float)
    return df

def _split(df):
    x = df[[0, 1, 2, 3, 4]]
    y = df[5]
    return x, y
    

def _hypo(w, x):
    res = np.sign(np.dot(w, x))
    if res == 0:
        res = -1
    return res

def _mistake_count(w, x, y):
    res = 0
    for i in np.arange(len(x)):
        if y[i] != _hypo(w, x.iloc[i]):
            res += 1
    return res

def _pla(df):
    (x, y) = _split(df)
    w = np.zeros(5)
    flag = True 
    update_count = 0
    while flag == True:
        flag = False
        # cyclic visit every sample
        for i in range(len(x)):
            if y[i] != _hypo(w, x.iloc[i]):
                #update w
                w = np.add(w, y[i]*x.iloc[i])
                update_count += 1
                flag = True
                break
    return update_count

def _random_pla(df):
    eta = 0.5
    w = np.zeros(5)
    flag = True 
    update_count = 0
    # randomize the order of df
    new_index = np.arange(400)
    np.random.shuffle(new_index)
    df = df.reindex(new_index)
    df.index = np.arange(400)
    (x, y) = _split(df)
    while flag == True:
        flag = False
        # cyclic visit every sample
        for i in range(len(x)):
            if y[i] != _hypo(w, x.iloc[i]):
                #update w
                w = np.add(w, eta*y[i]*x.iloc[i])
                update_count += 1
                flag = True
                break

    return update_count

def _pocket(df):
    (x, y) = _split(df)
    w = np.zeros(5)
    wnew = np.zeros(5)
    wpocket = np.zeros(5)
    mistake_count = _mistake_count(w, x, y) 
    newmistake_count = 0 
    update_count = 0
    while update_count < 50:
        # random choose a sample
        i = np.random.choice(np.arange(len(x)))
        if y[i] != _hypo(w, x.iloc[i]):
            # save the changed w to wnew
            wnew = np.add(w, y[i]*x.iloc[i])
            newmistake_count = _mistake_count(wnew, x, y) 
            w = wnew.copy()
            update_count += 1
            if newmistake_count <= mistake_count:
                mistake_count = newmistake_count
                wpocket = wnew
        # print(newmistake_count)
        print(mistake_count)
        # print(update_count)
    return update_count, wpocket

# pla
# df = _readfile('hw1_15_train.dat')
# res = _pla(df)
# print(res)

# random pla
runs = 2000
res = 0
for run in range(0, runs):
    df = _readfile('hw1_15_train.dat')
    res += _random_pla(df)
res = res/runs
print(res)




