from flask import Flask
import led18 as led
import ex09_select as db

app = Flask(__name__)

@app.route('/')
def index() :
    return "<h1>Hello World!</h1>"

# /led/on 라우팅, 응답은 'LED ON'
# /led/off, 'LED OFF'

@app.route('/led/on')
def led_on() :
    led.led_on()
    return "<h1>LED ON</h1>"

@app.route('/led/off')
def led_off() :
    led.led_off()
    return "<h1>LED OFF</h1>"

@app.route('/select')
def slt() :
    r = db.select_db()
    return r

if __name__ == "__main__" : # 서버를 직접 선언 했을 때만, 실행하기 위해서 사용
    app.run(host='192.168.219.41', port=5000)