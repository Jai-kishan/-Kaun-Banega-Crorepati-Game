from gtts import gTTS
import os
text=('''Question two is Identify the film from this video clip (shows the video clip of the original Golmaal)

a. Chashme Baddour

b. Golmaal  

c. Padosan

d. Angoor''')

speech = gTTS(text, 'en')
speech.save("Question2.mp3")
# os.system("mpg321 jai.mp3")