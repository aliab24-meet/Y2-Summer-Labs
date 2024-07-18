from flask import Flask,render_template,redirect,url_for,request
import random as rend

app = Flask(__name__,
template_folder='template',
static_folder='statics')

lis=["yellow fortune","blue fortune","black fortune","white fortune","red fortune","large fortune","small fortune","orange fortune","pink fortune","nice fortune"]
@app.route('/home',methods=['GET','POST'])
def home():
	if(request.method == 'GET'):
		return render_template("home1.html")
	else:
 		name=request.form['month']
 		return redirect(url_for('fortune',m=name))

@app.route('/fortune/<string:m>')
def fortune(m):
	x=lis[len(m)%10]
	return render_template("fortune.html",rrr=x)


if __name__ == '__main__':
    app.run(debug=True)