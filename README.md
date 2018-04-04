# Calculator

## Basic calculator operations
- `calculator.py` tool allows to perform simple operations as `add`, `subtract`, `multiply` and `divide` arbitrary amount of input numbers. 
```
~ python calculator.py -h
usage: calculator.py [-h]
                     (--add [ADD [ADD ...]] | --subtract [SUBTRACT [SUBTRACT ...]] | --multiply [MULTIPLY [MULTIPLY ...]] | --divide [DIVIDE [DIVIDE ...]])

The program allows to perform basic options for calculator such as `add`,
`subtract`, `multiply`, `divide`, .

optional arguments:
  -h, --help            show this help message and exit
  --add [ADD [ADD ...]], -a [ADD [ADD ...]]
                        Add two numbers like (5 + 5) (default: None)
  --subtract [SUBTRACT [SUBTRACT ...]], -s [SUBTRACT [SUBTRACT ...]]
                        Subtract two numbers like (10 - 5) (default: None)
  --multiply [MULTIPLY [MULTIPLY ...]], -m [MULTIPLY [MULTIPLY ...]]
                        Multiply two numbers like (5 * 5) (default: None)
  --divide [DIVIDE [DIVIDE ...]], -d [DIVIDE [DIVIDE ...]]
                        Divide two numbers like (10 / 5) (default: None)
```
## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vjagello93@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all require python packages

### Run unittests
Run `pytest -v` from shell in the root directory of the repository.