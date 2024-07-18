from flask import Flask,render_template

@app.route('/home')
def home():
	return render_template()