class User(object):

    def __init__(self, graph, values, name, zipCode):
        self.graph = graph
        self.name = name
        self.zipCode = zipCode
        self.state = 0
        self.values = values

    # def showOptions(self):
    #     edges = self.graph.get_edges(self.state)
    #     for node in edges[:]:
    #         print(self.values[node].action())
    #     option = input("Next Value?")
    #     self.state = option

    def process(self, node):
        return self.values[node].action()

    def update_zip(self, new_zip):
        self.zipCode = new_zip
