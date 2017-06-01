from transitions.extensions import GraphMachine

#do not use tab , using space


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )


    def is_going_to_end(self, update):
        text = update.message.text
        return text == '我要走了'

    def is_going_to_user(self, update):
        text = update.message.text
        return text == '你好'
    
    def is_leaving_state1(self, update):
        text = update.message.text
        return text == '都不要'       

    def is_going_to_state1(self, update):
        text = update.message.text
        return text == '療癒'
	
    def is_going_to_state2(self, update):
        text = update.message.text
        return text == '搞笑'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text == '負能量'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text == '正能量'

    
    def is_leaving_state11(self, update):
        text = update.message.text
        return text == '不要了'

    def is_going_to_state11(self, update):
        text = update.message.text
        return text == '動物'
	
    def is_going_to_state12(self, update):
        text = update.message.text
        return text == '植物'


    def is_leaving_state21(self, update):
        text = update.message.text
        return text == '換別的'

    def is_going_to_state21(self, update):
        text = update.message.text
        return text == '笑話'

    def is_going_to_state22(self, update):
        text = update.message.text
        return text == '影片'

    def is_going_to_state23(self, update):
        text = update.message.text
        return text == '其他'


    def is_leaving_state31(self, update):
        text = update.message.text
        return text == '夠了'
	
    def is_going_to_state31(self, update):
        text = update.message.text
        return text == '粉絲專頁'
    
    def is_going_to_state32(self, update):
        text = update.message.text
        return text == '其他'

    def is_leaving_state41(self, update):
        text = update.message.text
        return text == '不用了'

    def is_going_to_state41(self, update):
        text = update.message.text
        return text == '經典'

    def is_going_to_state42(self, update):
        text = update.message.text
        return text == '溫暖'

    def is_leaving_state111(self, update):
        text = update.message.text
        return text == '不要了'
	
    def is_going_to_state111(self, update):
        text = update.message.text
        return text == '狗'

    def is_going_to_state112(self, update):
        text = update.message.text
        return text == '貓'

    def is_going_to_state113(self, update):
        text = update.message.text
        return text == '其他'
    
    def is_leaving_state121(self, update):
        text = update.message.text
        return text == '不要了'

    def is_going_to_state121(self, update):
        text = update.message.text
        return text == '花'
	
    def is_going_to_state122(self, update):
        text = update.message.text
        return text == '草'


    def is_going_to_state211(self, update):
        text = update.message.text
        return text == '嘿嘿嘿'
    
    def is_leaving_state211(self, update):
        text = update.message.text
        return text == '...'

    def is_going_to_state212(self, update):
        text = update.message.text
        return text.lower() == 'funny'

    def is_leaving_state212(self, update):
        text = update.message.text
        return text == '不好笑'
    

    def is_leaving_state221(self, update):
        text = update.message.text
        return text == '換別的'
   
    def is_going_to_state221(self, update):
        text = update.message.text
        return text == '豆豆先生'

    def is_going_to_state222(self, update):
        text = update.message.text
        return text == '這群人'

    def is_going_to_state223(self, update):
        text = update.message.text
        return text == '監獄兔'


    def is_going_to_state231(self, update):
        text = update.message.text
        return text == '進來看看'
    
    def is_leaving_state231(self, update):
        text = update.message.text
        return text == '爛透了'

    def is_leaving_state311(self, update):
        text = update.message.text
        return text == '夠了'

    def is_going_to_state311(self, update):
        text = update.message.text
        return text == '厭世動物園'

    def is_going_to_state312(self, update):
        text = update.message.text
        return text == '厭世哲學家'

    def is_going_to_state313(self, update):
        text = update.message.text
        return text == '來點負能量'

    def is_going_to_state321(self, update):
        text = update.message.text
        return text == '進來看看'
    
    def is_leaving_state321(self, update):
        text = update.message.text
        return text == '夠了'


    def is_leaving_state411(self, update):
        text = update.message.text
        return text == '謝謝'

    def is_going_to_state411(self, update):
        text = update.message.text
        return text == '經典1'

    def is_going_to_state412(self, update):
        text = update.message.text
        return text == '經典2'
	
    def is_going_to_state413(self, update):
        text = update.message.text
        return text == '經典3'


    def is_going_to_state421(self, update):
        text = update.message.text
        return text == '溫暖1'
    
    def is_leaving_state421(self, update):
        text = update.message.text
        return text == '太熱了'

    def is_going_to_state422(self, update):
        text = update.message.text
        return text == '溫暖2'

    def is_leaving_state422(self, update):
        text = update.message.text
        return text == '一點都不溫暖'

    def on_enter_end(self, update):
        update.message.reply_text("掰掰")
        print('in end')
        self.go_back(update)

    def on_exit_end(self, update):
        #update.message.reply_text("leave 1")
        print('leaving end')

    def on_enter_user(self, update):
        update.message.reply_text("你好～我是QQ，\n今天想要來點什麼呢～\n\t\t[療癒]\n\t\t[搞笑]\n\t\t[負能量]\n\t\t[正能量]")
        print('in initial')

    def on_exit_user(self, update):
        #update.message.reply_text("leave 1")
        print('leaving initial')
    
    def on_enter_state1(self, update):
        update.message.reply_text("想要療癒的[動物]還是[植物]還是[都不要]？")
        print('in 1')

    def on_exit_state1(self, update):
        #update.message.reply_text("leave 1")
        print('leaving 1')

    def on_enter_state2(self, update):
        update.message.reply_text("想要搞笑的[笑話]還是[影片]還是[其他]還是[都不要]？")
        print('in 2')

    def on_exit_state2(self, update):
        #update.message.reply_text("leave 2")
        print('leaving 2') 
  
    def on_enter_state3(self, update):
        update.message.reply_text("想看[粉絲專頁]還是[其他]還是[都不要]？")
        print('in 3')

    def on_exit_state3(self, update):
        #update.message.reply_text("leave 3")
        print('leaving 3')

    def on_enter_state4(self, update):
        update.message.reply_text("想要來個[經典]還是求個[溫暖]還是[都不要]？")
        print('in 4')

    def on_exit_state4(self, update):
        #update.message.reply_text("leave 4")
        print('leaving 4')


    def on_enter_state11(self, update):
        update.message.reply_text("想要[狗]還是[貓]還是[其他]還是[不要了]？")
        print('in 11')

    def on_exit_state11(self, update):
        #update.message.reply_text("leave 11")
        print('leaving 11')

    def on_enter_state12(self, update):
        update.message.reply_text("想要[花]還是[草]還是[不要了]？")
        print('in 12')

    def on_exit_state12(self, update):
        #update.message.reply_text("leave 12")
        print('leaving 12') 
  
    def on_enter_state21(self, update):
        update.message.reply_text("想要[嘿嘿嘿]還是[funny]還是[換別的]？")
        print('in 21')

    def on_exit_state21(self, update):
        #update.message.reply_text("leave 21")
        print('leaving 21')

    def on_enter_state22(self, update):
        update.message.reply_text("想要[豆豆先生]還是[這群人]還是[監獄兔]還是[換別的]？")
        print('in 22')

    def on_exit_state22(self, update):
        #update.message.reply_text("leave 22")
        print('leaving 22')

    def on_enter_state23(self, update):
        update.message.reply_text("[進來看看]還是[換別的]？")
        print('in 23')

    def on_exit_state23(self, update):
        #update.message.reply_text("leave 23")
        print('leaving 23')

    def on_enter_state31(self, update):
        update.message.reply_text("要看[厭世動物園]還是[厭世哲學家]還是要[來點負能量]還是[夠了]？")
        print('in 31')

    def on_exit_state31(self, update):
        #update.message.reply_text("leave 31")
        print('leaving 31') 
  
    def on_enter_state32(self, update):
        update.message.reply_text("[進來看看]還是[夠了]？")
        print('in 32')

    def on_exit_state32(self, update):
        #update.message.reply_text("leave 32")
        print('leaving 32')

    def on_enter_state41(self, update):
        update.message.reply_text("要閱讀[經典1]還是[經典2]還是[經典3]還是[不用了]？")
        print('in 41')

    def on_exit_state41(self, update):
        #update.message.reply_text("leave 41")
        print('leaving 41')

    def on_enter_state42(self, update):
        update.message.reply_text("要體驗[溫暖1]還是[溫暖2]還是[不用了]？")
        print('in 42')

    def on_exit_state42(self, update):
        #update.message.reply_text("leave 42")
        print('leaving 42')

    def on_enter_state111(self, update):
        update.message.reply_photo(open('res/dog.jpg','rb'))
        print('in 111')

    def on_exit_state111(self, update):
        #update.message.reply_text("leave 111")
        print('leaving 111') 
  
    def on_enter_state112(self, update):
        update.message.reply_sticker(open('res/totoro4.gif','rb'))
        print('in 112')

    def on_exit_state112(self, update):
        #update.message.reply_text("leave 112")
        print('leaving 112')

    def on_enter_state113(self, update):
        update.message.reply_photo(open('res/bravo.jpg','rb'))
        print('in 113')

    def on_exit_state113(self, update):
        #update.message.reply_text("leave 113")
        print('leaving 113')

    def on_enter_state121(self, update):
        update.message.reply_photo(open('res/flower.jpg','rb'))
        print('in 121')

    def on_exit_state121(self, update):
        #update.message.reply_text("leave 121")
        print('leaving 121')

    def on_enter_state122(self, update):
        update.message.reply_photo(open('res/plant.jpg','rb'))
        print('in 122')

    def on_exit_state122(self, update):
        #update.message.reply_text("leave 122")
        print('leaving 122') 
  
    def on_enter_state211(self, update):
        update.message.reply_text("選這個是想看到什麼")
        print('in 211')

    def on_exit_state211(self, update):
        #update.message.reply_text("leave 211")
        print('leaving 211')

    def on_enter_state212(self, update):
        update.message.reply_photo(open('res/funny.png','rb'))
        print('in 212')

    def on_exit_state212(self, update):
        #update.message.reply_text("leave 212")
        print('leaving 212')

    def on_enter_state221(self, update):
        update.message.reply_video(open('res/MrBean.mp4','rb'))
        print('in 221')

    def on_exit_state221(self, update):
        #update.message.reply_text("leave 221")
        print('leaving 221')

    def on_enter_state222(self, update):
        update.message.reply_video(open('res/TGOP_ SuperLousyCover Songs.mp4','rb'))     
        print('in 222')

    def on_exit_state222(self, update):
        #update.message.reply_text("leave 222")
        print('leaving 222') 
  
    def on_enter_state223(self, update):
        update.message.reply_video(open('res/rabbit.mp4','rb'))
        print('in 223')

    def on_exit_state223(self, update):
        #update.message.reply_text("leave 223")
        print('leaving 223')

    def on_enter_state231(self, update):
        update.message.reply_audio(open('res/laugh.mp3','rb'))
        print('in 231')

    def on_exit_state231(self, update):
        #update.message.reply_text("leave 231")
        print('leaving 231')

    def on_enter_state311(self, update):
        update.message.reply_text("傳送門： https://www.facebook.com/zooofdepression/ \n\t\t[夠了]")
        print('in 311')

    def on_exit_state311(self, update):
        #update.message.reply_text("leave 311")
        print('leaving 311')

    def on_enter_state312(self, update):
        update.message.reply_text("傳送門： https://www.facebook.com/hateworldphilosopher/ \n\t\t[夠了]")
        print('in 312')

    def on_exit_state312(self, update):
        #update.message.reply_text("leave 312")
        print('leaving 312')

    def on_enter_state313(self, update):
        update.message.reply_text("傳送門： https://www.facebook.com/NeEnergy/ \n\t\t[夠了]")
        print('in 313')

    def on_exit_state313(self, update):
        #update.message.reply_text("leave 313")
        print('leaving 313') 
  
    def on_enter_state321(self, update):
        update.message.reply_photo(open('res/dislike.jpg','rb'))
        print('in 321')

    def on_exit_state321(self, update):
        #update.message.reply_text("leave 321")
        print('leaving 321')

    def on_enter_state411(self, update):
        update.message.reply_document(open('res/classic1.txt','rb'))
        print('in 411')

    def on_exit_state411(self, update):
        #update.message.reply_text("leave 411")
        print('leaving 411')

    def on_enter_state412(self, update):
        update.message.reply_document(open('res/classic2.txt','rb'))
        print('in 412')

    def on_exit_state412(self, update):
        #update.message.reply_text("leave 412")
        print('leaving 412')

    def on_enter_state413(self, update):
        update.message.reply_document(open('res/classic3.txt','rb'))
        print('in 413')

    def on_exit_state413(self, update):
        #update.message.reply_text("leave 413")
        print('leaving 413') 
  
    def on_enter_state421(self, update):
        update.message.reply_photo(open('res/warm1.jpg','rb'))
        print('in 321')

    def on_exit_state421(self, update):
        #update.message.reply_text("leave 421")
        print('leaving 421')

    def on_enter_state422(self, update):
        update.message.reply_photo(open('res/warm2.jpeg','rb'))
        print('in 422')

    def on_exit_state411(self, update):
        #update.message.reply_text("leave 422")
        print('leaving 422')
