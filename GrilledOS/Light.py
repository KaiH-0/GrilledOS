import io
from base64 import b64encode
import eel
from phue import Bridge

eel.init('web')
#b = Bridge('192.168.0.34')
#b.connect()
#b.get_api()

@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

@eel.expose
def generate_qr(data):
    print("Light On")
    #b.set_light(1,'on',True)
    return

@eel.expose
def generate_qra(data):
    print("Light Off")
    #b.set_light(1,'on',False)
    return

@eel.expose
def generate_qrb(demo):
    #print(demo)
    #c = demo
    #cd = int(c)
    #b.set_light(1, 'bri', cd)
    return

@eel.expose
def generate_qrc(data):
    print("Turn Screen Off")
    #c = demo
    #cd = int(c)
    #b.set_light(1, 'bri', cd)
    return

eel.start('index.html',port=0,size=(480, 320))
