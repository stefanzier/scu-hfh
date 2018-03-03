from helpers import templates
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

account_sid = "AC60948ef84ea6b1dfd17e8a849e4d6441"
auth_token = "b7975bdbbdc5bde48d28ead0f880f81d"


@app.route('/sms', methods=['POST'])
def sms():
    # number = request.form['From']
    # message_body = request.form['Body']

    resp = MessagingResponse()
    resp.message(templates.generate_menu())

    return str(resp)


if __name__ == '__main__':
    app.run()
