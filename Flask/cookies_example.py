from flask import Flask, make_response, render_template, request
app = Flask(__name__)


@app.route('/') 
def index(): 
    return render_template('index2.html') 


@app.route("/setcookie", methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST': 
      user = request.form['nm'] 
      print(user)
     
   resp = make_response(render_template('cookie.html')) 
   resp.set_cookie('userID', user) 
   print(resp.data)
   return resp 
    
@app.route('/getcookie') 
def getcookie(): 
   name = request.cookies.get('userID') 
   return '<h1>welcome '+name+'</h1>'
 
if __name__=='__main__': 
    app.run(debug = True) 
