import graph as graphs

values = dict();
values[1] = "start";
values[2] = "second node";
values[3] = "third node";

class User(object):

	def __init__(self, graph, name, zipCode):
		self.graph = graph;
		self.name = name;
		self.zipCode = zipCode;
		self.state = 1;

	def showOptions(self):
		print values[self.state];
		edges = self.graph.get_edges(self.state);
		for node in edges[:]:
			print "option : ", node
		option = input("Next Value?")
		self.state = option

if __name__ == "__main__":

	graph = graphs.Graph(None);

	graph.add_edge((1,2));
	graph.add_edge((1,3));
	graph.add_edge((2,1));
	graph.add_edge((3,1));

	user = User(graph,"Deen",95050);

	while True:

		user.showOptions();






