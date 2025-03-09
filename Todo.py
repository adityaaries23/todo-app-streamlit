from datetime import datetime


class Todo:
    def __init__(self, title):
        self.title = title
        self.complete = False
        self.complete_at = None

    def set_complete(self):
        self.complete = True
        self.complete_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

