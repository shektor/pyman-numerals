# Roman Numerals

A function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

## Getting Started

Clone the repository.
```bash
> git clone git@github.com:shektor/pyman-numerals.git
> cd pyman-numerals
```

Create a virtual environment.
```bash
> python3 -m venv env
> . env/bin/activate
```

Install required python packages.
```bash
> pip install -r requirements.txt
```

## Running Tests

```bash
> pytest
```

## Usage

```bash
# from /pyman-numerals
> python3

>>> from roman_numeral import convert
>>> convert(9)
IX
>>> convert(3518)
MMMDXVIII
```

## Closing

Leave the virtual environment.
```bash
> deactivate
```
