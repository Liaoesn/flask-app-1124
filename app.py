#-----------------------
# 匯入Flask類別
#-----------------------
from flask import Flask, render_template

#-----------------------
# 產生一個Flask物件
# 名稱為app
#-----------------------
app = Flask(__name__)

#-----------------------
# 用裝飾器定義app的路由
#-----------------------
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/customer/test')
def customer_test():
    # data = {}
    # data['name'] ="王曉明"
    # data['gender'] = "男"
    
    data = {'name':'王曉明','gender':'男','age':20}
    
    return render_template('test.html', data=data)
@app.route('/customer/list')
def customer_list():
    
    data = [{'name':'王曉明','gender':'男','age':20,'ab':20},
            {'name':'王曉明2','gender':'男','age':21,'ab':20},
            {'name':'王曉明','gender':'男','age':22,'ab':20},
            {'name':'王曉明4','gender':'男','age':23,'ab':20},]
    
    return render_template('list.html', data=data)

#-----------------------
# 執行app
#-----------------------
if __name__ == '__main__':
    app.run(port=5000,debug=True)