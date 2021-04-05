# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/4/5 15:00

from flask import Flask
import time

app = Flask(__name__)

@app.route('/an')
def index_an():
    time.sleep(2)
    return 'hello an'

@app.route('/echo')
def index_echo():
    time.sleep(2)
    return 'hello echo'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'hello tom'

if __name__ == '__main__':
    app.run(threaded=True)