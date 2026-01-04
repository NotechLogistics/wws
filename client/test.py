import os,sys
import json
from pathlib import Path
from src.core.card.card import Card
from src.core.player.player import Player
from src.core.card.card_processor import CardProcessor

def pr(card_processor:CardProcessor):
    print("\nDeck:")
    [print(card,end="  |  ") for card in card_processor.get_deck()]
    print("\nDiscard deck:")
    [print(card,end="  |  ") for card in card_processor.get_discard_deck()]

card_processor = CardProcessor()
card_processor.init_deck(num =10)
print("---- After init ----")
pr(card_processor)

print("---- After draw ----")
hand_cards = card_processor.draw_card(num=5)
print("Hand cards:")
[print(card,end="  |  ") for card in hand_cards]
pr(card_processor)

for i in range(3):
    display_cards = hand_cards.pop()
    card_processor.discard_card(display_cards)
print("---- After discard ----")
print("hand cards:")
[print(card,end="  |  ") for card in hand_cards]
pr(card_processor)
print()
print("---- After shuffle ----")
[print(card,end="  |  ") for card in card_processor.draw_card(num=7)]
