from flask import Flask,render_template, request
import disasterLibrary as db
from wtforms import Form, StringField,SubmitField, validators
app = Flask(__name__, static_url_path='')

@app.route('/', methods={'GET','Post'})
def index():
    if request.method == "POST":
        phone = request.form.get('phone')
        zipcode = request.form.get('zipcode')
        db.addUserInfo("name", zipcode, phone)
        return render_template('thankYou.html')
    return render_template('signUp.html')

@app.route('/thankYou')
def thankYou():
    return render_template('thankYou.html')
if __name__ == "__main__":
    app.run(debug=True)
