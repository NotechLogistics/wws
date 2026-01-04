from pathlib import Path #  用于处理文件路径
current_file_dir = Path(__file__).parent.parent.parent.parent.resolve() #  获取项目根目录的路径
from src.core.general.general import General
class Player:
    """玩家基类，定义了玩家的基本属性和行为"""
    
    def __init__(self, name):
        """
        初始化玩家
        Args:
            name (str): 玩家名称
        """
        self.name = name
        self.hand = []  # 手牌列表
        self.general = None  # 玩家所使用的武将
    
    @property
    def max_health(self):
        """返回玩家武将的最大生命值"""
        return self.general.max_health if self.general else 0
    @property
    def health(self):
        """返回玩家武将的当前生命值"""
        return self.general.health if self.general else 0
    def set_general(self, general_name):
        """
        设置玩家所使用的武将
        Args:
            general_name (str): 武将名称
        """
        self.general = General(general_name)

    def draw_card(self, card):
        """
        抽牌
        Args:
            card: 要加入手牌的卡牌
        """
        self.hand.append(card)
        
    def play_card(self, card_index):
        """
        出牌
        Args:
            card_index (int): 要出的牌在手牌中的索引
        Returns:
            card: 打出的牌，如果索引无效返回None
        """
        if 0 <= card_index < len(self.hand):
            return self.hand.pop(card_index)
        return None
        
    def take_damage(self, damage):
        """
        受到伤害
        Args:
            damage (int): 受到的伤害值
        """
        self.general.take_damage(damage)
        
    def heal(self, amount):
        """
        恢复生命值
        Args:
            amount (int): 恢复的生命值
        """
        self.general.heal(amount)
        
    def is_alive(self):
        """
        检查玩家是否存活
        Returns:
            bool: 玩家是否存活
        """
        return self.health > 0
        
    def __str__(self):
        """
        返回玩家的字符串表示
        Returns:
            str: 玩家信息
        """
        return f"Player {self.name}: General {self.general.name if self.general else 'None'},health: {self.health}/{self.max_health} , Cards in hand: {len(self.hand)}"

