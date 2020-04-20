

from aptf.lib.AptRepository import AptRepository
from aptf.lib.DockerContainer import DockerContainer

#import requests

class TestClass:

    @classmethod
    def setup_class(cls):
        cls.apt = AptRepository('/home/domelchuk/project/api_uploaded_files')
        cls.apt.start_repository(debug=False, host='0.0.0.0', port=8000)

    @classmethod
    def teardown_class(cls):
        cls.apt.stop_repository()
        print('setup_class')

    def test_request(self):
        commands = [
            ['sh', '-c', 'echo "deb [arch=amd64] http://192.168.1.243:8000/ubuntu stable main" > /etc/apt/sources.list.d/apttest.list'],
            ['cat', '/etc/apt/sources.list.d/apttest.list'],
            ['apt-get', 'update'],
            ['apt-get', 'install', 'sudo']
        ]

        with DockerContainer('ubuntu') as cnt:
            for cmd in commands:
                res = cnt.exec(cmd)
                print(res)
        # r = requests.get('http://0.0.0.0:8000/ubuntu/dists/stable/InRelease')
        # assert r.status_code==200

