from gtts import gTTS
import os
text=('''Question seven is In which of these sports would you normally see the referee running on the field?

A. Cricket.

B. Football

C. Badminton

D. Tennis''')

speech = gTTS(text, 'en')
speech.save("Question7.mp3")