from gtts import gTTS
import os
text=('''Question eleven is Which of these food items has different varieties such as Suji ka _______. Aate ka _______, Moong dal ka __________ and Gajar ka _______________?

A. Sharbat

B. Halwa

C. Pakora

D. Chaat''')

speech = gTTS(text, 'en')
speech.save("Question11.mp3")