import os

from os import path as os_path
from os import makedirs, listdir

from flask import Flask, abort, jsonify, send_from_directory


UPLOAD_DIRECTORY = "/home/domelchuk/project/api_uploaded_files"

if not os_path.exists(UPLOAD_DIRECTORY):
    makedirs(UPLOAD_DIRECTORY)


api = Flask(__name__)

@api.route("/<path:path>")
def list_files(path):
    files = []
    realpath = os_path.join(UPLOAD_DIRECTORY, path)
    if os_path.exists(realpath):
        if os_path.isfile(realpath):
            return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)
        if os_path.isdir(realpath):
            for filename in listdir(realpath):
                files.append(filename)
    else:
        abort(404)
    return jsonify(files)
