from flask import Flask , render_template
app = Flask(__name__) 
  
@app.route('/home')  #decorator for route(argument) function 
def hello_admin():     #binding to hello_admin call 
   return 'Hello Admin'    
  
@app.route('/home2') 
def hello_guest():    #binding to hello_guest call 
   return 'Hello %s as Guest' % "ANIL KUMAR PRADHAN" 
  
@app.route('/test/') 
def hello_user():     
   return render_template("index4.html")

if __name__ == "__main__":
    app.run(debug=True)