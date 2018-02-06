import datetime
import os
import sys
import time
import logging
import telegram
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

TOKEN = ""
CHAT_ID =
FILES_PATH = "/home/cctv/cctv"
LOCK_FILE = "/home/cctv/.locks/telegram-lock"


class MyEventHandler(FileSystemEventHandler):
    def __init__(self, observer, filename, bot):
        self.observer = observer
        self.filename = filename
        self.bot = bot

    def on_created(self, event):
        logging.info("New path found {}".format(event.src_path))
        if (not event.is_directory and event.src_path.endswith(self.filename)
            and not os.path.exists(LOCK_FILE)):
            now = datetime.datetime.now()
            logging.info("Try to sent photo {}".format(event.src_path))
            self.bot.sendPhoto(chat_id=CHAT_ID, photo=open(event.src_path,
                                                           'rb'))
            logging.info("Sent photo {}".format(event.src_path))
        else:
            logging.info("Found lock file, nothing to do")


def main(argv=None):
    path = FILES_PATH
    filename = '.jpg'

    observer = Observer()

    bot = telegram.Bot(TOKEN)

    event_handler = MyEventHandler(observer, filename, bot)
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
