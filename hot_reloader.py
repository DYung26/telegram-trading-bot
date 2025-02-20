import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BotReloader(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.restart_bot()

    def restart_bot(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(["python", "bot.py"])

    def on_any_event(self, event):
        if isinstance(event.src_path, str) and event.src_path.endswith(".py"):  # Only reload on Python file changes
            print(f"File changed: {event.src_path}, restarting bot...")
            self.restart_bot()

if __name__ == "__main__":
    path = "."  # Current directory
    event_handler = BotReloader()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

