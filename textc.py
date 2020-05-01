from gtts import gTTS 
import os 
mytext = 'Hello guys, Thank you so much f for 2 lakhs+ views and 1000+ subscribers on Our YouTube Channel Capturing Eye. [*Special Video]'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("welcome.mp3") 

os.system("mpg321 welcome.mp3") 
