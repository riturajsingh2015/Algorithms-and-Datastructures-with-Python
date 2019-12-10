
class QuickSort:
    def __init__(self,A):
        self.A=A
    def sort(self,p,r):
        A=self.A
        if p<r:
            q=self.Partition(A,p,r)
            self.sort(p,q-1)
            self.sort(q+1,r)

    def Partition(self,A,p,r):
        x=A[r]
        i=p-1
        for j in range(p,r):
            if A[j]<=x:
                i+=1
                temp=A[i]
                A[i]=A[j]
                A[j]=temp

        temp=A[i+1]
        A[i+1]=A[r]
        A[r]=temp
        return i+1


    def Partition_Ob(self,p,r):
        A=self.A
        x=A[r].w
        i=p-1
        for j in range(p,r):
            if A[j].w<=x:
                i+=1
                temp=A[i]
                A[i]=A[j]
                A[j]=temp

        temp=A[i+1]
        A[i+1]=A[r]
        A[r]=temp
        return i+1


    def Sort_Ob(self,p,r):
        A=self.A
        if p<r:
            q=self.Partition_Ob(A,p,r)
            self.Sort_Ob(p,q-1)
            self.Sort_Ob(q+1,r)

    def Sort_Ob_iter(self,l,r):
        A=self.A
        stack=[]
        stack.append(r)
        stack.append(l)

        while stack!=[]:
            l=stack.pop()
            r=stack.pop()
            #print("Popped" , l,r)
            q=self.Partition_Ob(l,r)
            #print(A)
            #print(stack)
            if q-1>=0: # there are elements to left of pivot element
                if l < q-1:
                    #print("Appending ",(q-1),l)
                    stack.append(q-1)
                    stack.append(l)

            if q+1<=len(A)-1: # there are elements to right of pivot element
                if q+1 < r:
                    #print("Appending ",r,(q+1))
                    stack.append(r)
                    stack.append(q+1)
            #input("wait")


class InsertionSort:
    def __init__(self,A):
        self.A=A
    def sort(self):
        A=self.A
        for j in range(1, len(A)):
            key = A[j]
            i=j-1
            while i>=0 and A[i]> key:
                A[i+1]=A[i]
                i-=1
            A[i+1]=key
        return A
    def Sort_Ob(self):
        A=self.A
        for j in range(1, len(A)):
            key = A[j]
            i=j-1
            while i>=0 and A[i].w> key.w:
                A[i+1]=A[i]
                i-=1
            A[i+1]=key
