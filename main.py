from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from models.users import User
from services.user_services import UserServices



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yekuc60n6T2lgumg7y40mIXhGQw9YKCul2f6OuTDm51e09dGNO5s9Wakh7aX58Iibvbq0Y37Q1Ns204YypgoNxn3610a1agfiUtA'

class UserCreateForm(FlaskForm):
    first_name = StringField('Ime')
    last_name = StringField('Prezime')
    pin_code = StringField('PIN')
    is_active = BooleanField('Aktivan?')
    submit = SubmitField('Kreiraj')



# http://www.domena.hr/
@app.route('/')
def index():
    user = UserServices().get_user()
    user_form = UserCreateForm()

    
    return render_template('index.html', user=user)


# http://www.domena.hr/about
@app.route('/about')
def about():
    return render_template('about.html')


# http://www.domena.hr/create-user
@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    user_form = UserCreateForm()

    if user_form.validate_on_submit():
        user_first_name = user_form.first_name.data
        user_last_name = user_form.last_name.data
        user_pin_code = user_form.pin_code.data
        user_is_active = user_form.is_active.data
        UserServices.create_user(User(user_first_name, user_last_name, user_pin_code, user_is_active))
        redirect(url_for('index'))

    return render_template('create-user.html', form=user_form)



if __name__ == '__main__':
    app.run(debug=True)
