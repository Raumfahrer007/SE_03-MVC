from flask import current_app as app

class Name:

    def __init__(self, name):
        self.name = name
        app.logger.info("Name Object created")

    def get_name(self):
        return self.name