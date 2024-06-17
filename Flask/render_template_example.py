from flask import Flask, render_template
app = Flask(__name__)

@app.route("/about/")
def about():
    sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
    return render_template("index5.html",sites=sites)


if __name__=="__main__":
    app.run(debug=True)