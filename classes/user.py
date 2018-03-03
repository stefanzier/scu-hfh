import graph as graphs
import option as opt


values = dict()
values[1] = opt.Option(1, "Prepare", [2, 3])
values[2] = opt.Option(2, "Need help now", [1])
values[3] = opt.Option(3, "Third option", [1])


class User(object):

    def __init__(self, graph, name, zipCode):
        self.graph = graph
        self.name = name
        self.zipCode = zipCode
        self.state = 1

    def showOptions(self):
        edges = self.graph.get_edges(self.state)
        for node in edges[:]:
            print(values[node].print_text())
        option = input("Next Value?")
        self.state = option


if __name__ == "__main__":

    graph = graphs.Graph(None)

    graph.add_edge((1, 2))
    graph.add_edge((1, 3))
    graph.add_edge((2, 1))
    graph.add_edge((3, 1))

    user = User(graph, "Deen", 95050)

    while True:
        user.showOptions()
