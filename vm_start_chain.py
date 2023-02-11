"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("appelhan/pong")

    client.message_callback_add("appelhan/pong", on_message_from_pong)


def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "  msg: " + str(msg.payload, "utf-8"))


def on_message_from_pong(client, userdata, message):
    number = int(message.payload.decode())
    number += 1
    print("Custom callback  - Number:", number)
    time.sleep(1)
    client.publish("appelhan/ping", f"{number}")


if __name__ == '__main__':

    #create a client object
    client = mqtt.Client()
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect


#    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.connect(host="172.20.10.7", port=1883, keepalive=60)

    client.publish("appelhan/ping", f"0")
    
    client.loop_forever()

