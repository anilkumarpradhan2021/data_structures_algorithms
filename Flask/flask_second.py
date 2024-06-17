from flask import Flask
app = Flask(__name__)

@app.route("/")
def index_page():
    return "Welcome to Index Page"

@app.route("/first/")
def first_page():
    return "Welcome to First Page"

@app.route("/dynamic/<page>")
def parameter_page(page):
    return f"Welcome to {page} Page"

if __name__=="__main__":
    app.run()
