# Calculator
If reflects simple cli calculator program that can operate `add`, `subtract`, `multiply` and `divide` options. I uses pure OOP style. Nothing more, have a fun :)

## Usage
Please use `calculator.py` tool to perform simple computation operations:
```bash
~ python calculator.py --multiply 5.5 2.5 10
2018-06-11 12:14:20,171 Performing multiply operation
2018-06-11 12:14:20,171 Result equals to 137.5
~ python calculator.py --add 5.5 2.5 10
2018-06-11 12:15:16,079 Performing add operation
2018-06-11 12:15:16,079 Result equals to 18.0
```

### Run unittests
Run `pytest -v` from shell in the root directory of the repository.

## Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all require python packages
