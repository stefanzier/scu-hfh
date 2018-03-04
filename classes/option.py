# Add info flag
#   - 2 = Insert safe cities in user zip
#   - 3 = Insert user zip
#   - 4 = Insert evacuation routes
#   - 5 = shelters
#   - 6 = hospitals

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
        # TODO: DB Call to get safe cities
        cities = "Santa Clara, CA (0 miles), "
        cities += "Los Gatos, CA (11 miles), "
        cities += "San Mateo, CA (27 miles)"

        return cities

    def get_hospitals_in_zip(self, zip_code):
        # TODO: DB Call to get safe cities
        medical = "\n\nSanta Clara Valley Medical Center - (Capacity: 1300)\n\n"
        medical += "Kaiser San Jose - (Capacity: 302)\n"

        return medical

    def get_shelters_by_zip(self, zip_code):
        # TODO: DB Call to get safe shelters
        shelters = "\n(1) Bill Wilson Center - (Capacity: 102)\n"
        shelters += "(2) HomeFirst Services of Santa Clara County - (Capacity: 89)\n"

        return shelters

    def get_evac_routes_by_zip(self, zip_code):
        # TODO: DB Call to get safe cities
        routes = "Highways: 101 North, 280 North"
        return routes

    def text_with_user_data(self, user):
        if self.add_info_flag == 2:
            # Insert safe cities
            safe_cities = self.get_safe_cities_in_zip(user.zipCode)
            return self.text.replace("%", safe_cities)
        elif self.add_info_flag == 3:
            # Insert user zip into option text
            return self.text.replace("%", str(user.zipCode))
        elif self.add_info_flag == 4:
            # Insert user zip into option text
            routes = self.get_evac_routes_by_zip(user.zipCode)
            return self.text.replace("%", routes)
        elif self.add_info_flag == 5:
            # Insert user zip into option text
            shelters = self.get_shelters_by_zip(user.zipCode)
            return self.text.replace("%", shelters)
        elif self.add_info_flag == 6:
            # Insert user zip into option text
            medical = self.get_hospitals_in_zip(user.zipCode)
            return self.text.replace("%", medical)

    def ask_question(self, user):
        # if our text contains [] then we know we need to insert user data
        if "%" in self.text:
            return self.text_with_user_data(user)

        return " {}".format(self.text)
