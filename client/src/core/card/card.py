import json #  用于处理JSON数据
import os #  用于处理操作系统相关的功能
from pathlib import Path #  用于处理文件路径
from random import choice #  用于随机选择
current_file_dir = Path(__file__).parent.parent.parent.parent.resolve() #  获取项目根目录的路径
class Card:
    _cards_data = None #  存储卡片数据的类变量
    _id_mapping = None #  存储ID映射的类变量

    @classmethod
    def _load_data(cls):
        if cls._cards_data is None:
            with open(current_file_dir / "data/card/id.json", "r", encoding="utf-8") as f: #  加载ID映射文件
                cls._id_mapping = json.load(f)
            with open(current_file_dir / "data/card/attribute.json", "r", encoding="utf-8") as f: #  加载卡片属性文件
                cls._cards_data = json.load(f)

    def __init__(self, name, point=None, suit=None):
        self._load_data()
        self._id = self._id_mapping[name] #  从ID映射中获取卡牌的ID
        self.name = self._cards_data[self._id]["name"] #  从卡牌数据中获取卡牌名称
        self.point = point if point is not None else choice(self._cards_data[self._id]["point_range"]) #  设置卡牌的点数，如果未提供则使用默认值
        self.suit = suit if suit is not None else choice(self._cards_data[self._id]["suit_range"]) #  设置卡牌的花色，如果未提供则使用默认值

        # 卡牌ui，待开发
        self.ui=None

    @property
    def attributes(self):
        return self._cards_data[self._id] #  返回卡牌的所有属性数据

    def __str__(self):
        return f"{self.name} {self.point} {self.suit}"
