import json
import os
from pathlib import Path
current_file_dir = Path(__file__).parent.parent.parent.parent.resolve()  #  获取当前文件所在项目的根目录路径
class General:
    _general_data = None  #  类变量，用于存储加载的通用数据
    _id_mapping = None  #  类变量，用于存储ID映射关系

    @classmethod
    def _load_data(cls):
        if cls._general_data is None:
            with open(current_file_dir / "data/general/id.json", "r", encoding="utf-8") as f:  #  加载ID映射的JSON文件
                cls._id_mapping = json.load(f)
            with open(current_file_dir / "data/general/data.json", "r", encoding="utf-8") as f:  #  加载通用数据的JSON文件
                cls._general_data = json.load(f)

    def __init__(self, name):
        self._load_data()
        self._id = self._id_mapping[name]  #  从名称映射中获取ID并赋值给实例变量_id
        self.name = self._general_data[self._id]["name"]  #  根据ID从通用数据中获取名称并赋值给实例变量name
        self.health = self._general_data[self._id]["health"]  #  根据ID从通用数据中获取生命值并赋值给实例变量health
        self.max_health = self._general_data[self._id]["maxHealth"]  #  根据ID从通用数据中获取最大生命值并赋值给实例变量max_health

        
        self.ui=None

    @property
    def attributes(self):
        return self._cards_data[self._id] 

    def __str__(self):
        return f"{self.name} {self.health} {self.max_health}"
    
    def cause_harm(self, damage):
        self.health -= damage
    
    def restore_health(self, amount):
        self.health = min(self.max_health, self.health + amount)
    
    def hurt(self, damage):
        self.health -= damage
