# 6.00x Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


class WeightedDigraph(Digraph):
    def __init__(self):
        Digraph.__init__(self)
        self.edges = {}
        self.children = {}
        self.weights = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.children[node] = []
    def __str__(self):
        res = ''
        for k in self.edges:
        #for k in sorted(self.edges.iterkeys()):
        #for k in sorted(self.edges, key=self.edges.get):
            tup = (float(self.edges[k][0]),float(self.edges[k][1]))
            res = '{0}{1}->{2} {3}\n'.format(res, k[0],k[1], tup)
        return res[:-1]

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        weights = edge.getWeights()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.children[src].append(dest)
        self.edges[(src, dest)] = weights
    def childrenOf(self, node):
        return self.children[node]

class WeightedEdge(Edge):
    """
    A directed graph edge
    """
    def __init__(self,src, dest, distance, opendistance):
        Edge.__init__(self, src, dest)
        self.distance = distance
        self.opendistance = opendistance
    def getTotalDistance(self):
        return self.distance
    def getOutdoorDistance(self):
        return self.opendistance
    def getWeights(self):
        tup = (self.distance,self.opendistance)
        return tup
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.distance, self.opendistance)


nj = Node('j')
nk = Node('k')
nm = Node('m')
ng = Node('g')
g = WeightedDigraph()
g.addNode(nj)
g.addNode(nk)
g.addNode(nm)
g.addNode(ng)
randomEdge = WeightedEdge(ng, nm, 81, 24)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(ng, nm, 62, 5)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(ng, nk, 11, 8)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nj, ng, 91, 59)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(ng, nj, 88, 81)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nk, nj, 61, 17)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nk, nm, 26, 11)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nj, nk, 96, 8)
g.addEdge(randomEdge)
print g

'''
k->j (61.0, 17.0)
k->m (26.0, 11.0)
j->g (91.0, 59.0)
j->k (96.0, 8.0)
g->m (81.0, 24.0)
g->m (62.0, 5.0)
g->k (11.0, 8.0)
g->j (88.0, 81.0)
'''