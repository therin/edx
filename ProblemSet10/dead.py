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
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.children[node] = []
            self.edges[node] = []
    def __str__(self):
        res = ''
        for k in self.edges:
            for d,f in self.edges[k]:
                tup = (float(f[0]),float(f[1]))
                res = '{0}{1}->{2} {3}\n'.format(res, k, d, tup)
        return res[:-1]

        '''
        res = ''
        for k in self.edges:
        #for k in sorted(self.edges.iterkeys()):
        #for k in sorted(self.edges, key=self.edges.get):
            tup = (float(self.edges[k][0]),float(self.edges[k][1]))
            res = '{0}{1}->{2} {3}\n'.format(res, k[0],k[1], tup)
        return res[:-1]
        '''

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        weights = edge.getWeights()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.children[src].append(dest)
        some = (dest, weights)
        self.edges[src].append(some)
        #self.edges[(src, dest)] = weights
    def childrenOf(self, node):
        return self.children[node]

class WeightedEdge(Edge):
    """
    A directed graph edge
    """
    def __init__(self,src, dest, distance, opendistance):
        Edge.__init__(self, src, dest)
        self.weights = (distance, opendistance)
        self.distance = distance
        self.opendistance = opendistance
    def getTotalDistance(self):
        return self.distance
    def getOutdoorDistance(self):
        return self.opendistance
    def getWeights(self):
        return self.weights
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.distance, self.opendistance)


na = Node('a')
nb = Node('b')
nc = Node('c')
e1 = WeightedEdge(na, nb, 15, 10)
print isinstance(e1, Edge)
print isinstance(e1, WeightedEdge)
print e1.getSource()
print e1.getDestination()
print e1.getTotalDistance()
print e1.getOutdoorDistance()