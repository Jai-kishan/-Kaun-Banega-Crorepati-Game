from gtts import gTTS
import os
text=('''Question four is Who is the only Vice President of India to have worked under three different Presidents?

a. S Radhakrishnan

b. Bhairo Singh Shekhawat

c. B D Jatti

d. Hamid Ansari''')

speech = gTTS(text, 'en')
speech.save("Question4.mp3")