from gtts import gTTS
import os
text=('''
Question Nine is What characteristics of a leopard is used by scientists to identify them individually?

A. Pugmarks

B. Spot patterns

C. Tail

D. Whiskers''')

speech = gTTS(text, 'en')
speech.save("Question9.mp3")