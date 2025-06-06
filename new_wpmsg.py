import pywhatkit as pw
import datetime as dt
time=dt.datetime.now()                                                                           # Current time is taken
hour=time.hour 
minute=time.minute
try:
  pw.sendwhatmsg("+91*********",                                                                # Replace with the recipient's phone number and Ensure the phone number is in the correct format 
                        "Hello ,I'm name . Nice to meet you.",                                  # Replace with your message
                        hour, minute+2,)                                                        # You can change the time (in min)add example 5 or 10 etc minutes
  print("Successfully Sent!")

except Exception as e:
  
  print("An Unexpected Error!",e)
