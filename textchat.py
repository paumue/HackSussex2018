#Python version 3
from distutils.core import setup
import Requests
import os
from twilio.rest import Client
from flask import Flask
import lxml.etree
import lxml.builder

# Initializing environmental  variables

acount_sid= os.environ["twilio_account_sid"]
auth_token = os.environ["twilio_auth_token"]

# Initializing Twilio and Flask variables

client = Client(account_side, auth_token)

app = flask(__name__)


#Get text

#set text to textmessage

#Generate XML from text

def xml_gen(txtmsg):
    #TWXL categories
    RESPONSE = E.response
    #TWXL Fields
    SAY = E.say
    #Generate TWXL
    pagetwxl = RESPONSE(
                        SAY(txtmsg, voice = "Alice")
                        )
    return lxml.etree.tostring(pagetwxl)

#xmlfile = open(responsetwxl.xml,"w")
#xml_gen(textmessage).write(xmlfile)

@app.route("/xml", methods=['GET','POST'])
def xmlpage():
    return xml_gen


#Construct TWXL page on Flask


call = client.calls.create(
    to=os.environ["phone_number"]
    from_= os.environ["twilio_number"]
    url = ""
)
print(call.sid)
