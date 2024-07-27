import pyrebase
from flask import session as login_session
from flask import Flask,request,url_for,redirect,render_template


app = Flask(__name__,
template_folder='templates',
static_folder='statics') 

app.config['SECRET_KEY']="your_secret_string"


firebaseConfig = {
  "apiKey": "AIzaSyApJQzxtiYLDmvoO6Ucxj-edeSP3VjxiLE",
  "authDomain": "game-lab-706ee.firebaseapp.com",
  "projectId": "game-lab-706ee",
  "storageBucket": "game-lab-706ee.appspot.com",
  "messagingSenderId": "652075151745",
  "appId": "1:652075151745:web:a0f14ecc0a6f0845e6b880",
  "measurementId": "G-PEQC8R8GLP",
  "databaseURL":"https://game-lab-706ee-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
y = 5.0
z = 1.0
x= float(y/z)

##db.child("games").push({"game_name": "Rocket lauge", "rate":"4.2", "info": "rocker is a fooball cars game"})
#d#b.child("games").push({"game_name": "fortnite", "rate":"4.0", "info": "fortnite is a gun shooting game"})



#     game_name = request.form['game_name']
#     try:
#         games = db.child("games").get()
#         matching_games = []
#         for game in games.each():
#             if game.val().get("game_name") == game_name:
#                 matching_games.append({
#                     "game_name": game.val().get("game_name"),
#                     "game_info": game.val().get("game_info"),
#
#                 })
#         return render_template('results.html', games=matching_games)
#           --==after that loop through the info in the html to show all the results==--
#     except Exception as e:
#         return e + "error"





@app.route('/',methods=['GET','POST'])
def main():
  return render_template("main.html")  





@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
  if request.method == 'POST':
    email=request.form['email']
    username=request.form['username']
    password=request.form['password']
    try:
      login_session['user'] = auth.create_user_with_email_and_password(email, password)
      user={"password":password,"username":username,"email":email}
      UID = login_session['user']['localId']
      db.child('Users').child(UID).set(user)
      return redirect(url_for('home'))
    except Exception as e:
      print(e)
      error = "Authentication failed"
  return render_template("sign_up.html")


@app.route('/sign_in',methods=['GET','POST'])
def sign_in():
  if request.method== 'POST':
    email=request.form['email']
    password=request.form['password']
  try:
    login_session['user'] = auth.sign_in_with_email_and_password(email, password)
    return redirect(url_for('home'))
  except Exception as e:
    print(e)
    error = "Authentication failed"
    return render_template("sign_in.html")
  


  return render_template("sign_in.html")


@app.route('/sign_out',methods=['GET','POST'])
def sign_out():
  if request.method == 'POST':
    login_session.clear()
  return render_template("sign_out.html")




@app.route('/home',methods=['GET','POST'])
def home():
  ctr=0
  flag = False
  if request.method =='POST':
    game_name = request.form['game_name']
    games = db.child("games").get().val()
    matching_games = []
    for key, game in games.items():
      print("passed game in games")
      print(game)
      if game['game_name'] == game_name:
        print("passed the if")
        ctr=ctr+1
        flag =True
        matching_games.append({
                     "game_name": game["game_name"],
                     "game_info": game["info"],
                     "game_rate": game["rate"]

        })
    print(matching_games)
    return render_template("game_page.html", games=matching_games,u=ctr)

  else:
    return render_template("home.html")


@app.route('/profile_page',methods=['GET','POST'])
def profile_page():
  return render_template("profile_page.html")

@app.route('/add',methods=['GET','POST'])
def add():
  if request.method=='POST':
    name=request.form['new_game_name']
    info=request.form['info']
    rate=request.form['rate']
    new_game={"name":name,"rate":rate,"info":info}
    db.child('games').push(new_game)
    return render_template("home.html")
  return render_template("adding_games.html")


@app.route('/game_page',methods=['GET','POST'])
def game_page():
  return render_template("game_page.html")

if __name__=='__main__':
  app.run(debug=True)

# route ('/game/<string:gamename>')
# show_x(gamename)
#db.cild.order by child = gamname

