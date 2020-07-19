# from flask import Flask, request
# app = Flask(__name__)
# @app.route('/query')
# def index():
#     args = request.args
#     id = args.get('id')
#     print(id)
#     return "Query String!!"
# if __name__ == '__main__':
#     app.run(debug=True)

#json으로 받기

from flask import Flask, request
app = Flask(__name__)
@app.route('/body', methods=['POST'])
def request_body():
    print(request.json)
    body = request.json
    id = body['id']
    name = body['name']
    print(id)
    print(name)
    return "Request Body!!"
if __name__ == '__main__':
    app.run(debug=True)