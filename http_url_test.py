from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello World!!"

@app.route('/user')

def get_user():
    return "Hello User!!"

@app.route('/post')

def get_post():
    return "Hello Post!!"

@app.route('/user/list')

def get_user_list():
    return "Hello User List!!"

if __name__ == '__main__':
    app.run(debug=True)