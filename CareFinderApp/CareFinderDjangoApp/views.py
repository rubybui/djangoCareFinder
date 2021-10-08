from django.shortcuts import render
import xmltodict, json 
import requests


def index(request):
    url  = "http://www.knautzfamilywi.com/CareFinder-1.0.0/api/hospitals/id/5114"
    city  = "Kenosha"
    header  = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'X-API-KEY': 'ecd81e2c619e423998acb1aade836470'}
    r = requests.get(url, headers=header)
    obj = xmltodict.parse(r.content)
    json_data = json.dumps(obj)
    print(json_data)
    data = json.loads(json_data)
    hospital = {
      "provider_id": data['xml']['item']['provider_id'],
      "hospital_name": data['xml']['item']['hospital_name'],
      "address": data['xml']['item']["address"],
      "city": data['xml']['item']["city"],
      "state": data['xml']['item']["state"],

    }
    context = {'hospital' :  hospital}
    print(hospital)
    return render(request, 'carefinder/index.html',context)