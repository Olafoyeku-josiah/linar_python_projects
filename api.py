import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

querystring = {"from":"USD","to":"NGN","amount":"5"}

headers = {
	"X-RapidAPI-Key": "f332892779msha39d7da2929843fp166289jsncf9bf133e940",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data=json.loads(response.text)
converted_amount=data['result']['convertedAmount']
formatted="{:.2f}".format(converted_amount)
print(converted_amount,formatted)