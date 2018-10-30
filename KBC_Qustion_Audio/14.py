from gtts import gTTS
import os
text=('''Question fourteen is Samukha, Vighnaharta and Ekadanta are other names for which Hindu god?

A. Brahma

B. Krishna

C. Rama

D. Ganesha''')

speech = gTTS(text, 'en')
speech.save("Question14.mp3")