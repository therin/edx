# 6.00x Problem Set 10
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result

def load_map(mapFilename):

    print "Loading map from file..."
    result = WeightedDigraph()
    with open(mapFilename) as f:
        for line in f:
            from_node, to_node, total, outdoors = line.split()

            from_node = Node(from_node)
            to_node = Node(to_node)
            edge = WeightedEdge(from_node, to_node, float(total),float(outdoors) )
            try:
                result.addNode(from_node)
            except ValueError:
                pass
            try:
                result.addNode(to_node)
            except ValueError:
                pass
            result.addEdge(edge)
    return result
       


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
   Finds the shortest path from start to end using brute-force approach.
   The total distance travelled on the path must not exceed maxTotalDist, and
   the distance spent outdoor on this path must not exceed maxDisOutdoors.
 
   Parameters:
       digraph: instance of class Digraph or its subclass
       start, end: start & end building numbers (strings)
       maxTotalDist : maximum total distance on a path (integer)
       maxDistOutdoors: maximum distance spent outdoors on a path (integer)
 
   Assumes:
       start and end are numbers for existing buildings in graph
 
   Returns:
       The shortest-path from start to end, represented by
       a list of building numbers (in strings), [n_1, n_2, ..., n_k],
       where there exists an edge from n_i to n_(i+1) in digraph,
       for all 1 <= i < k.
 
       If there exists no path that satisfies maxTotalDist and
       maxDistOutdoors constraints, then raises a ValueError.
   """
   
    # Brute Force Outputs
    BFSResult = {}
    BFSResult1 = {}
   
    # Helper function to calculate Total Distance in a path
    def Dist(path):
        result = 0
        if path == None:
            return result
        if len(path) == 0:
            return result
        for i in range(len(path)-1):
            src = path[i]
            dest = path[i+1]
            for item in digraph.edges[src]:
                if item[0] == dest:
                    item = str(item[1][0])
                    result += float(item)
        return result    
   
    # Helper function to calculate Total Outdoor Distance in a path
    def Out(path):
        result = 0
        if path == None:
            return result
        if len(path) == 0:
            return result
        for i in range(len(path)-1):
            src = path[i]
            dest = path[i+1]
            for item in digraph.edges[src]:
                if item[0] == dest:
                    item = str(item[1][1])
                    result += float(item)
        return result    
    # Helper function using DFS method
    def find_shortest_path(graph, start, end, maxD, maxO, path = [], result = None):
        start = Node(start)
        end = Node(end)
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph.childrenOf(start):
            if node not in path:
                newpath = find_shortest_path(graph,node,end,maxD, maxO, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest) and Dist(newpath) <= maxD and Out(newpath) <= maxO:
                        distResult = Dist(newpath)
                        outDist = Out(newpath)
                        BFSResult[distResult] = newpath
                        BFSResult1[(distResult, outDist)] = newpath
        return BFSResult

    find_shortest_path(digraph, start, end, maxTotalDist, maxDistOutdoors)
    good = False
    BFSResult2 = {}
    for key in BFSResult1.keys():
        if key[0] <= maxTotalDist and key[1] <= maxDistOutdoors:
            BFSResult2[key[0]] = BFSResult1[key]
            good = True 
            if len(BFSResult) == 0:
                raise ValueError
    if good == False:
        raise ValueError
    end = []
    for shit in BFSResult2[min(BFSResult2)]:
        shit = str(shit)
        end.append(shit)
    return end
        
    '''
    def BFS(graph, start, end, maxD, maxO, path = [], result = None):
        start = Node(start)
        end = Node(end)
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph.childrenOf(start):
            if node not in path: #avoid cycles and constraints
                newPath = BFS(graph,node,end,maxD, maxO, path)
                if newPath!= None and Dist(newPath) <= maxD and Out(newPath) <= maxO:
                    shortest = newPath
                    if Dist(newPath) <= maxD and Out(newPath) <= maxO:
                        result = newPath
                        distResult = Dist(result)
            if result != None and distResult not in BFSResult:
                BFSResult[distResult] = result
                print sho
                break
       
    find_shortest_path(digraph, start, end, maxTotalDist, maxDistOutdoors)
    print BFSResult
    if len(BFSResult) == 0:
        raise ValueError
    else:
        end = []
        for shit in BFSResult[min(BFSResult)]:
            shit = str(shit)
            end.append(shit)
        return BFSResult[min(BFSResult)]

'''

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    pass

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
# if __name__ == '__main__':
#     Test cases
#     mitMap = load_map("mit_map.txt")
#     print isinstance(mitMap, Digraph)
#     print isinstance(mitMap, WeightedDigraph)
#     print 'nodes', mitMap.nodes
#     print 'edges', mitMap.edges


#     LARGE_DIST = 1000000

#     Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#     print "DFS: ", dfsPath1
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

map1 = load_map("map1.txt")
#print bruteForceSearch(map1, "1", "3", 100, 100)

map2 = load_map("map2.txt")
#print bruteForceSearch(map2, "1", "3", 100, 100)

map3a = load_map("map3a.txt")
#print bruteForceSearch(map3a, "1", "3", 100, 100)

map5 = load_map("map5.txt")
#print bruteForceSearch(map5, "1", "3", 100, 100)
#['1', '2', '4', '3']
#print bruteForceSearch(map5, "1", "5", 100, 100)
#['1', '2', '3']
#['1', '2', '4', '3']

#print bruteForceSearch(map2, "1", "3", 18, 18)
#['1', '4', '3']
#print bruteForceSearch(map2, "1", "3", 15, 15)
#['1', '4', '3']
#print bruteForceSearch(map2, "1", "3", 18, 0)
#ValueError successfully raised
##ValueError successfully raised

print bruteForceSearch(map5, "1", "3", 17, 8)
#['1', '2', '4', '3']
print bruteForceSearch(map5, "1", "5", 23, 11)
#['1', '2', '4', '3', '5']
print bruteForceSearch(map5, "4", "5", 21, 11)
#['4', '3', '5']
print bruteForceSearch(map5, "5", "1", 100, 100)
#ValueError successfully raised
print bruteForceSearch(map5, "4", "5", 8, 2)
#ValueError successfully raised
