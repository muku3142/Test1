row={
    0:[1,2,3],
    1:['a',1,'c'],
    2:[-1,-2,0]

}

i=0
j=0
flag=0
for i in range(len(row)-1):
    if (row[i][j]== row[i+1][j+1]):
        flag= 1
        i +=1
        j+=1
    else: flag= 0

if(not flag): print("True")