import requests
import json
from pprint import pprint


class Comix():
    """docstring for Comix"""

    def getAllComix(self):
        response = requests.get(self.urlLib)
        response = response.json()
        totalPages = response['num']
        libraryPage = response['dados']
        for comix in libraryPage:
            print('STARTING COMIX ' + comix['titulo'] + '\n\n')
            chapter = requests.get(self.urlComix + comix['id'])
            pprint(chapter.json())
            break
        # response = json.loads(response)
