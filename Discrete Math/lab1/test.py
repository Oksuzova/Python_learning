import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
import matplotlib

matplotlib.use("TkAgg")

graph = {'1': {'4', '5'},
         '2': {'2', '3'},
         '3': {'1', '4', '6'},
         '4': {'1', '5'},
         '5': {'7'},
         '6': {'2', '6', '7'},
         '7': {'4', '4'},
         '8': {'1', '2', '5', '1'}}


# ----------------------------------------------------------------------------------------------------------------------
def dfs_alg(gr, start, goal):
    unseen = [(start, [start])]
    while unseen:
        (node, path) = unseen.pop()
        for next in gr[node] - set(path):
            if next == goal:
                yield path + [next]
            else:
                unseen.append((next, path + [next]))
# ----------------------------------------------------------------------------------------------------------------------
edges = [[i, j] for i in graph.keys() for j in graph[i]]
G = nx.Graph()
G.add_nodes_from(graph.keys())
G.add_edges_from(edges)
nx.draw(G, with_labels=True)
plt.show()
# ----------------------------------------------------------------------------------------------------------------------
def set_graph(entr1, entr2, gr, edg):
    all_ways = list(dfs_alg(gr, entr1, entr2))
    print(f'Всі можливі шляхи: {all_ways}')
    min_len = all_ways[0]
    for i in range(len(all_ways) - 1):
        if len(min_len) > len(all_ways[i + 1]): min_len = all_ways[i + 1]
    print(f'Найкоротший шлях: {min_len}')
    short_ways = [(min_len[i], min_len[i + 1]) for i in range(len(min_len) - 1)]
    print(f'Ребра, по яким іде шлях: {short_ways}')
    # ------------------------------------------------------------------------------------------------------------------
    g = nx.Graph()
    g.add_nodes_from(gr.keys())
    nx.draw(g, pos=nx.shell_layout(g), with_labels=True, font_weight='bold')
    nx.draw_networkx_edges(g, pos=nx.shell_layout(g), edgelist=edg, edge_color='b',
                           with_labels=True)
    nx.draw_networkx_edges(g, pos=nx.shell_layout(g), edgelist=short_ways, edge_color='r',
                           with_labels=True)
    plt.show()

# ----------------------------------------------------------------------------------------------------------------------
root = Tk()
Label(root, text=f"Дромашко Артем\nІВ-93\nВаріант {9308 % 10 + 1}", font=('Verdana', 14)).grid(row=0, column=1)

Label(root, text="Вершина 1").grid(row=1, column=0)
Label(root, text="Вершина 2").grid(row=1, column=2)

e1 = Entry(root)
e2 = Entry(root)
b1 = Button(root, text="Показати", command=lambda: set_graph(e1.get(), e2.get(), graph, edges))

e1.grid(row=2, column=0)
e2.grid(row=2, column=2)
b1.grid(row=2, column=1)

root.mainloop()


# import networkx as nx
# import matplotlib.pyplot as plt
#
# G = nx.Graph()
#
# print(G.nodes()) # returns a list
# print(G.edges()) # returns a list
#
# G.add_node("A")
# G.add_nodes_from(["B", "C", "D", "E"])
#
# G.add_edge(*("A", "B"))
# G.add_edges_from([("A", "C"), ("B", "D"), ("B", "E"), ("C", "E")])
#
# print("Vertex set: ", G.nodes())
# print("Edges set: ", G.edges())
#
# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()
#
#
# from tkinter import *
# import matplotlib.pyplot as pyp
# import networkx as netx
# import matplotlib.backends.backend_tkagg
#
#
#
# class Lab3Python:
#     def __init__(self):
#         self.root = Tk()
#         self.root.geometry('900x600')
#
#         self.mainwin = Frame(self.root, relief=GROOVE, borderwidth=3, bg = "light blue")
#         self.mainwin.pack(fill=BOTH)
#
#         self.ridman = Frame(self.mainwin, bg = "pink")
#
#         self.ridEnt = Entry(self.ridman)
#         self.ridEnt.pack(side=BOTTOM, fill=BOTH)
#         self.myname = Label(self.ridman, text="Kopernak Liza, IO-91", bg="light green")
#         self.myname.pack(side=TOP)
#         self.newRid = Button(self.ridman, text="Add new rid between two vertices (using the space) ", relief=GROOVE, fg = "black", bg = "pink", command=self.newRidcom)
#         self.newRid.pack(side=TOP)
#         self.ridman.pack(side=LEFT, pady=5)
#
#         self.ridListnam = Label(self.mainwin, text = "The list of already existing rids",relief=GROOVE, fg = "black", bg ="pink")
#         self.ridListnam.pack(side = TOP)
#         self.ridList = Listbox(self.mainwin)
#         self.ridList.pack(side=TOP)
#
#         self.butSh = Button(self.mainwin, text='To show the shortest path',relief=GROOVE, bg = "light pink",command=self.myway)
#         self.butSh.pack(side=TOP, pady=1, padx = 20)
#
#         self.vertex1 = Frame(self.mainwin, bg = "light pink")
#         self.leb1 = Label(self.vertex1, text='First vertex', relief=GROOVE, bg = "light pink", fg ="black")
#         self.leb1.pack(side=TOP)
#         self.entVert1 = Entry(self.vertex1)
#         self.entVert1.insert(END, '---')
#         self.entVert1.pack(side=TOP)
#         self.vertex1.pack(side=TOP, pady=1)
#
#         self.vertex2 = Frame(self.mainwin, bg = "light pink")
#         self.leb2 = Label(self.vertex2, text="Second vertex",relief=GROOVE,  bg = "light pink", fg ="black")
#         self.leb2.pack(side=TOP)
#         self.entVert2 = Entry(self.vertex2)
#         self.entVert2.insert(END, '---')
#         self.entVert2.pack(side=TOP)
#         self.vertex2.pack(side=TOP, pady=5)
#
#
#         self.grahp = None
#         self.start = None
#
#         self.fig = pyp.figure(figsize=(5, 3))
#         self.place = self.fig.add_subplot(111)
#
#         self.way = None
#         self.way_edges = None
#
#         self.canva = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.fig, master=self.root)
#         self.canva.draw()
#         self.canva.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=TRUE)
#         self.draw()
#
#
#     def newRidcom(self):
#         self.ridList.insert(END, self.ridEnt.get())
#         edges = self.ridList.get(0, last=END)
#         self.grahp = netx.parse_edgelist(list(edges))
#         self.start = netx.spring_layout(self.grahp)
#         self.place.cla()
#         self.draw()
#         self.canva.resize_event()
#
#     def update(self):
#         self.root.title("Laba 3 Kopernak")
#         self.root.mainloop()
#
#
#     def draw(self):
#         if self.grahp is not None:
#             netx.draw(self.grahp, self.start, with_labels=True)
#         if self.way is not None:
#             netx.draw_networkx_nodes(self.grahp, self.start, nodelist=self.way, node_color='c')
#             netx.draw_networkx_edges(self.grahp, self.start, edgelist=self.way_edges, edge_color='m')
#
#     def myway(self):
#         point1 = self.entVert1.get()
#         point2 = self.entVert2.get()
#         self.way = netx.shortest_path(self.grahp, source=point1, target=point2)
#         self.way_edges = list(zip(self.way, self.way[1:]))
#         self.place.cla()
#         self.draw()
#         self.canva.resize_event()
#
#
# if __name__ == '__main__':
#     graph = Lab3Python()
#     graph.update()