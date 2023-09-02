import os
import sys
import json
import re
import html

import constants as const

parentdir = os.path.dirname(__file__)
rootdir = os.path.dirname(parentdir)

if __package__:
    if rootdir not in sys.path:
        sys.path.append(rootdir)
    if parentdir not in sys.path:
        sys.path.append(parentdir)


class Chunk:

    """
    Coverts the text file into chunks of words.
    """

    def __init__(self):
        file_text = self.get_data()
        cleaned_text = self.clean_text(file_text)
        self.split_chuncks(cleaned_text)

    def get_data(self) -> str:
        text_file_path = os.path.join(rootdir, 'resources', 'chapters.txt')

        chapter_file = open(text_file_path, "rb")
        string = chapter_file.read()
        chapter_file.close()

        return string

    def clean_text(self, text) -> str:
        decoded_text = text.decode('utf-8', 'ignore')
        cleaned_text = re.sub(r'[^\x00-\x7F]+', ' ', decoded_text)
        cleaned_text = html.unescape(cleaned_text)

        return cleaned_text

    def split_chuncks(self, text):
        lines = text.split('\n')
        chunks = []
        current_chunk = ""

        for line in lines:
            if len(current_chunk) >= const.MIN_CHUNK_SIZE:
                chunks.append(current_chunk.strip())
                current_chunk = ""

            if len(current_chunk) + len(line) <= const.MAX_CHUNK_SIZE:
                if len(current_chunk) + len(line) + 1 <= const.MAX_CHUNK_SIZE:
                    current_chunk += line + "\n"
                else:
                    chunks.append(current_chunk.strip())
                    current_chunk = line + "\n"

        if current_chunk:
            chunks.append(current_chunk.strip())

        json_file_path = os.path.join(rootdir, 'resources', 'chunks.json')

        with open(json_file_path, 'w') as json_file:
            json.dump(chunks, json_file)
