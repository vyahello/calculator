import argparse

from calculator.calculations import BasicCalculation

if __name__ == '__main__':
    _parser = argparse.ArgumentParser(
        description='The program allows to perform basic options for calculator such as '
                    '`add`, `subtract`, `multiply`, `divide`, .',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    _runner_group = _parser.add_mutually_exclusive_group(required=True)
    _runner_group.add_argument('--add', '-a', nargs='*', action='store', help='Add two numbers like (5 + 5)',
                               type=float)
    _runner_group.add_argument('--subtract', '-s', nargs='*', action='store', help='Subtract two numbers like (10 - 5)',
                               type=float)
    _runner_group.add_argument('--multiply', '-m', nargs='*', action='store', help='Multiply two numbers like (5 * 5)',
                               type=float)
    _runner_group.add_argument('--divide', '-d', nargs='*', action='store', help='Divide two numbers like (10 / 5)',
                               type=float)
    args = _parser.parse_args()

    BasicCalculation(args).start()
