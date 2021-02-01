from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myISM209CA2@localhost:5431/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'!\xc8\x02\x9f\x83k\xf7\x03w2dgX\xf1D\xb5\xb6\x97\x8b\xe8\x97\xd8\xd6\xdc'




@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route("/products-and-services/")
def products_and_services():
    return render_template('products-and-services.html', title="Products and Services")


@app.route("/about-us/")
def about_us():
    return render_template('about-us.html', title="About Us")


@app.route("/signup/")
def signup():
 return render_template('signup.html', title="SIGN UP", information="Use the form displayed to register")

@app.route("/process-signup/", methods=['POST'])
def process_signup():

 firstname = request.form['firstname']
 lastname = request.form['lastname']
 dateofbirth = request.form['dateofbirth']
 residentialaddress = request.form['residentialaddress']
 nationality = request.form['nationality']
 nationalidentificationnumber = request.form['nationalidentificationnumber']
 # let's write to the database
 try:
    user = models.User(firstname=firstname, lastname=lastname, dateofbirth=dateofbirth, residentialaddress=
    residentialaddress, nationality=nationality, nationalidentificationnumber=nationalidentificationnumber)
    db.session.add(user)
    db.session.commit()

 except Exception as e:
    # Error caught, prepare error information for return
    information = 'Could not submit. The error message is {}'.format(e.__cause__)
    return render_template('signup.html', title="SIGN-UP", information=information)

 # If we have gotten to this point, it means that database write has been successful. Let us compose success info

 # Let us prepare success feedback information

 information = 'User by name {} {} successfully added. The login name is the email address {}.'.format(firstname, lastname, email)

 return render_template('signup.html', title="SIGN-UP", information=information)


if __name__ == '__main__':
    app.run(port=5430)



