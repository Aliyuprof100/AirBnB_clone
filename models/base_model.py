#!/usr/bin/python3


"""This is the file that defines the basemodel class
whill serve as our base model for this console project
"""
import models
from uuid import uuid4
from datetime import datetime


class Basemodel():
    """This is tghe base models class"""
    def __init__(self, *args, **kwargs):
        """Instantiate a new Basemodel class".


        args:
            *args: Unused.
            **kwars (dict): Key value pairs of attributes.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
    def save(self):
        self.updated_at = datetime.now
        self.storage = storage


