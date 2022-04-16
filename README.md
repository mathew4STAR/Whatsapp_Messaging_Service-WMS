# Whatsapp_Messaging_Service-WMS

A free alternative to services like to Twilio to send whatsapp messages. It has quite a few problems, runs locally on your computer, little slow, but hey its free. 

# Installation:
`git clone https://github.com/mathew4STAR/Whatsapp_Messaging_Service-WMS`

# Requirments:
1. You will need to have [Chrome](https://www.google.com/chrome) installed on your computer.
2. You will need [Chromedriver](https://chromedriver.chromium.org/downloads).
3. You will need the selenium module
`pip install selenium`

# Usage
1. Copy the `wms.py` file to the folder your project is on.
2. To import WMS into your project `import wms.py`
3. You will first need to configure wms-
    `messenger = wms.configure("<pathtochromedriver", "<profile>", <buffer>)` (here the first attribute is the path to your chrome driver, the second attribute is the chrome profile you are using(Note: You need to be signed in to Whatsapp web in that profile)(Note: Conflicts might be created if you already have chrome open, it is recommended to create a new profile), the third attribute is the buffer you may have to increase or decrease this based on your internet speed)
4. To send a message use `wms.send_message(messenger, "Contact",  "Hello World")` (here the first attribute is the messenger you just created while configuring, the second attribute is the person you are sending the message to (Note: This number need to be saved in phone) , the third attribute is the message itself)
5. To read the last message someone send use `last_message = wms.read_last(messenger, "Contact")` (here the first attribute is the messenger you just created while configuring, the second attribute is the contact you want to read the message from.



