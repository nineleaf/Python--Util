import flask

app =flask.Flask(__name__)
@app.route('/')
def Hello():
    print('this is main')
    return 'this is main'

@app.route('/test',methods=['POST'])
def test():
    print(flask.request)
    print(flask.request.form)#form表单获取数据
    print(flask.request.form.get('key1'))#form表单获取数据
    print(flask.request.form.getlist('key1'))#form表单获取数据
    return '3333'

@app.route('/testJson',methods=['POST'])
def testJson():
    print(flask.request)
    print(flask.request.get_data())#json获取byte数据
    print(flask.request.get_json())#json获取json数据
    return '3333'
if __name__ == '__main__':
    app.run(port=3000,debug=True)