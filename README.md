# telegramBot
teelebot
### debian

    su root 
    apt update
    apt install -y git build-essential libssl-dev libffi-dev python3-pip python3-dev python3-setuptools python3-venv 
 
    adduser telebot
*************

    su telebot
    whoami
 
    git clone https://github.com/helgpro/botrep
 
    cd botep/
    ls -lh
    nano telebot.py 
 
 
    python3 -m venv botvirt
    ls -lah
    cd
    source /home/newbot/botrep/botvitr/bin/activate
    pip install -r /home/telebot/botrep/requirements.txt

    /home/telebot/botrep/.venv/bin/python /home/telebot/botrep/telebot.py

    exit
    su - user
    sudo su

    cd /etc/systemd/system/

    nano telebot.service
 
[Unit]
Description=My telebot
After=network.target
 
[Service]
User=telebot
Group=telebot
 
WorkingDirectory=/home/telebot/botrep/
Environment="PYTHONPATH=/home/telebot/botrep/"
ExecStart=/home/telebot/botrep/botvirt/bin/python /home/telebot/botrep/telebot.py
 
[Install]
WantedBy=multi-user.target
 
    sudo systemctl start telebot
    sudo systemctl status telebot
    sudo systemctl stop telebot
