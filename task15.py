from  random import shuffle     # метод shuffle смешивает список в случайном порядке
class Card:
    def __init__(self):
        pass

class Deck_of_Cards(Card):
    """ тут создаётся колода карт """
    def __init__(self):
        Card.__init__(self)
        self.all_cards = []
        for i in range(2, 11):
            x = str(i) + 'c'
            self.all_cards.append(x)
            x = str(i) + 'b'
            self.all_cards.append(x)
            x = str(i) + 't'
            self.all_cards.append(x)
            x = str(i) + 'p'
            self.all_cards.append(x)
        for i in ['A', 'K', 'Q', 'J']:
            x = str(i) + 'c'
            self.all_cards.append(x)
            x = str(i) + 'b'
            self.all_cards.append(x)
            x = str(i) + 't'
            self.all_cards.append(x)
            x = str(i) + 'p'
            self.all_cards.append(x)
    """ раздает карты (в колоде убирает эти карты) """
    def deal(self, *x):
        if x[0]:
            print(self.all_cards[x[0]-1])
            del self.all_cards[x[0]-1]
    """ смешивает карты и показывает """
    def mix(self):
        shuffle(self.all_cards)
        list(map(lambda x: print(x, end=" "), self.all_cards))
        print(f"\nв колоде {len(self.all_cards)}")

go = Deck_of_Cards()
go.deal(1)
go.mix()
