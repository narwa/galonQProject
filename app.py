from flask import Flask,render_template
import datetime
import sqlite3
import paho.mqtt.client as mqtt
import time


app = Flask(__name__)

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
      c.execute("INSERT INTO data_galon (status,waktu) VALUES ('KOSONG',datetime('now','localtime'))")
    elif str(msg.payload) == "b'PENUH'" :
      print("PENUH")
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

