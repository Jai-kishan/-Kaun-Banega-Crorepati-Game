from gtts import gTTS
import os
text=('''Question one is Who is the first Indian woman wrestler to win a gold medal at the Asian Games?

A. Sakshi Malik

B. Babita Kumari

C. Vinesh Phogat

D. Kavita Devi''')

speech = gTTS(text, 'en')
speech.save("Question1.mp3")
# os.system("mpg321 jai.mp3")