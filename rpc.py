import discord_rpc
import time
from config import discordToken
from capture import data

def readyCallback(current_user):
  print('Our user: {}'.format(current_user))

def disconnectedCallback(codeno, codemsg):
  print(f'Disconnected from Discord rich presence RPC. Code {codeno}: {codemsg}')

def errorCallback(errno, errmsg):
  print(f'An error occurred! Error {errno}: {errmsg}')

start = time.time()

def updateRPC():
  discord_rpc.update_presence(
    **{
      'details': f"{data['composer']} - {data['title']}",
      'start_timestamp': start,
      'large_image_key': 'rekordbox'
    }
  )
  discord_rpc.update_connection()
  discord_rpc.run_callbacks()

# Note: 'event_name': callback
callbacks = {
  'ready': readyCallback,
  'disconnected': disconnectedCallback,
  'error': errorCallback,
}
discord_rpc.initialize(discordToken, callbacks=callbacks, log=False)
