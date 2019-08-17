# -*- coding: utf-8 -*-

import json
from random import *

class Grand_py:
    """ Character creation.
    """

    def __init__(self):
        """ Initialisation.
        """

        # Attribut
        self.query = None
        self.answer = None

    def introduction_sentence(self):
        """ Provide a random sentence.
        """

        # Open the json file
        with open("GrandPy_BotApp/static/json/GrandPy_answer.json", "r") as read_file:
            random_answer = json.load(read_file)

        # Provide a random number
        random_Number = randint(1, len(random_answer)-1)

        # Define a random sentence from the json file
        self.answer = random_answer["Beginning"][random_Number]