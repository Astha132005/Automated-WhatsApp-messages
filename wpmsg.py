import pywhatkit
try:
  pywhatkit.sendwhatmsg("+919937081663", 
                        "Hello ,I'm ASTHA . Nice to meet you.", 
                        0, 24)
  print("Successfully Sent!")

except:

  print("An Unexpected Error!")