class Option(object):

    def __init__(self, o_id, text, next_nodes, capacity=0):
        self.o_id = o_id
        self.text = text
        self.next_nodes = next_nodes
        self.capacity = capacity

    def update_capacity(self):
        if (self.capacity > 0):
            self.capacity -= 1

    def print_text(self):
        return "  {}".format(self.text)
