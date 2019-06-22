s1= "Hello"
#for i in range(len(s1)):
#List= [s1[i], s1[i+1]]

List1= list(s1)
print("Solution 1 {}".format(List1))

s3=[]
for ch in s1:
    s3.append(ch)
print("Solution 2 {}".format(s3))


s4= [ch for ch in s1]
print("Solution 3 {}".format(s4))

