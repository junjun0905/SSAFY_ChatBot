from flask import Flask
app = Flask(__name__)
@app.route('/user', methods=['GET'])
def get_user():
    return "GET /user called!!"
@app.route('/user', methods=['POST'])
def post_user():
    return "POST /user called!!"
@app.route('/user', methods=['PUT'])
def put_user():
    return "PUT /user called!!"
@app.route('/user', methods=['DELETE'])
def delete_user():
    return "DELETE /user called!!"
if __name__ == '__main__':
    app.run(debug =True)

    #크롤링과 챗봇 활용해서 뭘 개발할지지