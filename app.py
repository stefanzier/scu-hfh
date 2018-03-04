from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

import classes.user as usr
import classes.graph as graphs
from classes.buildGraph import get_options

app = Flask(__name__)

account_sid = "AC60948ef84ea6b1dfd17e8a849e4d6441"
auth_token = "b7975bdbbdc5bde48d28ead0f880f81d"
client = Client(account_sid, auth_token)

# create our graph
graph = graphs.Graph(None)
options = get_options(graph)

user1 = usr.User(graph, options, "Stefan", 95053)
users = {"+16509954925": user1}


def send_message(phone, message):
    client.api.account.messages.create(
        to="+{}".format(phone),
        from_="+14085965335 ",
        body=message)


@app.route('/sms', methods=['POST'])
def sms():

    ### Receiving a response - so we know curren state is a question
    resp = MessagingResponse()

    number = request.form['From']

    user = users[number]
    message_body = request.form['Body']

    try:

        # if current option is of type 4 then we know we should do something
        #   with user input
        #     implement google maps api zip code lookup
        # if current_option = options[user.state] == 4
        # obtain the users response
        next_node_index = int(message_body)-1

        if (next_node_index < 0):
            resp.message("Please respond with a valid option number.")
            return str(resp)

        # get our list of next options
        edges = graph.get_edges(user.state)

        # get the option our user chose
        next_node = edges[next_node_index]
        user.state = next_node

        # each option has functionality it implements
        # ensure that functinality occurs
        # option.process_response()

        # The current option has only one next next_node
        edges = graph.get_edges(user.state)
        user.state = edges[0]

        # Now we have a ask_question
        # print the question and wait for response
        option = options[user.state]

        response_to_user = option.ask_question(user)

        resp.message(response_to_user)
        return str(resp)
    except ValueError:
        resp.message("Please respond with a valid option number.")
        return str(resp)


send_message("+16509954925", options[0].ask_question(users["+16509954925"]))
if __name__ == '__main__':
    app.run()
