"""Advent of Code 2021 day 04"""

from itertools import compress, chain


class BingoCard:

    def __init__(self, numbers):
        self.number_index = dict()
        for r, row in enumerate(numbers):
            for c, number in enumerate(row):
                self.number_index[number] = (r, c)
        self.grid = numbers
        self.not_called = []
        for row in numbers:
            self.not_called.append([True for _ in row])
        self.last_number_called = None

    def call(self, number):
        self.last_number_called = number
        if number in self.number_index:
            self._mark_called(self.number_index[number])

    def _mark_called(self, element):
        r, c = element
        self.not_called[r][c] = False

    def has_won(self):
        row_win = any(sum(i) == 0 for i in self.not_called)
        column_win = any(sum(i) == 0 for i in zip(*self.not_called))
        return row_win | column_win

    def score(self):
        return self.last_number_called * sum(
            chain.from_iterable(
                compress(d, s) for d, s in zip(self.grid, self.not_called)
            )
        )

    def __repr__(self):
        return repr(self.grid)

    __str__ = __repr__


class BingoHall:

    def __init__(self, call_order, card_numbers):
        self.call_order = call_order
        self.cards = [BingoCard(numbers) for numbers in card_numbers]

    def call(self, number):
        for card in self.cards:
            card.call(number)

    def check_for_winner(self):
        """
        Return the index of the first winning card

        Returns the index of the first winning card, or None if no card wins
        """
        for index, card in enumerate(self.cards):
            if card.has_won():
                return index
        return None

    def find_first_winning_score(self):
        for number in self.call_order:
            self.call(number)
            index = self.check_for_winner()
            if index is not None:
                return self.cards[index].score()

    def find_last_winning_score(self):
        n_cards = len(self.cards)
        winlist = []
        for number in self.call_order:
            self.call(number)
            for index, card in enumerate(self.cards):
                if card.has_won() and index not in winlist:
                    winlist.append(index)
                if len(winlist) == n_cards:
                    return self.cards[index].score()


def parse_input(_fd):
    raw_lines = _fd.read().splitlines()

    call_order = list(
        map(int, raw_lines[0].split(','))
    )

    card_numbers = list()
    card = None

    for line in raw_lines[1:]:
        if line == '':
            if card is not None:
                card_numbers.append(card)
            card = list()
        else:
            card.append(
                list(map(int, line.split()))
            )

    # add the last card to the stack (if there wasn't a blank line to trigger it
    if len(card):
        card_numbers.append(card)

    return call_order, card_numbers


if __name__ == '__main__':
    with open('input.txt') as fd:
        parsed = parse_input(fd)

    bingo = BingoHall(*parsed)
    print('Part1: ', bingo.find_first_winning_score())
    print('Part2: ', bingo.find_last_winning_score())
