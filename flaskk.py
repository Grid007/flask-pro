from flask import Flask,render_template,request
import pyrebase
app=Flask(__name__)

firebaseConfig = {
  "apiKey": "AIzaSyBvMQqKHT3lAJQeX0niMn-gB4n4N5h1qn4",
  "authDomain": "fssdp1-f53c7.firebaseapp.com",
  "databaseURL": "https://fssdp1-f53c7-default-rtdb.firebaseio.com",
  "projectId": "fssdp1-f53c7",
  "storageBucket": "fssdp1-f53c7.appspot.com",
  "messagingSenderId": "443722051751",
  "appId": "1:443722051751:web:03b2f3c7981e8d04106b82"
};
fbobj=pyrebase.initialize_app(firebaseConfig)

fdb=fbobj.database()
@app.route("/",methods=["GET","POST"])
def hello():
    global userdetails
    if(request.form):
        fd = request.form["btn"]
        if(fd=="Home"):
            return render_template("index.html")
        elif(fd == "Skills"):
            return render_template("skills.html")
        elif(fd == "Contact"):
            return render_template("contact.html")
        elif(fd == "Database"):
            dbnent=fdb.get()
            return render_template("database.html",data=dbnent.val())
        elif(fd == "cb"):
            ctcname=request.form["contact-name"]
            ctcnumber=request.form["contact-mobile"]
            ctcemail=request.form["contact-email"]
            reguc=fdb.child("RU").get().val()
            reguc+=1
            fdb.update({"contact-name"+str(reguc):ctcname,
            "contact-mobile"+str(reguc):ctcnumber,
            "contact-email"+str(reguc):ctcemail,
            "RU":reguc})
            return render_template("contact.html")
        elif(fd=="Delete"):
            fdb.remove()
            fdb.update({"RU":0})
            return render_template("contact.html")
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=False,port= 5051)