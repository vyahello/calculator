# Calculator

## Basic calculator operations
- `calculator.py` tool allows to perform simple operations as `add`, `subtract`, `multiply` and `divide` arbitrary amount of input numbers. 

## Demo
```bash
~/calculator python calculator.py --multiply 5.5 2.5 10
2018-06-11 12:14:20,171 Performing multiply operation
2018-06-11 12:14:20,171 Result equals to 137.5
~/calculator python calculator.py --add 5.5 2.5 10
2018-06-11 12:15:16,079 Performing add operation
2018-06-11 12:15:16,079 Result equals to 18.0
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