# -*- coding: utf-8 -*-

__all__ = ['AptRepository']
__version__ = '0.1'
__docformat__ = 'restructuredtext'


from os import path as os_path
from os import makedirs, listdir
from flask import Flask, abort, jsonify, send_from_directory

from multiprocessing import Process


class AptRepository(Flask):

    def __init__(self, root_dir, **kwargs):
        super(AptRepository, self).__init__(__name__, **kwargs)
        self.root_dir = root_dir
        self.add_route("/<path:path>")
        self.server= None

    def add_route(self, rule):
        self.add_url_rule(rule, view_func=self.list_files)

    def list_files(self, path):
        files = []
        realpath = os_path.join(self.root_dir, path)
        if os_path.exists(realpath):
            if os_path.isfile(realpath):
                return send_from_directory(self.root_dir, path, as_attachment=True)
            if os_path.isdir(realpath):
                for filename in listdir(realpath):
                    files.append(filename)
        else:
            abort(404)
        return jsonify(files)

    def start_repository(self, **arguments):
        self.server = Process(target=self.run, kwargs=arguments)
        self.server.start()

    def stop_repository(self):
        self.server.terminate()
        self.server.join()
