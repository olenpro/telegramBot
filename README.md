# telegramBot
teelebot !
### debian

    su root 
    apt update
    apt install -y git build-essential libssl-dev libffi-dev python3-pip python3-dev python3-setuptools python3-venv 
 
    adduser telebot
*************

    su telebot
    whoami
 Созд каталог 
 
    сd /home/telebot/botrep
    git clone https://github.com/helgpro/botrep
    
либо пример простенького бота tbot.py 
> не называть telebot.py

    import telebot
    #1660344529:AAFxYzr0ddrLlaWiRvm8zXiVmWa35csYvws
    #testHelgBot
    #test_helgpro_bot
    bot = telebot.TeleBot("1660344529:AAFxYzr0ddrLlaWiRvm8zXiVmWa35csYvws")

    #obrabotchik komand
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
            bot.reply_to(message, "Howdy, how are you doing?")
    #obrabotchik sobiti
    @bot . message_handler ( func = lambda  m :  True )
    def  echo_all ( message ):
            if message.text=='Привет':
                    bot . reply_to (message, "О здоров!")
            elif  message.text=='kak':
                    bot . reply_to (message, " Норм как сам?")
            elif  message.text=='Хрень':
                    bot . reply_to (message, " и не говори")

    bot.polling()

 
  Вирт окружение
 
 
    python3 -m venv botvirt
    ls -lah
    cd
    source botvitr/bin/activate
    pip install -r /home/telebot/botrep/requirements.txt # зависимости в репозитори это потом 
 

    
установка модуля бота

    pip install pytelegrambotapi
    pip install requests
    
    pip freeze > requirements.txt
    
    
    su  telebot
   

    cd /etc/systemd/system/

    nano telebot.service
 > вставляем это дело возможно коменты убрать

    [Unit]
    Description=telebot //  произвольное имя
    After=syslog.target //
    After=network.target  //загрузка после старта сети

    [Service]
    Type=idle  //
    User=telebot  // юсер 
    Group=telebot  // группа
    WorkingDirectory=/home/telebot/botrep/   //рабочая папка
    Environment="PYTHONPATH=/home/telebot/botrep/"  //
    ExecStart=/home/.python/bin/python3 /home/telebot/botrep/tbot.py  //путь к питону и скрипту
    Restart=always   // в случаи падения перестартовать

    [Install]
    WantedBy=multi-user.target   //
 
 Переконфигуировать
 
    systemctl daemon-reload
    
   Старт бота 
    systemctl start telebot.service
    systemctl status telebot.service
    
    > статус зеленый и бот запуститься
    
   в sourse botvirt/bin/activate   в виртуальном ставим selenium
   #### установка webdriver debian
