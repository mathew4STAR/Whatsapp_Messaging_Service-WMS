import wms

messenger = wms.configure("pathtochromedriver", "Default", 5)
#configured wms to use the default profile and 5 seconds of buffer, and also provided the path to chromedriver

last_message = wms.read_last(messenger, "Contact")
#read last message from Contact
print(last_message)
#printing last message

wms.send_message(messenger, "Contact",  "Hello")
#send a message which says hello to Contact
