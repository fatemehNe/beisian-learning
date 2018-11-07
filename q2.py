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

ppb =[[0 for x in range(1594)] for y in range(29)]  #positive class probabilities
npb =[[0 for x in range(1594)] for y in range(29)] #negative class probabilities

# for i in range(1,1594):
#     for j in range(0,29):
#         cnt = 0
#         for x in range(0,795):
#             if negative_class.loc[x , i]> 5*j and negative_class.loc[x , i] < 5*j+5 :
#                 cnt +=1    
#         npb[j][i] = cnt/795 #p_class= -1 => 795

#     for j in range(0,29):
#         cnt = 0
#         for x in range(795,1599):
#             if  positive_class.loc[x , i] > 5*j and positive_class.loc[x , i] < 5*j+5 :
#                 cnt +=1    
#         ppb[j][i] = cnt/804 #p_class= -1 => 804

test = pandas.read_csv('test.csv')
test.columns = column_name


stop=time.time()
print(stop-start)

