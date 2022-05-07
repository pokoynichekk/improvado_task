from vk.api_wrapper import VkApiWrapper
from abc import ABC


class Report(ABC):
    def __init__(self, api: VkApiWrapper):
        self.api = api

    def get_data(self, user_id: int):
        pass
