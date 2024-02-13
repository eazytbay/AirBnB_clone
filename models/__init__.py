#!/usr/bin/python3
"""This is the autoinit Module for FileStorage"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

