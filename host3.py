from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello():
   if(request.form):
      fd = request.form["btn"]
      return render_template("homepage.html",data = fd)
      
   return render_template("homepage.html")

if __name__ == "_main_":
    app.run(debug=False,port = 5069)