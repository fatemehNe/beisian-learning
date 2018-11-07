import pandas
import time

column_name=[]
start=time.time()
for i in range(1,1595):
    column_name.append(i)
train = pandas.read_csv('train.csv')
train.columns = column_name
a = train[1594].value_counts()  #counting values

negative_class = train.loc[train[1594] == -1]   #rows that are class -1
positive_class = train.loc[train[1594] == 1]

ppb =[[0 for x in range(29)] for y in range(1594)]  #positive class probabilities
npb =[[0 for x in range(29)] for y in range(1594)] #negative class probabilities

for i in range(1,1594):
    for j in range(0,29):
        cnt = 0
        for x in range(0,795):
            if negative_class.loc[x , i]> 5*j and negative_class.loc[x , i] < 5*j+5 :
                cnt +=1    
        npb[i][j] = (cnt+1)/795 #p_class= -1 => 795

    for j in range(0,29):
        cnt = 0
        for x in range(795,1599):
            if  positive_class.loc[x , i] > 5*j and positive_class.loc[x , i] < 5*j+5 :
                cnt +=1    
        ppb[i][j] = (cnt+1)/804 #p_class= -1 => 804

test = pandas.read_csv('test.csv')
test.columns = column_name

ptst = [[0 for x in range(2)] for y in range(398)] # 0 => positive 1=> negative
print(len(ptst[2]))


for x in range(0,398):
    for i in range(1,1594):
        for j in range(0,29):
            if  test.loc[x , i] > 5*j and test.loc[x , i] < 5*j+5 :
                ptst[x][0] += ppb[i][j]
                ptst[x][1] += npb[i][j]

stop=time.time()
print(stop-start)

