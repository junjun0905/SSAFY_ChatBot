# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return 'Hello World!'
#
# @app.route('/webhook')
# def hello():
#     return 'Hello this is webhook!!!'
# # run the app
# if __name__ == '__main__':
#     app.run()

    #다이알로그 플로우가 내 웹서버에 접속 못하니까 ngrok 이용  (터널링 해준다)
    #/ webhook 으로 들어왔으면 다이알로그의 플라스크와 터널링
    ##################################################################################

#ngrok 실행 (ngrok http 5000) -> dialogflow 에서 풀필먼트 주소에 /webhook 붙여서 입력해서 나의 플라스크 웹서버와 연동,

from flask import Flask, make_response, request, jsonify
app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(results()))
def results():
    req = request.get_json(force=True)   #json 파일로 받는다 json viewer에서 확인해 볼것
    print(req)
    print('----------------------T-shirt 주문정보-----------------------')

    colorText = req.get('queryResult').get('outputContexts')[0].get('parameters').get('color')   #json 정보에서 뽑아오자
    addressText = req.get('queryResult').get('queryText')

    print("색상: "+colorText)
    print("주소: "+addressText)


    ########################### 여기에 받아온 정보를 가지고 (삼성전자) 검색 후 밑에 return 에서 반환
    # 나는 일본+환율 이라는 채팅을 받아서 -> 네이버 환율로 검색 (주식정보에서 사용했던 url + 기법으로)  ---> 밑에 return 에서 환율 정보 반환 +( 가능하면 이미지도 반환)

    return {'fulfillmentMessages': [{'text':{'text':["이거 내가 보낸거"]}}]}  #이건 딕셔너리 형태로 fulfillmenttext 로 보내면 스트링 형태로 보낼 수 있음
if __name__ == '__main__':
    app.run()


    #인천광역시 부평구를 qureryText로 받고 return fulfillmentMessages로 풀필먼트 리스폰

