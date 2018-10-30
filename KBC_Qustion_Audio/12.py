from gtts import gTTS
import os
text=('''Question twelve is Which of these is the name of a type of womens clothing?

A. Padmini

B. Man Bai

C. Jodha

D. Anarkali''')

speech = gTTS(text, 'en')
speech.save("Question12.mp3")