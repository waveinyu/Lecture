from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sis7sux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

# 기록하기 API
@app.route("/bucket", methods=["POST"]) # save_bucket() / 서버 측에서는 버킷완료를 알아보기 위해 numbering이 필요하다
def bucket_post():
    bucket_receive = request.form['bucket_give']
    
    bucket_list = list(db.bucket.find({},{'_id':False}))
    count = len(bucket_list) + 1
    
    doc = {
        'num':count,
        'bucket':bucket_receive,
        'done':0
    }
    
    db.bucket.insert_one(doc)

    return jsonify({'msg': '버킷리스트 저장 완료!'})

# 데이터가 클라이언트에서 서버로 날아올 땐 String으로 온다
@app.route("/bucket/done", methods=["POST"]) # done_bucket(num)
def bucket_done():
    done_receive = request.form['done']
    num_receive = request.form['num_give'] # print(num_receive)
    # print(type(num_receive))
    
    if (int(done_receive) == 0): 
        db.bucket.update_one({'num':int(num_receive)},{'$set':{'done':1}})
        return jsonify({'msg': '버킷 완료!'})     
    else:
        db.bucket.update_one({'num':int(num_receive)},{'$set':{'done':0}})
        return jsonify({'msg': '취소 완료!'})    


# 전체 버킷리스트 보여주기 API
@app.route("/bucket", methods=["GET"]) # show_bucket()
def bucket_get():
    bucket_list = list(db.bucket.find({},{'_id':False}))
    return jsonify({'buckets': bucket_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)