from gtts import gTTS
import pyglet
import time, os

def speaking(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = './temp.mp3'
    file.save(filename)

    music = pyglet.media.load(filename, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)
