import pywhatkit
try:
  pywhatkit.sendwhatmsg("+91xxxxxxxxxxx", 
                        "Hello ,I'm ASTHA . Nice to meet you.", 
                        0, 24)
  print("Successfully Sent!")

except:

  print("An Unexpected Error!")
