sequence=[2,4,3,7,4,5]



LIS= [1]*len(sequence)

for i in range(1,len(sequence)):
    for j in range(0,i):
        if sequence[i] > sequence[j]:
            LIS[i]=max(LIS[i],LIS[j]+1)

print( max(LIS))
