dict={
    0:[1,2,3],
    1:['a',1,'c'],
    2:[-1,-2,0]

}

flag=[]
for key in dict.key():
    if (dict[key][key]==1):
        flag.append(1)
    else: flag.append(0)

if 0 in flag:
    print("False")
else:
    print("True")