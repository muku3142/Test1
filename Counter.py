arr= [ "abz","aba", "cac", "kmm","lpl"]
count=0
for i in range(len(arr)):
    if ( len(arr[i]) >= 2 and arr[i][0]==arr[i][-1]): count +=1

print(count)
