import argparse
from calculator.calculators import BasicCalculator


class _Calculator:
    """Represent object that perform calculation."""

    def __init__(self, parser) -> None:
        self._parser = parser
        self._calc = lambda parse_args: BasicCalculator(parse_args)

    def run(self) -> None:
        if self._parser.add:
            self._calc(self._parser.add).add()
        elif self._parser.subtract:
            self._calc(self._parser.subtract).subtract()
        elif self._parser.multiply:
            self._calc(self._parser.multiply).multiply()
        elif self._parser.divide:
            self._calc(self._parser.divide).divide()


if __name__ == '__main__':
    _parser = argparse.ArgumentParser(
        description='The program allows to perform basic options for calculator such as '
                    '`add`, `subtract`, `multiply`, `divide`, .',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    _runner_group = _parser.add_mutually_exclusive_group(required=True)
    _runner_group.add_argument('--add', '-a', nargs='*', action='store', help='Add two numbers like (5 + 5)',
                               type=int)
    _runner_group.add_argument('--subtract', '-s', nargs='*', action='store', help='Subtract two numbers like (10 - 5)',
                               type=int)
    _runner_group.add_argument('--multiply', '-m', nargs='*', action='store', help='Multiply two numbers like (5 * 5)',
                               type=int)
    _runner_group.add_argument('--divide', '-d', nargs='*', action='store', help='Divide two numbers like (10 / 5)',
                               type=int)
    args = _parser.parse_args()

    _Calculator(args).run()
