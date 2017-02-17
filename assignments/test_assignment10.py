from assignment10 import getWordScore, Hand, Player, ComputerPlayer, Wordlist


class TestHand:
    def setup(self):
        self.handSize = 8

        self.hand1 = {'a': 3, 'b': 2, 'd': 3}
        self.h1 = Hand(self.handSize, self.hand1)

        self.hand2 = {'h': 2, 'e': 3, 'l': 4, 'o': 2}
        self.h2 = Hand(self.handSize, self.hand2)

    def test_update(self):
        self.h1.update('bad')
        self.h2.update('hello')

        assert self.hand1 == {'a': 2, 'b': 1, 'd': 2}
        assert self.hand2 == {'h': 1, 'e': 2, 'l': 2, 'o': 1}

    def test_containsLetters(self):
        self.h1.update('bad')
        self.h2.update('hello')

        assert self.h1.containsLetters('abd') is True
        assert self.h2.containsLetters('hello') is True
        assert self.h1.containsLetters('aaabbddd') is False
        assert self.h2.containsLetters('hheelloo') is False

    def test_isEmpty(self):
        assert self.h1.isEmpty() is False
        assert self.h2.isEmpty() is False

        self.h1.update('bad')
        self.h1.update('dad')
        self.h1.update('ab')

        assert self.h1.isEmpty() is True

    def test_eq(self):
        assert (self.h1 == self.h2) is False
        assert (self.h2 == self.h1) is False

    def test_str(self):
        assert str(self.h1) == "a a a b b d d d"
        assert str(self.h2) == "h h e e e l l l l o o"

        self.h1.update('bad')
        self.h2.update('hello')

        assert str(self.h1) == "a a b d d"
        assert str(self.h2) == "h e e l l o"


class TestPlayer:
    def setup(self):
        self.hand1 = Hand(6, {'c': 1, 'a': 1, 'd': 1, 'o': 1, 'e': 1})
        self.hand2 = Hand(8, {'a': 2, 'b': 1, 'd': 2})

        self.p1 = Player(1, self.hand1)
        self.p2 = Player(2, self.hand2)

    def test_getHand(self):
        assert self.p1.getHand() == self.p1.hand
        assert self.p2.getHand() == self.p2.hand

    def test_addPoints(self):
        self.p1.addPoints(5.)
        self.p1.addPoints(12.)
        self.p2.addPoints(6)

        assert self.p1.getPoints() == 17.
        assert self.p2.getPoints() == 6.

    def test_getPoints(self):
        self.p1.addPoints(5.)
        self.p1.addPoints(12.)
        self.p2.addPoints(20.1)

        assert self.p1.getPoints() == float(17)
        assert self.p2.getPoints() == float(20.1)

    def test_getIdNum(self):
        assert self.p1.getIdNum() == 1
        assert self.p2.getIdNum() == 2

    def test_cmp(self):
        pass


class TestComputerPlayer:
    def setup(self):
        self.wordlist = Wordlist().getList()
        self.p = ComputerPlayer(1, Hand(6, {'c': 1, 'a': 1, 'b': 1,
                                            'd': 1, 'o': 1, 'e': 1}))

    def test_pickBestWord(self):
        assert self.p.pickBestWord(self.wordlist) == ('abode')
