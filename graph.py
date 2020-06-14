from collections import defaultdict
class Graph:
  def __init__(self,edge, n:int, directed:bool=False):
    self.__adjdict=defaultdict(set)
    self.__vertices=n
    self.__directed=directed 
    self.__createAdjList(edge, n)
    
  def insertEdge(self,edge:list):
    """
    insertEdge
    Input: 
      edge-a list containg two vertex where we insert an edge.
    """
    if edge[0]>self.__vertices:
      raise "Vertices Not found"
    else:
      if self.__directed==False:
        v, e= edge[::-1]
        self.__adjdict[v].add(e)
      v, e=edge
      self.__adjdict[v].add(e)

  @property
  def vertices(self):
    return self.__vertices

  @vertices.setter
  def vertices(self, n):
    if n>self.__vertices :
      self.__vertices=n

  #Create Adjacency List, n is no of vertex and e is list of edges.
  def __createAdjList(self,edge,n):
    """
    createAdjList
    Input:
      edge: 2 D array of all the edges to be inserted
      n:no of vertices 
    """
    for i in range(len(edge)):
      self.insertEdge(edge[i])
    #print (self.__adjdict)

  @property
  def adjdict(self):
    return self.__adjdict

  def isVertex(self, vertex):
    """
    isVertex: Indicating Valid vertex
    Input: 
      vertex: an integer
    Output:
      Boolean value: if vertex in range of (0,no of vertex) then return True else False
    """
    if vertex>self.__vertices or vertex<0:
      return False
    else :
      return True


  
  def outdegree(self,vertex:int):
    """
    outdegree: tells outdegree of a vertex
    Input:
      vertex: an integer
    Output: 
      returns outdegree 
    """
    if self.isVertex(vertex):
      return len(self.__adjdict[vertex])  
    else:
       raise "Vertex not found"
      
  
  def indegree(self, vertex:int):
    """
    indegree: tells indegree of a vertex
    Input:
      vertex: an integer
    Output: 
      returns indegree 
    """
    if self.isVertex(vertex):
      l1=[]
      for i in self.__adjdict.keys():
        if vertex in self.__adjdict[i]:
          l1.append(i)
      return len(l1)
    else: 
      raise "Vertex not found"
    

  def deleteEdge(self,deledge:list):
    """
    deleteEdge
    Input:
      edge-a list containg two vertex where we insert an edge.
    """
    v,e =deledge
    self.__adjdict[v].remove(e)
  
  def isolateVertex(self, delvertex:int):
    """
    isolateVertex
    Input: 
      Vertex: a vertex you want to disconnect
    """
    if self.isVertex(vertex):
      self.__adjdict.pop(delvertex)
      for i in self.__adjdict.keys():
        self.__adjdict[i].discard(delvertex)
    else:
      raise "Vertex not found"

  def __Traverse(self, vertex, visited, Type):
    l1=[]
    if self.isVertex(vertex):
      l1.append(vertex)
      visited.add(vertex)
      while l1!=[]:
        if Type=="BFS":
          vertex=l1.pop(0)
        elif Type=="DFS":
          vertex=l1.pop(-1)
        othvertex=self.__adjdict[vertex]
        for v in othvertex:
          if v not in visited:
            l1.append(v)
            visited.add(v)
    return visited

  def BFS(self, vertex:int= None):
    """
    BFS
    Input: 
      1.Vertex: an vertex who you want to traverse in BFS manner.
      2.Default: None, If no vertex given then it Traverse all the vertex 

    """
    visited=set()
    if vertex!=None:
      visited=self.__Traverse(vertex, visited, Type="BFS")
    else:
      for v in range(self.__vertices+1):
        if v not in visited:
          visited=self.__Traverse(v, visited, Type="BFS")
    return visited

  def DFS(self, vertex:int=None):
    """
    DFS
    Input: 
      1.Vertex: an vertex who you want to traverse in DFS manner.
      2.Default: None, If no vertex given then it Traverse all the vertex 
    """
    visited=set()
    if vertex!=None:
      visited=self.__Traverse(vertex, visited, Type="DFS")
    else:
      for v in range(self.__vertices+1):
        if v not in visited:
          visited=self.__Traverse(v, visited, Type="DFS")
    return visited




  

  