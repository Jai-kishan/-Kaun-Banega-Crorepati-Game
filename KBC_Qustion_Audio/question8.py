from gtts import gTTS
import os
text=('''Question Eight is Madhuri Dixits Bucket List is her film in which language?

A. English

B. Hindi

C. Marathi

D. Telugu''')

speech = gTTS(text, 'en')
speech.save("Question8.mp3")