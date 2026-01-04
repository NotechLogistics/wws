class GameEngine:
    """三国杀核心引擎"""
    
    def __init__(self):
        # 1. 游戏状态管理
        self.state = GameState()
        
        # 2. 卡牌处理器
        self.card_processor = CardProcessor()
        
        # 3. 技能处理器
        self.skill_processor = SkillProcessor()
        
        # 4. 规则检查器
        self.rule_checker = RuleChecker()
    
    def game_loop(self):
        """主游戏循环"""
        while not self.state.is_game_over():
            current_player = self.state.current_player
            
            # 回合开始阶段
            self.phase_start()
            
            # 判定阶段（如果有）
            self.phase_judge()
            
            # 摸牌阶段
            self.phase_draw()
            
            # 出牌阶段（核心！）
            self.phase_play()
            
            # 弃牌阶段
            self.phase_discard()
            
            # 回合结束阶段
            self.phase_end()
            
            # 切换到下个玩家
            self.state.next_player()
