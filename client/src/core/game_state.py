'''
Author: NotechLogistics chenkai.32301@foxmail.com
Date: 2025-12-25 19:01:25
LastEditors: NotechLogistics chenkai.32301@foxmail.com
LastEditTime: 2026-01-13 11:15:04
FilePath: \game4.0\client\src\core\game_state.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class GameState:
    def __init__(self):
        self.player = None
        self.players = {}
        self.current_player = None 



    @property
    def is_game_over(self):
        return False