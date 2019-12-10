from Graph import *
import time
from Sorting import *



class BFS:
    def __init__(self,G,s):
        self.G=G
        self.s=s

        source=self.G.get_vertex(self.s)
        source.color="GRAY"
        source.d=0
        source.py=None
        Q=[]
        Q.append(source)
        while Q !=[]:
            #print([v.id for v in Q])
            u=Q.pop(0) # pop from front not back
            for v in self.G.Adj_List[u.id]:
                if v.color=="WHITE":
                    v.color="GRAY"
                    v.d=u.d+1
                    v.py=u
                    Q.append(v)
            u.color="BLACK"


    def get_distances(self):
        dist_unit=6
        x=self.G.V.v_list[:(self.s-1)]+self.G.V.v_list[self.s:]
        distance=[]
        for v in x:
            if v.d==-1:
                distance.append(v.d)
            else:
                distance.append(v.d*dist_unit)
        return distance

    def get_BFS_Tree(self):
        pass




class MST_Kruskal:
    def __init__(self,G):
        self.G=G
        self.MST=set()
        self.Components=list() # list of components
        for v in self.G.V:
            temp=set()
            temp.add(v.id)
            self.Components.append(temp)
        #print("Before")
        #print([(e.V_from.id , e.V_to.id , e.w) for e in self.G.E])

        #Sorting G.E
        #start = time.time()
        #self.Sort_GE()  # this is taking much of the time

        #InsertionSort(self.G.E).Sort_Ob()
        Q=QuickSort(self.G.E)
        #Q.Sort_Ob(0,len(self.G.E)-1)
        Q.Sort_Ob_iter(0,len(self.G.E)-1)
        self.G.E=Q.A

        #print("Sorted Array" , A)
        #end = time.time()
        #print(end - start)

        #print("After")
        #print([(e.V_from.id , e.V_to.id , e.w) for e in self.G.E])
        #start = time.time()
        self.Tree_Generator()
        #end = time.time()
        #print(end - start)
        # print the tree edges
        #print([(e.V_from.id,e.V_to.id,e.w) for e in self.MST])


    def Sort_GE(self):
        for j in range(1, len(self.G.E)):
            key = self.G.E[j]
            i=j-1
            while i>=0 and self.G.E[i].w> key.w:
                self.G.E[i+1]=self.G.E[i]
                i-=1
            self.G.E[i+1]=key

    def Tree_Generator(self):
        for e in self.G.E:
            u=e.V_from.id
            v=e.V_to.id
            s_u=self.Find_Set(self.Components,u)
            s_v=self.Find_Set(self.Components,v)
            if s_u !=s_v:
                self.MST.add(e)
                self.Components.remove(s_u)
                self.Components.remove(s_v)
                self.Components.append(s_u.union(s_v))


    def Find_Set(self,Components,ele):
        component=None
        for c in Components:
            if ele in c:
                component=c
                break
        return component

    def get_MST_Sum(self):
        MST_SUM=0
        for e in self.MST:
            MST_SUM+=e.w
        return (MST_SUM)




class MST_Prim:
    def __init__(self,G,r):
        self.G=G
        root=self.G.V[r - 1]
        root.d=0
        min_Q=set()

        #for e in G.E:
        #    print(e.V_from.id, e.V_to.id , e.w)

        for v in self.G.V:
            min_Q.add(v)

        self.mst_sum=0
        while len(min_Q)!=0: # while set is not empty
            # Extract-Min from min_Q
            #print("min_Q",[(v.id,v.d) for v in min_Q])
            min_d=float('Inf')
            v_min=None
            for v in min_Q:
                if v.d < min_d:
                    min_d=v.d
                    v_min=v

            u=v_min
            #print(type(u))

            min_Q=min_Q-{u}
            #print("Extracted : ",u.id)
            #input()
            self.mst_sum+=u.d
            for v in G.Adj_List[u.id]:
                wt=self.G.get_Edge(u,v).w
                #print(u.id , "--->",v.id , wt)
                if (v in min_Q) and (wt < v.d):
                    v.py=u
                    v.d=wt

                    #print(v.id , v.d)
