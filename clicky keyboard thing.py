import winsound
from pynput.keyboard import Key, Listener
import keyboard

def on_press(key):
    #print(key)
    if keyboard.is_pressed('enter'):
    	winsound.PlaySound('jeff.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
    	winsound.PlaySound('click.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

with Listener(on_press=on_press) as listener:
    listener.join()
