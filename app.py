#pip3 install -r requiresment.txt
#./ngrok http 5000
#python3 app.py
#use space , do not use tab
#state名字要對應到fsm的function name

import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '348118568:AAGm6sIQeIFXMuIkINsuLv2mog8P6t8sz0I' #'Your Telegram API Token'
WEBHOOK_URL = 'https://72d3ce1d.ngrok.io/show-fsm'              #'Your Webhook URL'

#state1 = '療癒' state2 = '搞笑' state3 = '負能量' state4 = '正能量'
#state11 = '動物' state12 = '植物'
#state21 = '笑話' state22 = '影片' state23 = '搞笑其他
#'state31 = '粉絲專頁' state32 = '負能量其他'
#state41 = '經典' state42 = '溫暖'
#state111 = '狗' state112 = '貓' state113 = '療癒動物其他'
#state121 = '花' state122 = '草'
#state211 = '嘿嘿嘿 'state212 = 'funny'
#state221 = '豆豆先生 'state222 = '這群人' state223 = '監獄兔'
#state231 = '搞笑要進來看看嗎'
#state311 = '厭世動物園 'state312 = '厭世哲學家' state313 = '來點負能量'
#state321 = '負能量要進來看看嗎'
#state411 = '經典1' state412 = '經典2' state413 = '經典3'
#state421 = '溫暖1' state422 = '溫暖2'


app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'start',
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state11',
        'state12',
        'state21',
        'state22',
        'state23',  
        'state31',
        'state32',
        'state41',
        'state42',
        'state111',
        'state112',
        'state113',
        'state121',
        'state122',
        'state211',
        'state212',
        'state221',
        'state222',
        'state223',
        'state231',
        'state311',
        'state312',
        'state313',
        'state321',
        'state411',  
        'state412',
        'state413',
        'state421',
        'state422',
        'end'
    ],
    transitions=[
        {
            'trigger': 'go_back',
            'source': 'end',
            'dest': 'start'        
        },
        {  
           'trigger': 'advance',
            'source': ['user',
                       'state1',
                       'state2',
                       'state3',
                       'state4',
                       'state11',
                       'state12',
                       'state21',
                       'state22',
                       'state23',  
                       'state31',
                       'state32',
                       'state41',
                       'state42',
                       'state111',
                       'state112',
                       'state113',
                       'state121',
                       'state122',
                       'state211',
                       'state212',
                       'state221',
                       'state222',
                       'state223',
                       'state231',
                       'state311',
                       'state312',
                       'state313',
                       'state321',
                       'state411',  
                       'state412',
                       'state413',
                       'state421',
                       'state422'],
            'dest': 'end',
            'conditions': 'is_going_to_end' 
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'user',
            'conditions': 'is_going_to_user'            
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': ['state1','state2','state3','state4'],
            'dest': 'user',
            'conditions' : 'is_leaving_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state21',
            'conditions': 'is_going_to_state21'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state22',
            'conditions': 'is_going_to_state22'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state23',
            'conditions': 'is_going_to_state23'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state31',
            'conditions': 'is_going_to_state31'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state32',
            'conditions': 'is_going_to_state32'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state41',
            'conditions': 'is_going_to_state41'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state42',
            'conditions': 'is_going_to_state42'
        },
        {
            'trigger': 'advance',
            'source': ['state11','state12'],
            'dest': 'state1',
            'conditions' : 'is_leaving_state11'
        },
        {
            'trigger': 'advance',
            'source': ['state21','state22','state23'],
            'dest': 'state2',
            'conditions' : 'is_leaving_state21'
        },
        {
            'trigger': 'advance',
            'source': ['state31','state32'],
            'dest': 'state3',
            'conditions' : 'is_leaving_state31'
        },
       
        {
            'trigger': 'advance',
            'source': ['state41','state42'],
            'dest': 'state4',
            'conditions' : 'is_leaving_state41'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state111',
            'conditions': 'is_going_to_state111'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state112',
            'conditions': 'is_going_to_state112'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state113',
            'conditions': 'is_going_to_state113'
        },
        {
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state121',
            'conditions': 'is_going_to_state121'
        },
        {
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state122',
            'conditions': 'is_going_to_state122'
        },
        {
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state211',
            'conditions': 'is_going_to_state211'
        },
        {
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state212',
            'conditions': 'is_going_to_state212'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state221',
            'conditions': 'is_going_to_state221'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state222',
            'conditions': 'is_going_to_state222'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state223',
            'conditions': 'is_going_to_state223'
        },
        {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state231',
            'conditions': 'is_going_to_state231'
        },
        {
            'trigger': 'advance',
            'source': 'state31',
            'dest': 'state311',
            'conditions': 'is_going_to_state311'
        },
        {
            'trigger': 'advance',
            'source': 'state31',
            'dest': 'state312',
            'conditions': 'is_going_to_state312'
        },
        {
            'trigger': 'advance',
            'source': 'state31',
            'dest': 'state313',
            'conditions': 'is_going_to_state313'
        },
        {
            'trigger': 'advance',
            'source': 'state32',
            'dest': 'state321',
            'conditions': 'is_going_to_state321'
        },
        {
            'trigger': 'advance',
            'source': 'state41',
            'dest': 'state411',
            'conditions': 'is_going_to_state411'
        },
        {
            'trigger': 'advance',
            'source': 'state41',
            'dest': 'state412',
            'conditions': 'is_going_to_state412'
        },
        {
            'trigger': 'advance',
            'source': 'state41',
            'dest': 'state413',
            'conditions': 'is_going_to_state413'
        },
        {
            'trigger': 'advance',
            'source': 'state42',
            'dest': 'state421',
            'conditions': 'is_going_to_state421'
        },
        {
            'trigger': 'advance',
            'source': 'state42',
            'dest': 'state422',
            'conditions': 'is_going_to_state422'
        },
        {
            'trigger': 'advance',
            'source': ['state111','state112','state113'],
            'dest': 'state11',
            'conditions' : 'is_leaving_state111'
        },
        {
            'trigger': 'advance',
            'source': ['state121','state122'],
            'dest': 'state12',
            'conditions' : 'is_leaving_state121'
        },
        {
            'trigger': 'advance',
            'source': 'state211',
            'dest': 'state21',
            'conditions' : 'is_leaving_state211'
        },
        {
            'trigger': 'advance',
            'source': 'state212',
            'dest': 'state21',
            'conditions' : 'is_leaving_state212'
        },
        {
            'trigger': 'advance',
            'source': ['state221','state222','state223'],
            'dest': 'state22',
            'conditions' : 'is_leaving_state221'
        },
        {
            'trigger': 'advance',
            'source': 'state231',
            'dest': 'state23',
            'conditions' : 'is_leaving_state231'
        },
        {
            'trigger': 'advance',
            'source': ['state311','state312','state313'],
            'dest': 'state31',
            'conditions' : 'is_leaving_state311'
        },
        {
            'trigger': 'advance',
            'source': 'state321',
            'dest': 'state32',
            'conditions' : 'is_leaving_state321'
        },
        {
            'trigger': 'advance',
            'source': ['state411','state412','state413'],
            'dest': 'state41',
            'conditions' : 'is_leaving_state411'
        },
        {
            'trigger': 'advance',
            'source': 'state421',
            'dest': 'state42',
            'conditions' : 'is_leaving_state421'
        },
        {
            'trigger': 'advance',
            'source': 'state422',
            'dest': 'state42',
            'conditions' : 'is_leaving_state422'
        }
    ],
    initial='start',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

if __name__ == "__main__":
    _set_webhook()
    app.run()
