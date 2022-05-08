from vk.api_vk import VkApi
from abc import ABC


class Report(ABC):
    def __init__(self, api: VkApi):
        self.api = api

    def get_data(self, user_id: int):
        pass
