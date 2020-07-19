from flask import Flask, make_response, request, jsonify
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(results()))
def results():
    req = request.get_json(force=True)   #json 파일로 받는다 json viewer에서 확인해 볼것
    base_url='https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8'

    print(req)
    print('----------------------환율을 알고싶은 나라-----------------------')

    countyText = req.get('queryResult').get('outputContexts')[0].get('parameters').get('any')   #json 정보에서 뽑아오자
    print("나라이름: "+countyText)

    result_url = '{}&query={}+환율'.format(base_url, countyText)   #네이버 환율 url 뽑아오자
    print("서버에서 받은 url : "+result_url)

    response = requests.get(result_url)
    soup = bs(response.content, 'html.parser')

    exchange_rate_won = soup.find(id="ds_from_money") #, attrs={'class': 'content_search section'}id="ds_from_money"
    exchange_rate = soup.find(id="ds_to_money")          #환율정보 가져오기
    exchange_rate_img_url = soup.find(alt="3개월그래프")

    print("그래프:"+ exchange_rate_img_url.get('src'))
    print("원화 :"+exchange_rate_won.get('value'))
    print("해외 환율 :"+exchange_rate.get('value'))


    ########################### 여기에 받아온 정보를 가지고 (삼성전자) 검색 후 밑에 return 에서 반환
    # 나는 일본 이라는 채팅을 받아서 -> 네이버 환율로 검색 (주식정보에서 사용했던 url + 기법으로)  ---> url 통해서 파싱 후 밑에 return 에서 환율 정보 반환 +( 가능하면 이미지도 반환)

    return {'fulfillmentMessages': [{'text':{'text':["나라 이름: " + countyText +"//  원화 "+exchange_rate_won.get('value') +"원 당 환율 : "+exchange_rate.get('value')+" 입니다. "]}}], 'fulfillmentImage': [{'image':{ 'image':[exchange_rate_img_url.get('src')]}  }]          } #, {'fulfillmentUrl' : exchange_rate_img_url.get('src')} #,exchange_rate_img_url.get('src')  #이건 딕셔너리 형태로 fulfillmenttext 로 보내면 스트링 형태로 보낼 수 있음

if __name__ == '__main__':
    app.run()


    #인천광역시 부평구를 qureryText로 받고 return fulfillmentMessages로 풀필먼트 리스폰
