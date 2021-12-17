"""Advent of Code 2021 day 03"""

from collections import Counter


class P1Diagnostic:

    def __init__(self, _input_data):
        self.counters = None
        self._gamma = None
        self._epsilon = None

        for line in _input_data:
            if self.counters is None:
                self.counters = [
                    # explicitly initialise counts for "0" and "1" in case any
                    # columns in the input are just 1's or just 0's
                    Counter(
                        {
                            '0': 0,
                            '1': 0,
                        }
                    ) for _ in line
                ]
            for c, counter in zip(line, self.counters):
                counter.update(c)

    @property
    def gamma(self):
        if self._gamma is None:
            gamma_str = ''.join(
                [c.most_common()[0][0] for c in self.counters]
            )
            self._gamma = int(gamma_str, base=2)
        return self._gamma

    @property
    def epsilon(self):
        if self._epsilon is None:
            epsilon_str = ''.join(
                [c.most_common()[-1][0] for c in self.counters]
            )
            self._epsilon = int(epsilon_str, base=2)
        return self._epsilon

    @property
    def power_consumption(self):
        return self.gamma * self.epsilon


class P2Diagnostic:
    # symbolic constants for oxygen generator rating (OGR) and
    # co2 scrubber rating (CSR) modes.
    #
    # These values are chosen in order to be able to use as slice indices
    # in the Counter().most_common() output to pic the most/least common.
    #
    # These also act as indices into the lookup string which is used to
    # determine the digit to use int eh event of a tie

    OGR, CSR = 0, -1
    tiebreak_digit = '10'

    def __init__(self, _input_data):
        self.report = _input_data
        self._oxygen_generator_rating = None
        self._co2_scrubber_rating = None

    def filter_report_value(self, report_mode):
        filtered_report = self.report.copy()
        bits = len(filtered_report[0])  # assumption: all are the same length

        for i in range(bits):
            if len(filtered_report) == 1:
                break
            counter = Counter(
                {'0': 0, '1': 0}
            )
            counter.update([record[i] for record in filtered_report])
            most_common = counter.most_common()

            # the expression here maps 0 -> -1 and -1 -> 0
            other_report_mode = -(report_mode + 1)

            this = most_common[report_mode]
            other = most_common[other_report_mode]

            # tie-break
            if this[1] == other[1]:
                filter_digit = self.tiebreak_digit[report_mode]
            else:
                filter_digit = this[0]
            filtered_report = [
                r for r in filtered_report if r[i] == filter_digit
            ]

        assert (len(filtered_report) == 1)

        return int(filtered_report[0], base=2)

    @property
    def oxygen_generator_rating(self):
        if self._oxygen_generator_rating is None:
            # calculate here and cache in self._oxygen_generator_rating
            self._oxygen_generator_rating = self.filter_report_value(
                report_mode=self.OGR
            )
        return self._oxygen_generator_rating

    @property
    def co2_scrubber_rating(self):
        if self._co2_scrubber_rating is None:
            # calculate here and cache in self.co2_scrubber_rating
            self._co2_scrubber_rating = self.filter_report_value(
                report_mode=self.CSR
            )
        return self._co2_scrubber_rating

    @property
    def life_support_rating(self):
        return self.oxygen_generator_rating * self.co2_scrubber_rating


def parse_input(input_fd):
    return input_fd.read().splitlines()


if __name__ == '__main__':
    with open('input.txt') as fd:
        input_data = parse_input(fd)

    p1diag = P1Diagnostic(input_data)
    p2diag = P2Diagnostic(input_data)

    print('Part1: ', p1diag.power_consumption)
    print('Part2: ', p2diag.life_support_rating)
