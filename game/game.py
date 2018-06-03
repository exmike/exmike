class Hand:
    def __init__(self, name):
        # имя игрока
        self.name = name
        # Изначально рука пустая
        self.cards = []

    def add_card(self, card):
        """ Добавляет карту на руку """
        self.cards.append(card)

    def get_value(self):
        """ Метод получения числа очков на руке """
        result = 0
        # Количество тузов на руке.
        aces = 0
        for card in self.cards:
            result += card.card_value()
            # Если на руке есть туз - увеличиваем количество тузов
            if card.get_rank() == "A":
                aces += 1
        # Решаем считать тузы за 1 очко или за 11
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = "%s 's contains:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nHand value: " + str(self.get_value())
        return text

class Deck:
    def __init__(self):  # метод __init__ используется для автоматического присвоения аттрибутов при вызове класса
        import random
        ranks = "23456789TJQKA"
        suits = "КПЧБ"
        self.cards = [Card(r, s) for r in ranks for s in suits] # генератор списков создающий колоду из 52 карт
        random.shuffle(self.cards)  # перетасовываем колоду в стек

    def deal_card(self):
        """ Функция сдачи карты """
        return self.cards.pop()

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        """ Возращает количество очков которое дает карта """

        if self.rank in "TJQK":
            return 10
        else:
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)



def new_game():
    # создаем колоду
    d = Deck()
    # задаем "руки" для игрока и дилера
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    # сдаем две карты игроку
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    # сдаем одну карту дилеру
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print("=" * 20)
    print(player_hand)
    # Флаг проверки необходимости продолжать игру
    in_game = True
    # набирать карты игроку имеет смысл только если у него на руке меньше 21 очка
    while player_hand.get_value() < 21:
        ans = input('Брать ещё ? (y/n) ')
        if ans == "n":
            print("Вы выбрали стоп!")
            break
        else:
            player_hand.add_card(d.deal_card())
            print(player_hand)
            # Если у игрока перебор - дилеру нет смысла набирать карты
            if player_hand.get_value() > 21:
                print("Вы проиграли!")
                ans = input('Будете играть ещё ?(y/n) ')
                if ans == "n":
                    print("Всего доброго!!")
                    exit(0)
                else:
                    new_game()
                in_game = False
    print("=" * 20)
    if in_game:
        # По правилам дилер обязан набирать карты пока его счет меньше 17
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            # Если у дилера перебор играть дальше нет смысла - игрок выиграл
            if dealer_hand.get_value() > 21:
                print("Раздающий проиграл")
                ans = input('Будете играть ещё ?(y/n) ')
                if ans == "n":
                    print("Всего доброго!!")
                    exit(0)
                else:
                    new_game()
                in_game = False
    if in_game:
        # Ни у кого не было перебора - сравниваем количество очков у игрока и дилера.
        # В нашей версии если у дилера и игрока равное количество очков - выигрывает казино
        if player_hand.get_value() > dealer_hand.get_value():
            print("Вы выиграли!")
            ans = input('Будете играть ещё ?(y/n) ')
            if ans == "n":
                print("Всего доброго!!")
                exit(0)
            else:
                new_game()
        else:
            print("Раздающий выиграл!")
            ans = input('Будете играть ещё ?(y/n) ')
            if ans == "n":
                print("Всего доброго!")
                exit(0)
            else:
                new_game()


new_game()
