from .card import Card

class CardProcessor:
    def __init__(self):

        """
        初始化方法，用于创建类的实例
        初始化两个列表：_deck 和 _discard_deck
        """
        self._deck = []  # 存放牌堆的列表，初始为空
        self._discard_deck = []  # 存放弃牌堆的列表，初始为空
    def init_deck(self, num=1, card_names=["sha","shan","tao","jiu"]):
        """根据提供的卡牌名称列表初始化牌堆"""
        from random import choice
        self._deck = [Card(choice(card_names)) for _ in range(num)]

    def draw_card(self, num=1):
        """从牌堆顶摸牌"""
        drawn_cards = []
        for _ in range(num):
            if not self._deck:
                self.shuffle_deck()
            drawn_cards.append(self._getTheNextCard())
        return drawn_cards
    
    def _lookTheNextCard(self):
        """查看牌堆顶的num张牌"""
        return self._deck[0]
    
    def _getTheNextCard(self):
        """获取牌堆顶的num张牌"""
        if not self._deck:
            self.shuffle_deck()
        return self._deck.pop(0)

    def shuffle_deck(self):
        """洗牌，将弃牌堆重新洗入牌堆"""
        from random import shuffle
        self._deck.extend(self._discard_deck)
        self._discard_deck.clear()
        shuffle(self._deck)
    

    def discard_card(self, card: Card):
        """将卡牌放入弃牌堆"""
        self._discard_deck.append(card)
    
    def get_deck(self):
        """获取牌堆"""
        return self._deck
    
    def get_discard_deck(self):
        """获取弃牌堆"""
        return self._discard_deck