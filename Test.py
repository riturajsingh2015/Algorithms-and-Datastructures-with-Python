from Graph_Algorithms import *
from Graph import *

class Test:
    """docstring for ."""

    def __init__(self, input_file="test_input.txt",output_file="test_output.txt"):
        self.input_file = open(input_file, 'r')
        self.output_file = open(output_file, 'r')

    def create_test_BFS(self): # changes need to be made
        ip=self.input_file
        op=self.output_file
        q=int(ip.readline())
        for q_itr in range(q):
            nm = ip.readline().split()

            n = int(nm[0])

            m = int(nm[1])

            Edge_List = []

            for _ in range(m):
                Edge_List.append(list(map(int, ip.readline().rstrip().split())))
            s = int(ip.readline())
            distances=BFS(Graph(n, Edge_List) , s).get_distances()
            x=list (map(int ,op.readline().rstrip().split(" ")) )
            print(distances==x)

    def create_test_MST_Kruskal(self):
        ip=self.input_file
        op=self.output_file
        g_nodes, g_edges = map(int, ip.readline().rstrip().split())

        V=Vertics(g_nodes).get_Vertices()
        #print([(v.id,v.py,v.color,v.d) for v in V])
        g_from = [0] * g_edges
        g_to = [0] * g_edges
        g_weight = [0] * g_edges

        E=Edges().get_Edges()
        for i in range(g_edges):
            g_from[i], g_to[i], g_weight[i] = map(int, ip.readline().rstrip().split())
            V_from=V[g_from[i]-1]
            V_to=V[g_to[i]-1]
            e=Edge(V_from,V_to,g_weight[i])
            E.append(e)

        G=Graph(V,E)

        MST_OP_result=int (op.readline().rstrip().split()[0])
        print( MST_Kruskal(G).get_MST_Sum() == MST_OP_result)

    def create_test_MST_Prim(self):
        ip=self.input_file
        op=self.output_file
        nm = ip.readline().split()
        n = int(nm[0])
        m = int(nm[1])

        V=Vertics(n).get_Vertices()
        #print([(v.id,v.py,v.color,v.d) for v in V])
        E=Edges().get_Edges()
        g_from = [0] * m
        g_to = [0] * m
        g_weight = [0] * m

        for i in range(m):
            g_from[i], g_to[i], g_weight[i] = map(int, ip.readline().rstrip().split())
            V_from=V[g_from[i]-1]
            V_to=V[g_to[i]-1]
            e=Edge(V_from,V_to,g_weight[i])
            E.append(e)

        root = int(ip.readline())

        G=Graph(V,E)

        MST_OP_result=int (op.readline().rstrip().split()[0])
        print( MST_Prim(G,root).mst_sum)
        print( MST_Prim(G,root).mst_sum==MST_OP_result )




#Test().create_test_MST_Kruskal()
Test().create_test_MST_Prim()
