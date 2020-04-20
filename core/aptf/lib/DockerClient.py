from docker import client, errors


class DockerClient(object):

    _client = client.from_env()

    def stop_all_running_containers(self):
        for container in self._client.containers.list():
            container.stop()

    def list_all_images(self):
        images = list()
        for image in self._client.images.list(all=True):
            images.extend(image.tags)
        return images

    def get_image(self, name):
        try:
            self._client.images.get(name)
        except errors.ImageNotFound:
            pass
        except errors.APIError:
            pass

    def remove_image(self, image_id):
        self._client.images.remove(image_id, force=True)
