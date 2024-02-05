from random import choice

#1.
print("Добро пожаловать в игру 'Красное или черное'!")

#2.
print("Я загадаю карту, а ты попробуй угадать цвет")

#3.
CARD_NUMBER = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "В", "Д", "К", "Т"]
CARD_SUIT = ["Ч", "Б", "П", "К"]
random_card_number = choice(CARD_NUMBER)
random_card_suit = choice(CARD_SUIT)

#4. 5.
player_answer = input("Угадайте цвет масти карты: Красная или черная? \n")

#6.
if player_answer == "Красная" and random_card_suit in ["Ч", "Б"]:
  print("Правильно! Загаданная карта была:", random_card_number, random_card_suit)
elif player_answer == "черная" and random_card_suit in ["П", "К"]:
  print("Правильно! Загаданная карта была:", random_card_number, random_card_suit)
else:
  print("Не правильно! Загаданная карта была:", random_card_number, random_card_suit)