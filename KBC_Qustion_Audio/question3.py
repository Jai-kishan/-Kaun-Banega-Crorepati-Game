from gtts import gTTS
import os
text=('''Question Three  is Which of these banks was founded in lahore in the 19th century?

a. Punjab and Sindh Bank

b. Punjab National Bank  (ans)

c. UCO Bank

d. Dena Bank''')

speech = gTTS(text, 'en')
speech.save("Question3.mp3")