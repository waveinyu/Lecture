from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sis7sux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

#1
@app.route("/homework", methods=["POST"])
def homework_post():    # 클라이언트에서 받은 데이터를 DB에 저장하기
    name_receive = request.form['name_give'] # name, comment
    comment_receive = request.form['comment_give'] # name, comment
    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.homework.insert_one(doc) # DB 저장
    return jsonify({'msg':'응원 완료!'}) 

@app.route("/homework", methods=["GET"])
def homework_get():
    comments_list = list(db.homework.find({},{'_id':False}))
    return jsonify({'comments':comments_list}) # 클라이언트에 읽어주기(GET)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


#check
