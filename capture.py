# ***************
# Imports
# ***************
from PIL import Image
from config import tesseract_cmd, captureInterval
import numpy as np
import win32gui
import pytesseract
import pyscreenshot as ImageGrab

# ***************
# Global variables
# ***************
data = { 'title': '', 'composer': '' }

# ***************
# pytesseract setting
# ***************
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

# ***************
# Functions
# ***************
# Find window
def capture ():
  print('Capturing...')
  global data

  # Find rekordbox window
  hwnd = win32gui.FindWindow(None, 'rekordbox')
  # Find rekordbox window position
  left, top, right, bot = win32gui.GetWindowRect(hwnd)

  # Find master track by getting track 1 master text color
  im = ImageGrab.grab(bbox=(862, 318, 863, 319))
  im_matrix = np.array(im)
  Track = 2 if im_matrix[0][0][0] == 19 else 1

  if Track == 1:
    # Get Track 1 title text position
    T1TitleLeft = left + 69
    T1TitleTop = top + 300
    T1TitleWidth = 735
    T1TitleHeight = 23
    T1TitleRight = T1TitleLeft + T1TitleWidth
    T1TitleBot = T1TitleTop + T1TitleHeight
    # Take screenshot of track 1 title
    im = ImageGrab.grab(bbox=(T1TitleLeft, T1TitleTop, T1TitleRight, T1TitleBot))
    # Save screenshot
    # im.save('./T1Title.png')
    # Extract text
    title = pytesseract.image_to_string(im, lang='jpn+eng').strip()
    # print(title)

    # Get Track 1 composer text position
    T1ComposerLeft = left + 69
    T1ComposerTop = top + 322
    T1ComposerWidth = 154
    T1ComposerHeight = 15
    T1ComposerRight = T1ComposerLeft + T1ComposerWidth
    T1ComposerBot = T1ComposerTop + T1ComposerHeight
    # Take screenshot of track 1 composer
    im = ImageGrab.grab(bbox=(T1ComposerLeft, T1ComposerTop, T1ComposerRight, T1ComposerBot))
    # Save screenshot
    # im.save('./T1Composer.png')
    # Extract text
    composer = pytesseract.image_to_string(im, lang='jpn+eng').strip()
    # print(composer)

  else:
    # Get Track 2 title text position
    T2TitleLeft = left + 1077
    T2TitleTop = top + 300
    T2TitleWidth = 735
    T2TitleHeight = 23
    T2TitleRight = T2TitleLeft + T2TitleWidth
    T2TitleBot = T2TitleTop + T2TitleHeight
    # Take screenshot of track 1 title
    im = ImageGrab.grab(bbox=(T2TitleLeft, T2TitleTop, T2TitleRight, T2TitleBot))
    # Save screenshot
    # im.save('./T2Title.png')
    # Extract text
    title = pytesseract.image_to_string(im, lang='jpn+eng').strip()
    # print(title)

    # Get Track 2 composer text position
    T2ComposerLeft = left + 1077
    T2ComposerTop = top + 322
    T2ComposerWidth = 154
    T2ComposerHeight = 15
    T2ComposerRight = T2ComposerLeft + T2ComposerWidth
    T2ComposerBot = T2ComposerTop + T2ComposerHeight
    # Take screenshot of track 1 composer
    im = ImageGrab.grab(bbox=(T2ComposerLeft, T2ComposerTop, T2ComposerRight, T2ComposerBot))
    # Save screenshot
    # im.save('./T2Composer.png')
    # Extract text
    composer = pytesseract.image_to_string(im, lang='jpn+eng').strip()
    # print(composer)

  # Update global variables
  data['title'] = title
  data['composer'] = composer

  # Print debug message
  print(f'Captured master track is {Track}, {data["composer"]} - {data["title"]}')