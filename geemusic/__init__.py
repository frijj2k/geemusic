from flask import Flask
from flask_ask import Ask
from geemusic.utils.music_queue import MusicQueue

app = Flask(__name__)
ask = Ask(app, '/alexa')
queue = MusicQueue()

import geemusic.intents
import geemusic.controllers
