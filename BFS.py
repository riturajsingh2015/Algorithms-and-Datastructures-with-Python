class vertex:
  def __init__(self, number):
    self.id=number
    self.color = "WHITE"
    self.d = float('Inf')
    self.py= None


def find_vertex(vertices,number):
    found=False
    for v in vertices:
        if v.id ==number:
            return v

    return found




def bfs(n, m, edges, s):
    vertices=set()
    source=vertex(s)
    for number in set(range(1,n+1))-{s}:
        vertices.add(vertex(number))

    vertices.add(source)

    Adj_List = [[] for _ in range(n+1)]
    for (i,j) in edges:
        Adj_List[i].append(find_vertex(vertices,j))
        Adj_List[j].append(find_vertex(vertices,i))
        #Adj_List[i].append(j)
        #Adj_List[j].append(i)


    #print(Adj_List[1][0].id)

    #vertices.remove(source):
    source.color="GRAY"
    source.d=0
    source.py=None

    Q=[]
    Q.append(source)
    while Q !=[]:
        u=Q.pop()
        for v in Adj_List[u.id]:

    #        print(v.d , v.id , v.py, v.color)
            if v.color=="WHITE":
                v.color="GRAY"
                v.d=u.d+1
                v.py=u
                Q.append(v)
        u.color="BLACK"

    #print("----------------------------")
    dist = ["" for _ in range(n+1)]
    for v in vertices:
        #print( v.id, "Obj id:",v, v.d ,"Parent id:", v.py, v.color)
        dist[v.id] =v.d
    dist=dist[1:]
    dist =[ele *6 for ele in dist]
    for idx in range(len(dist)):
        if dist[idx]==float('Inf'):
            dist[idx]=-1
    dist.remove(0)

    print(dist)


#edges=[[1,2],[1,3]]
#bfs(4,2,edges,1)

#edges=[[2,3]]
#bfs(3,1,edges,2)

#edges=[[1,2],[1,3],[3,4]]
#bfs(5,3,edges,1)


#edges=[[1,2],[1,3],[3,4],[2,5],[2,6],[5,7],[5,6],[7,6],[8,7],[8,6]]
#bfs(8,10,edges,1)
#edges=[[1,2],[1,3],[3,4],[2,5],[2,6],[5,7],[5,6],[7,6]]
#bfs(8,8,edges,1)
