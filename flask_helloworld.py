from flask import Flask

app = Flask(__name__) #모듈 만들 때 사용 (플라스크 객체 생성)

@app.route('/') #플라스크 객체가 만들어져서 해당 url 들어오면 밑에 함수 자동으로 실행 (데코레이터)
def index():
    return "Hello World!"

if __name__ == '__main__':  #플라스크 서버를 런해라
    app.run(debug=True)


#웹페이지 백엔드에 긁어서 가져올거야