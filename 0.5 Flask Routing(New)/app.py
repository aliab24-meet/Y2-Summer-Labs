from flask import Flask

app= Flask(__name__)

@app.route("/food1")
def food1():
	return '''<html> 
	<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/800px-Good_Food_Display_-_NCI_Visuals_Online.jpg">
	<a href="/food2">next food pic</a>
	<a href="/home">home</a>
	</html>'''
@app.route("/food2")
def food2():
	return '''<html> 
	<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsfR6QS0Jda7nwIK4qy1bSXSRVzJmQxmt0LA&s">
	<a href="/food3">next food pic</a>
	</html>'''
@app.route("/food3")
def food3():
	return '''<html> 
	<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzYWcUVg_I6A6RSYQ-HKY4Szdq7tBFTc65Eg&s">
	<a href="/home">home</a>
	</html>'''	

@app.route("/pet1")
def pet1():
	return '''<html> 
	<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSddqc-p4xRroa90v8AImxUooUElCQV45yPoQ&s">
	<a href="/pet2">next food pic</a>
	</html>'''
@app.route("/pet2")
def pet2():
	return '''<html> 
	<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmdrvCoofM1s2X155newV6ptaTFvvb6wqt3g&s">
	<a href="/home">home</a>
	<a href="/pet1">next pet pic</a>
	<a href="/pet3">next pet pic</a>
	</html>'''
@app.route("/pet3")
def pet3():
	return '''<html> 
	<img src="https://t3.ftcdn.net/jpg/04/81/85/46/360_F_481854656_gHGTnBscKXpFEgVTwAT4DL4NXXNhDKU9.jpg">
	<a href="/pet2">next pet pic</a>
	</html>'''	

@app.route("/space1")
def space1():
	return '''<html> 
	<img src="https://starwalk.space/gallery/images/what-is-space/1920x1080.jpg">
	<a href="/space3">next space pic</a>
	<a href="/space2">next space pic</a>
	<a href="/home">home</a>
	</html>'''
@app.route("/space2")
def space2():
	return '''<html> 
	<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE8rlBbqnDycGlg4HYo7CnnMOdSE7JA6ICkg&s">
	<a href="/space3">next space pic</a>
	<a href="/space1">next space pic</a>
	</html>'''
@app.route("/space3")
def space3():
	return '''<html> 
	<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Webb%27s_First_Deep_Field.jpg/1200px-Webb%27s_First_Deep_Field.jpg">
	<a href="/space2">next space pic</a>
	<a href="/space1">next space pic</a>
	</html>'''	

@app.route("/home")
def Home():
	return '''<html> 
	<h1> welcom!</h1>
	<p> welcome home <p>
	<a href="/food1">go to the first food photo!</a>
	<a href="/pet2">go to the second pet photo!</a>
	<a href="/space1">go to the first space photo!</a>
	</html>'''

if __name__ == '__main__':
    app.run(debug=True)