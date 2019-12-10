class Graph:
    def __init__(self,V,E,undirected=True):
        self.V=V # list of vertices
        self.E=E # list of edges
        self.undirected=undirected
        self.Adj_List = self.generate_Adj_List(E)
        #self.print_Adj_List()

    def generate_Adj_List(self,E):
        n=len(self.V)
        Adj_List=[[] for _ in range(n+1)]
        for e in E:
            #print(e.V_from.id,e.V_to.id,e.w)
            i=e.V_from.id
            j=e.V_to.id
            if self.undirected:
                if i!=j: # undirected graph no self edge
                    if all([v.id !=j for v in Adj_List[i]]):
                        Adj_List[i].append(self.V[j-1])
                        #Adj_List[i].append(e)

                    if all([v.id !=i for v in Adj_List[j]]):
                        Adj_List[j].append(self.V[i-1])
                        #Adj_List[j].append(e)
            else:
                if all([v.id !=j for v in Adj_List[i]]):
                    Adj_List[i].append(self.V[j-1])
                    #Adj_List[i].append(e)

        return Adj_List

    def get_Edge(self,v,u): #from v ---> u
        for e in self.e_list:
            if ((v == e.V_from) and (u == e.V_to)) or ((u == e.V_from) and (v == e.V_to)):
                return e


    def print_Adj_List(self):
        for i in range(len(self.Adj_List)):
            print(i," : ",[v.id for v in self.Adj_List[i]])




class Edge:
    def __init__(self,V_from,V_to,w):
        self.V_from=V_from # from
        self.V_to=V_to # to
        self.w=w # weight

class Edges:
    def __init__(self):
        self.e_list=list()

    def get_Edges(self):
        return self.e_list
        





class Vertex:
    def __init__(self,id):
        self.id= id
        self.color="WHITE"
        self.d =float('Inf') #-1   # in order for the test in Hacker rank to pass
        self.py= None

class Vertics:
    def __init__(self,n):
        self.v_list=list()
        for id in range(1,n+1):
            self.v_list.append(Vertex(id))
    def get_Vertices(self):
        return self.v_list
