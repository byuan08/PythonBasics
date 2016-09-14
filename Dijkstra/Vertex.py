class Vertex:

	def __init__(self, node):
		self.id = node
		self.neighbors = {}

	def add_neighbor(self, *neighbors, *weight=0)
		assert len(neighbors)==len(weight), 
		"""Error: the length of neighbors 
			is not equal to lengh of weight
		"""
		for x,y in neighbors, weight:
			self.neighbors[x] = y

	def get_id(self):
		return self.id

	def get_weight(self, neighbor):
		return self.neighbors[neighbor]



class Graph:

	def __init__(self):
		
		self.vertices = {}
		self.paths = []


	def add_edge(self, startnode, endnode, weight):
	# startnode and endnode are just strings indicating the name of the coresponding vertices

		if self.vertices[startnode] = NULL:
			self.add_vertex(self, startnode)
		if self.vertices[endnode] = NULL:
			self.add_vertex(self, endnode)

		self.paths[startnode].add_neighbor(endnode, weight)
		self.paths[endnode].add_neighbor(startnode, weight)

	def add_vertex(self, node):
		vertex = Vertex(node)
		self.vertices[node] = vertex

	def get_vertex(self, node):
		return self.vertices[node]

	def get_all_vertices():
		return self.vertices.keys()





