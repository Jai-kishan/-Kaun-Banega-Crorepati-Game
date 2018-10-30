from gtts import gTTS
import os
text=('''Question thirteen is Which of these actresses became known as the Hawa-Hawai girl?

A. Sridevi

B. Hema Malini

C. Rekha

D. Madhuri Dixit''')

speech = gTTS(text, 'en')
speech.save("Question13.mp3")