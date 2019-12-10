A=[3,6,5,8,10,20,15]
print("Original Array" , A)

flag=True
count=0
for j in range(1, len(A)):
    key = A[j]
    i=j-1
    while i>=0 and A[i]> key:
        A[i+1]=A[i]
        i-=1
    A[i+1]=key
    count+=1
    if count >=2:
        flag=False
        break

return flag
