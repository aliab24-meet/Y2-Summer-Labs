from flask import Flask,render_template,redirect,url_for,request
import random as rend
from flask import session as login_session


app = Flask(__name__,
template_folder='template',
static_folder='statics')

app.config['SECRET_KEY']="your_secret_string"

lis=["yellow fortune","blue fortune","black fortune","white fortune","red fortune","large fortune","small fortune","orange fortune","pink fortune","nice fortune"]
	
@app.route('/')
def main():
	return render_template("home.html1")

@app.route('/home',methods=['GET','POST'])
def home():
	if(request.method == 'GET'):
		return render_template("home1.html")
	else:
		return redirect(url_for("login_session"))

@app.route('/login_page',methods=['POST','GET'])
def login_session():
	if request.method =='GET':
		return redirect(url_for("login_session"))
	else:
		x=request.form['month']
		username=request.form['username']
		login_session['month']=x
		login_session['username']=username
		if (len(x)>10):
			return render_template("wrong.html")
		else:
			return render_template("home1.html")	

@app.route('/fortune')
def fortune():
		x=lis[len(m)]
		return render_template("fortune.html",rrr=x)


if __name__ == '__main__':
    app.run(debug=True)