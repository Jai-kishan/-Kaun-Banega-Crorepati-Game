from gtts import gTTS
import os
text=('''
Question fifteen is Which of these foods would complete the name of these three common dishes: Kadhai _______, Shahi _______, and Matar ______?

A. Dahi

B. Ghee

C. Paneer

D. Khoya''')

speech = gTTS(text, 'en')
speech.save("Question15.mp3")