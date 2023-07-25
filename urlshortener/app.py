from flask import Flask,render_template,request
import pyshorteners
app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    if request.method=="POST":
        l=request.form['name']
        shortener=pyshorteners.Shortener()
        x=shortener.tinyurl.short(l)
        return x
    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(port=5000,debug=True)