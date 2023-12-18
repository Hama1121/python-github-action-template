import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    if r.status_code == 200:
        data = r.json()
        
      name: Windows - RustDesk

on:
  workflow_dispatch:

jobs:
  build:
    name: Start Building...
    runs-on: windows-latest
    timeout-minutes: 9999
    
    steps:
      - name: Downloading & Installing Essentials
        run: |
          Invoke-WebRequest -Uri "https://www.dropbox.com/scl/fi/qdyd4p9t6xoabl95n5o3g/Downloads.bat?rlkey=snr74vv1vr8k5suujugvrhjtm&dl=1" -OutFile "Downloads.bat"
          cmd /c Downloads.bat

      - name: Log In To AnyDesk
        run: cmd /c show.bat

      - name: Time Counter
        run: python time.py
