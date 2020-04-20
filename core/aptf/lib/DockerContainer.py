from DockerClient import DockerClient

class DockerContainer(DockerClient):

    def __init__(self, image_name):
        self.__image_name = image_name
        self.__container = None
        self.exec_result = list()


    def __enter__(self):
        self.__container = self._client.containers.create(self.__image_name, tty=True,detach=True,privileged=False)
        self.__container.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__container.stop()
        self.__container.remove()
        if exc_val:
            raise

    def exec(self, cmd):
        result = self.__container.exec_run(cmd, demux=True, stream=False, detach=False)
        stdout, stderr = result.output
        return tuple(result)

    def start(self):
        self.__container.start()

    def stop(self):
        self.__container.stop()

    def remove(self):
        self.__container.remove()

    def commit(self):
        commit_n = self.__container.commit()
        return commit_n


    def create(self, image):
        pass
