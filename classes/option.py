class Option(object):

    def __init__(self, o_id, text, next_nodes, add_info_flag, capacity=0):
        self.o_id = o_id
        self.text = text
        self.next_nodes = next_nodes
        self.capacity = capacity
        self.add_info_flag = add_info_flag

    # TODO: If we have info to add then conditionally add the
    #   user text into the self.text
    # def add_info_to_text(self)

    def update_capacity(self):
        if (self.capacity > 0):
            self.capacity -= 1

    def process_response(self, response):
        print("Process was called")


    def ask_question(self):
        return "  {}".format(self.text)
