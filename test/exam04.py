from flask import Flask
import led

app = Flask(__name__)

@app.route('/')
def hello() :
    return "<h1>Hello World!</h1>"

@app.route('/led/on')
def led_on() :
    led.led_on()
    return "<h1>LED ON</h1>"

@app.route('/led/off')
def led_off() :
    led.led_off()
    return "<h1>LED OFF</h1>"

if __name__ == "__main__" :
    app.run(host='localhost', port=5000)