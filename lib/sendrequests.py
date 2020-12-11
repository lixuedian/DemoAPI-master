import os,sys,json
import config.readConfig

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class SendRequests():

    def get_Url(self):
        readconfig = config.readConfig.ReadConfig()
        # new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':8888' + '/login' + '?'
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl')
        return new_url

    """发送请求数据"""
    def sendRequests(self,s,apiData):
        try:
            # 从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url = apiData["url"]
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])
            type = apiData["type"]
            v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data)
            else:
                body = body_data

            #发送请求
            # re = s.request(method=method,  url=url, headers=h, params=par, data=body, verify=v)
            new_url = SendRequests().get_Url()
            # h = SendRequests().get_Url()
            re = s.request(method=method, url=new_url+url, headers=h, params=par, data=json.dumps(body), verify=v)
            return re
        except Exception as e:
            print(e)



# if __name__ == '__main__':# 验证拼接后的正确性
#     # new_url = SendRequests.get_Url()
#     print(SendRequests().get_Url())
#     # print(SendRequests().get_Url())
