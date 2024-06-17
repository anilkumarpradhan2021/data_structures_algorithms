from flask import Flask,render_template
app = Flask(__name__)

# app name 
@app.errorhandler(404) 
  
# inbuilt function which takes error as parameter 
def not_found(e):
	return render_template("404.html") 

@app.route("/")
def home_page():
	return "Home Page"


if __name__ == "__main__":
	app.run(debug=True)