from cmath import e
import email
from matplotlib.collections import Collection
import pymongo
import certifi
client = pymongo.MongoClient("mongodb+srv://root:kevin6290@mycluster.gqrtw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client.test
print("資料庫建立成功")


from flask import *
app = Flask(
    __name__,
    static_folder="static",  #控制 static 的位置
    static_url_path="/"
)
app.secret_key = "abchahaha"

#先處理路由

@app.route("/")
def homepage():
    msg = request.args.get("msg","")
    if msg == "success":
        return render_template("homepage.html",msg="註冊成功")
    else:
        return render_template("homepage.html")
    
@app.route("/member") 
def memberpage():
    if "nickname" in session:
        return render_template("memberpage.html") 
    else:
        return redirect("/")

#/error?msg=錯誤訊息
@app.route("/error")
def error():
    msg = request.args.get("msg","發生錯誤")
    return render_template("errorpage.html", msg=msg) #傳入錯誤msg

@app.route("/signup",methods = ["POST"])
def signup():
    #前端接收資料
    nickname = request.form["nickname"]
    email = request.form["email"]
    password= request.form["password"]
    #根據資料與資料庫互動
    collection = db.user
    #檢查是否有相同
    result = collection.find_one({
        "email": email
    })

    if result!= None:
        return redirect("/error?msg=會員信箱已被註冊")

    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password
    })
    return redirect("/?msg=success")

@app.route("/signin",methods=["POST"])
def signin():
    email = request.form["email"]
    password = request.form["password"]
    collection=db.user
    result = collection.find_one({
        "$and":[
            {"email":email},
            {"password":password} 
        ]
    })
    if result == None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    #if 登入成功，在sessoin中紀錄會員資訊，並導入會員頁面
    session["nickname"] = result["nickname"]
    return redirect("/member")

@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("/")

@app.route("/index")
def index():
    return render_template("index.html")

app.run() #這要放最後面