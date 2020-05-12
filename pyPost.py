import requests,json


# python post 请求方式的编码具有三种，
# 1.application/x-www-form-urlencoded 以form表单提交数据       就是提交对象
# 2.application/json 以json格式提交数据                        就是提交对象的json字符串
# 3.multipart/form-data   一般用来上传文件

# 第一种提交对象
url = 'http://127.0.0.1:3000/test'
data = {'key1':'value1','key2':'value2'}
res = requests.post(url,data=data)
print(res)


#第二种提交对象字符串
url = 'http://127.0.0.1:3000/testJson'
data = {'key1':'value1','key2':'value2'}
res = requests.post(url,data=json.dumps(data),headers={'Content-Type':'application/json'})
print(res)


# #第三种提交文件
# url = ''
# files = {'file':open('E:/test.txt','rb')}
# res = requests.post(url,files=files)
# print(res)
