import configparser
from kanboard import Kanboard

class Kan():

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('settings.cfg')
        self.url = config['auth']['url']
        self.token = config['auth']['token']
        self.project_id = config['auth']['project']
        self.kb = self.auth()

    def auth(self):
        return Kanboard(self.url, 'jsonrpc', self.token)

    def create_task(self, text):
        self.kb.create_task(project_id=self.project_id, title=text)
