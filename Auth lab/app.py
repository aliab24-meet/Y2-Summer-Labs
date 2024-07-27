import pyrebase
from flask import session as login_session
from flask import Flask,request,url_for,redirect,render_template


app = Flask(__name__,
template_folder='templates',
static_folder='statics') 

app.config['SECRET_KEY']="your_secret_string"


firebaseConfig = {
  "apiKey": "AIzaSyCXWB1K9oG9b3igHgc2ZjymNoJEP0vTsd8",
  "authDomain": "auth-lab-afd23.firebaseapp.com",
  "projectId": "auth-lab-afd23",
  "storageBucket": "auth-lab-afd23.appspot.com",
  "messagingSenderId": "954121086747",
  "appId": "1:954121086747:web:69cad84288c43b71e8d5be",
  "measurementId": "G-1LTK3ES0Q6",
  "databaseURL":"https://auth-lab-afd23-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()


@app.route('/home',methods=['GET','POST'])
def home():
  if request.method=='POST':
    quote=request.form['quote']
    date=request.form['date']
    speker=request.form['quotes enter']

    dict_info = {'text':quote,'uid':login_session['user']['localId'],'said_by':speker,'date':date}
    login_session['watan'] = dict_info
    db.child("quotes").push(dict_info)

    return redirect(url_for("thanks"))
  return render_template("home.html")

@app.route('/signout',methods=['GET','POST'])
def signout():
  if request.method=='GET':
    login_session.pop('user')
    return redirect(url_for("signup"))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  error = ""
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']   
    try:
      login_session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('home'))
    except Exception as e:
      print(e)
      error = "Authentication failed"
  return render_template("signin.html")


@app.route('/display', methods=['GET', 'POST'])
def display():
  quotes_dict_info = login_session['watan']
  return render_template("display.html",quotes = quotes_dict_info)


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
  return render_template("thanks.html")



@app.route('/', methods=['GET', 'POST'])
def signup():
  error = ""
  if request.method=='GET':
    return render_template("signup.html")
  else: 
    email = request.form['email']
    password = request.form['password'] 
    username = request.form['username']
    full_name = request.form['full_name'] 

    try:
      login_session['user'] = auth.create_user_with_email_and_password(email, password)
      login_session['quotes']=[]

      user={"full_name":full_name,"username":username,"email":email}
      UID = login_session['user']['localId']
      db.child('Users').child(UID).set(user)

      return redirect(url_for('home'))
    except Exception as e:
      print(e)
      error = "Authentication failed"
      return render_template("signup.html")
      
if __name__=='__main__':
  app.run(debug=True)
  