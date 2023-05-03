def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: x, filter(lambda x: x, f.read().split("\n"))))
  return l


class Vertex: 
  def __init__(self, name, neighbors):
    self.name: str = name
    self.neighbors: list(Vertex) = neighbors
    self.big: bool = not all(map(lambda x : x.islower(), name))
  
  def addNeighbor(self, vertex):
    if vertex not in self.neighbors:
      self.neighbors.append(vertex)
  
  def print(self):
    print("Name: {}".format(self.name))
    for e in self.neighbors:
      print("  | - {}".format(e))


class Graph: 
  def __init__(self,lines):
    vertices: list[Vertex] = []
    for line in lines:
      start, end = line.split("-")
      startV = False
      endV = False
      for v in vertices:
        if v.name == start:
          startV = v
        if v.name == end:
          endV = v
      if not startV:
        startV = Vertex(start, [])
        vertices.append(startV)
      if not endV:
        endV = Vertex(end, [])
        vertices.append(endV)
      
      if endV not in startV.neighbors:
        startV.addNeighbor(endV)
      if startV not in endV.neighbors:
        endV.addNeighbor(startV)
      

    self.vertices = vertices
    self.paths = 0
  

  # Shout out geeks for geeks for the heavy inspiration
  def buildAllPaths(self, node, visited, maxSmallVisit):
    if node.name.islower():
      if node.name in visited:
        visited[node.name] += 1
      else: 
        visited[node.name] = 1

    if node.name == 'end':
        self.paths += 1
        if self.paths % 5000 == 0:
          print(self.paths)
    else:
      for neighbor in node.neighbors:
        canVisitTwice = all(map(lambda x: x < maxSmallVisit, visited.values()))
        if neighbor.name not in visited or (neighbor.name != 'start' and neighbor.name != 'end' and canVisitTwice) or visited[neighbor.name] == 0:
          self.buildAllPaths(neighbor, visited, maxSmallVisit)

    if node.name in visited:
      visited[node.name] -= 1 


def part1():
  print('Day 12 part 1')
  lines = parseInput()
  graph = Graph(lines)
  for v in graph.vertices:
    if v.name == 'start':
      graph.buildAllPaths(v, {}, 1)
  print("Answer: {}".format(graph.paths))


def part2():
  print('Day 12 part 2')
  lines = parseInput()
  graph = Graph(lines)
  for v in graph.vertices:
    if v.name == 'start':
      graph.buildAllPaths(v, {}, 2)
  print("Answer: {}".format(graph.paths))
  

def main():
  part1()
  part2()

main()