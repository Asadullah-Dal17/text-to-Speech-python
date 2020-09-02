import pyttsx3 as ts

e = ts.init()
text = 'pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3.'

# e.say(text= text)
e.save_to_file(text= text, filename= 'ptt.mp3')
e.runAndWait()
e.stop()