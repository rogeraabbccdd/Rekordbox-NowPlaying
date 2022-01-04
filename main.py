# Import flask to host a web server for OBS
from threading import Timer
from flask import Flask, render_template
from config import updateInterval, captureInterval
from capture import data, capture
from functools import partial

# Capture repeatedly
def repeat(func, interval):
  func()
  Timer(interval, partial(repeat, func, interval)).start()
repeat(capture, captureInterval)

# Flask settings
app = Flask(__name__)

# Flask routes
@app.route("/")
def home():
  global data
  return render_template(
    'index.html',
    title = data['title'],
    composer = data['composer'],
    interval = updateInterval
  )

# Run flask
app.debug = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run()
