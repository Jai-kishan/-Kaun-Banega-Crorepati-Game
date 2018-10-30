from gtts import gTTS
import os
text=('''Question ten is Which of these national flags has the most number of stars on them?

A. USA

B. Brazil

C. Australia

D. New Zealand''')

speech = gTTS(text, 'en')
speech.save("Question10.mp3")