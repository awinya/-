import requests
import json
# 账户管家数据获取
url='https://api.baidu.com/json/sms/service/LiveReportService/getAccountLiveData'
data={
    "header": {
        "username":"****",
        "password":"*****",     
        "token":"****",
        "target": "****",#账户管家中某个账户名，获取对应的数据
    },
    "body": {
        "dataType":1,
        "device":0
    }    
}
rep=requests.post(url,data=json.dumps(data),verify=False)
