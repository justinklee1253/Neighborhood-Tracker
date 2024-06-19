from flask import Flask, render_template, request 

app = Flask(__name__) #makes our app a Flask app


#define routes in Flask, which are routes we would access on the web 
@app.route('/')
@app.route('/index')
def index(): #home page will return "Hello World!"
  return render_template('index.html')


if __name__ == "__main__": #make this run on our localhost
  app.run(host="0.0.0.0", port=8000) #localhost:8000 to see our app when we start it
