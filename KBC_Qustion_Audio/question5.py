from gtts import gTTS
import os
text=('''Question five is Who wrote the Saraswati Vandana Var de Veenavaadini var de?

A. Jaishankar Prasad

B. Sumitranandan Pant

C. Ramdhari Singh Dinkar

D. Suryakant Tripathi Nirala''')

speech = gTTS(text, 'en')
speech.save("Question5.mp3")