from flask import Flask, render_template, url_for, request, redirect
import requests
import const

app = Flask(__name__)

@app.route('/<ticker>', methods=['GET'])
def index(ticker):
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-profile"
    querystring = {"symbol":ticker,"region":"US"}
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': const.RAPID_API_KEY
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.json()

    data = {
        'description': res['assetProfile']['longBusinessSummary'],
        'price': res['price']['regularMarketPrice']['fmt'],
        'name': res['price']['shortName']
        }
    return data

if __name__ == "__main__":
    app.run(debug=True)