A=[-1,150,190,170,-1,-1,160,180]
print("Original Array" , A)

for j in range(1, len(A)):

    key = A[j]
    i=j-1
    while i>=0 and A[i]> key:
        A[i+1]=A[i]
        i-=1
    A[i+1]=key
print("Sorted Array" , A)
