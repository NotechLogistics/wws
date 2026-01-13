import os,sys
import json
from pathlib import Path
from src.core.card.card import Card
from src.core.player.player import Player
from src.core.card.card_processor import CardProcessor
from src.core.game_engine import GameEngine


a = GameEngine()
a.game_loop()