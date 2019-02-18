from flask import Flask,render_template
# import mysql.connector
import datetime
import sqlite3
import paho.mqtt.client as mqtt
import time


app = Flask(__name__)

# def on_connect(client, userdata, flags, rc):
 
#     if rc == 0:
 
#         print("Connected to broker")
 
#         global Connected                #Use global variable
#         Connected = True                #Signal connection 
 
#     else:
 
#         print("Connection failed")

# def on_message(client, userdata, message):
#     print ("Message received: "  + message.payload)
#     if message.payload == "KOSONG" :
#       c.execute("INSERT INTO data_galon (status,waktu) VALUES ('KOSONG',datetime('now','localtime'))")
#     elif message.payload == "PENUH" :
#       c.execute("INSERT INTO data_galon (status,waktu) VALUES ('PENUH',datetime('now','localtime'))")
#     conn.commit()
#     conn.close()
 
# Connected = False   #global variable for the state of the connection
 
# broker_address= "localhost"  #Broker address
 
# client = mqttClient.Client("P1")               #create new instance
# client.on_connect= on_connect                      #attach function to callback
# client.on_message= on_message                      #attach function to callback
 
# client.connect(broker_address)          #connect to broker
 
# client.loop_start()        #start the loop
 
# while Connected != True:    #Wait for connection
#     time.sleep(0.1)
 
# client.subscribe("topic")
 
# try:
#     while True:
#         time.sleep(1)
 
# except KeyboardInterrupt:
#     print ("exiting")
#     client.disconnect()
#     client.loop_stop()

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



#     return render_template('hello.html', message="Hello World!")

#@app.route('/<name>')
#def hello_name(name):
#    return render_template('hello.html',message="Hello "+name)


# mycursor = mydb.cursor()

# sql = "insert into nostracrm.data_galon (status,waktu) values ('kosong',now())"
# mycursor.execute(sql)
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")


if __name__ == '__main__':
    app.run(debug=True)

