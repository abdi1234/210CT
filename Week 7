class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Queue:
     def __init__(self):
          self.items = []

     def isEmpty(self):
          return self.items == []

     def enqueue(self, item):
          self.items.insert(0,item)

     def dequeue(self):
          return self.items.pop()

     def size(self):
          return len(self.items)

class Graph:
     def __init__(self):
        self.graphDict = {}

     def addVertex(self,label):
          if label not in self.graphDict:
               self.graphDict[label] = []
               return("Vertex created")
          else:
                 return("Vertex exists")

     def addEdge(self,vertex1,vertex2):
          self.graphDict[vertex1].append(vertex2)
          self.graphDict[vertex2].append(vertex1)
          return("An edge has been created between",vertex1," and ",vertex2)

     def displayGraph(self):
          return self.graphDict

     def displayAdjacencyList(self):
          for k,v in self.graphDict.items():
               print(k , "|", v)

     def depthFirstSearch(self,startNode):
          s = Stack()
          visited = []
          s.push(startNode)
          while s.isEmpty() == False:
               u = s.pop()
               if u not in visited:
                    visited.append(u)
                    for e in self.graphDict[u]:
                         s.push(e)
          f = open("dfs.txt","w")
          f.write(str(visited))
          f.close
          return visited

     def breadthFirstSearch(self,startVertex):
          q = Queue()
          visited = []
          q.enqueue(startVertex)
          while q.isEmpty() == False:
               u = q.dequeue()
               if u not in visited:
                    visited.append(u)
               for edge in self.graphDict[u]:
                    if edge not in visited:
                         q.enqueue(edge)
          f = open("bfs.txt","w")
          f.write(str(visited))
          f.close
          return visited
          
          
                

if __name__ == "__main__":
    g = Graph()
    g.addVertex("a")
    g.addVertex("b")
    g.addVertex("c")
    g.addVertex("d")
    g.addVertex("e")
    g.addEdge("a","b")
    g.addEdge("a","e")
    g.addEdge("a","c")
    g.addEdge("b","e")
    g.addEdge("b","d")
    g.displayAdjacencyList()
    print(g.depthFirstSearch("a"))
    print(g.breadthFirstSearch("a"))
