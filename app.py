from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

import classes.user as usr
import classes.graph as graphs
import disasterLibrary as db
from classes.buildGraph import get_options

app = Flask(__name__)

account_sid = "AC60948ef84ea6b1dfd17e8a849e4d6441"
auth_token = "b7975bdbbdc5bde48d28ead0f880f81d"
client = Client(account_sid, auth_token)

# Empty users map to store our DB users
users = {}


def send_message(phone, message):
    client.api.account.messages.create(
        to="+{}".format(phone),
        from_="+14085965335 ",
        body=message)


@app.route('/sms', methods=['POST'])
def sms():

    # Receiving a response - so we know curren state is a question
    resp = MessagingResponse()

    number = request.form['From']
    user = users[number]
    message_body = request.form['Body']

    try:
        curr_option = options[user.state]

        # obtain the users response
        next_node_index = int(message_body)-1

        if (next_node_index < 0):
            resp.message("Please respond with a valid option number.")
            return str(resp)

        # if current add_info_flag is of type 4 then we know we should
        #   update user zip code
        prepend_text = ""
        if curr_option.add_info_flag == 4:
            try:
                new_zip = int(message_body)
                # TODO: Update zip in mongo
                user.zipCode = new_zip
                prepend_text = "Thank you for updating your zip code!\n\n"
                next_node_index = int(curr_option.next_nodes[0])
                user.state = next_node_index
            except ValueError:
                resp.message("Please respond with a valid zip code.")
                return str(resp)

        # get our list of next options
        edges = graph.get_edges(user.state)

        # get the option our user chose
        next_node = edges[next_node_index]
        user.state = next_node

        # The current option has only one next next_node
        edges = graph.get_edges(user.state)
        user.state = edges[0]

        option = options[user.state]
        response_to_user = option.ask_question(user)

        if len(prepend_text) > 0:
            response_to_user = "{}{}".format(prepend_text, response_to_user)

        resp.message(response_to_user)
        return str(resp)
    except ValueError:
        resp.message("Please respond with a valid option number.")
        return str(resp)


# create our graph
graph = graphs.Graph(None)
options = get_options(graph)

# Add a user and pull it from DB
# user = db.addUserInfo("Stefan", 95053, "+16509954925")
# user = db.getUserInfo("+16509954925")
# users["+16509954925"] = usr.User(graph, options, user["Name"], user["ZIP"])
users["+16509954925"] = usr.User(graph, options, "Stefan", 95053)

test_user = users["+16509954925"]
send_message("16509954925", options[0].ask_question(test_user))
if __name__ == '__main__':
    app.run()
