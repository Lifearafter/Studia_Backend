import os
import sys
import json

if __package__:
    parentdir = os.path.dirname(__file__)
    rootdir = os.path.dirname(parentdir)
    if rootdir not in sys.path:
        sys.path.append(rootdir)
    if parentdir not in sys.path:
        sys.path.append(parentdir)

import constants as const
from chunks import Chunk


class Summary:
    def __init__(self):
        self.obj1 = Chunk()


if __name__ == "__main__":
    obj = Summary()
