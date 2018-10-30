from gtts import gTTS
import os
text=('''Question six is Who became the first Indian to score a century before lunch in the opening session of a Test Match in June 2018?

A. Lokesh Rahul

B. Shikhar Dhawan

C. Ajinkya Rahane

D. Rohit Sharma''')

speech = gTTS(text, 'en')
speech.save("Question6.mp3")