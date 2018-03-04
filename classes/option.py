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

    def get_safe_cities_in_zip(self, zip_code):
        # TODO: API call to detect safe cities. For now sample data...
        cities = "Santa Clara, CA (0 miles), "
        cities += "Los Gatos, CA (10 miles), "
        cities += "San Mateo, CA (27 miles), "

        return cities

    def text_with_user_data(self, user):
        if self.add_info_flag == 3:
            # Insert user zip into option text
            return self.text.replace("[]", str(user.zipCode))
        elif self.add_info_flag == 2:
            # Insert safe cities
            safe_cities = self.get_safe_cities_in_zip(user.zipCode)
            return self.text.replace("[]", safe_cities)

    def ask_question(self, user):
        # if our text contains [] then we know we need to insert user data
        if "[]" in self.text:
            return self.text_with_user_data(user)

        return "  {}".format(self.text)
