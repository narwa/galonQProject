from flask import Flask,render_template
import datetime
import sqlite3
import paho.mqtt.client as mqtt
import time
import telegram_send as ts
import requests


app = Flask(__name__)
def telegram_bot_sendtext(bot_message):
    
    bot_token = '609109760:AAFzx05CJ96jT26WLZVtZC4rv0D-uOJN6TU'
    bot_chatID = '-379105000'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext("Testing Telegram bot")
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("topic")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))
    conn = sqlite3.connect('./galonku.db')
    c=conn.cursor()
    if str(msg.payload) == "b'KOSONG'" :
      print("KOSONG")
      telegram_bot_sendtext("GALON HABIS COOOY")
      c.execute("INSERT INTO data_galon (status,waktu) VALUES ('KOSONG',datetime('now','localtime'))")
    elif str(msg.payload) == "b'PENUH'" :
      print("PENUH")
      telegram_bot_sendtext("TERIMA KASIH MASBRO")
      c.execute("INSERT INTO data_galon (status,waktu) VALUES ('PENUH',datetime('now','localtime'))")
    conn.commit()
    conn.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


if __name__ == '__main__':
    app.run(debug=True)

