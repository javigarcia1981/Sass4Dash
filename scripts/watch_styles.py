""" Watch for file changes in 'src/styles' folder to launch SASS compiler  """
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from compile_styles import compile_sass


class ChangeHandler(FileSystemEventHandler):
    """ When style file is modified SASS compiler is launched """

    def on_modified(self, event):
        compile_sass()
        print("Compiled!")


observer = Observer()
observer.schedule(ChangeHandler(), path='src/styles/scss', recursive=True)
observer.start()

# First compilation
compile_sass()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
