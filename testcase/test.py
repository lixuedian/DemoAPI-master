import requests
import json
method ='post'
url = 'http://test-contract-potal.ekeguan.com/contract/seal/add'
h={
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdUlkIjoiNDA4IiwidXNlcm5hbWUiOiJsaXh1ZWRpYW4iLCJyZWFsbmFtZSI6Ilx1Njc0ZVx1OTZlYVx1NmJiZiIsIm5pY2tuYW1lIjoiIiwicHJvamVjdElkcyI6IjEsMiwzLDgiLCJncm91cElkIjoiMiIsImN1cnJlbnRQcm9qZWN0SWQiOiIxIiwibG9naW5OdW1zIjoiNDU5Iiwic3RhdHVzIjoiWSIsIm9sZFN1SWRzIjp7IjMiOiIxNzIiLCIyIjoiMzQwIiwiMSI6IjE3OCJ9LCJhdXRoVGltZSI6MTYwNzQ3NzA2N30.MZ0Ts27oK35gbgCGyLrjM0b6FkEVodkQPXPgEe6TJTo",
	"Content-Type": "application/json"
}

body={
  "url": "http://kg-oss-test-all.oss-cn-hangzhou.aliyuncs.com/contract/2020-12-10/1877906b96a74e389d3bad9222f36ed0-unnamed.jpg",
  "fileId":7366,
  "name": "课观教育005",
  "isDefault": 0,
  "status": 0,
  "remark": "测试",
  "version": "1.0"
}
url2='http://test-contract-potal.ekeguan.com/contract/template/determine'
par={'fileId':'7386'}

re = requests.post( url=url, headers=h, data=json.dumps(body))

print(re.json())

re2 = requests.get( url=url2, headers=h, params=par,verify = False)
print(re2.json())