# Importing the library
from gtts import gTTS
import os

# Providing the text
input_text = "Hare krishana Hare rama Hare krishna Hare rama Hare krishana Hare rama Hare krishna Hare rama Hare krishana Hare rama Hare krishna Hare rama Hare krishana Hare rama Hare krishna Hare rama Hare krishana Hare rama Hare krishna Hare rama Hare krishana Hare rama Hare krishna Hare rama Hare krishana Hare rama Hare krishna Hare rama Hare krishana Hare rama Hare krishna Hare rama"

# Setting the language
language = "en"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating and saving the audio file
voice.save("demo.mp3")

# Playing the file
os.system("start demo.mp3")