# Do You Even File Searcher

## Overview
Small utility to search a local system for a particular string.

# Prerequisites
- [pyenv](https://github.com/pyenv/pyenv#installation)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv#installation)

# First Time Setup
```
pyenv install 3.8.2
pyenv virtualenv 3.8.2 file-searcher
pyenv activate file-searcher
```

# Run Arguments
The utility takes required command line arguments.

`-p | -path` - is the file path used for a recursive search

`-t | -target` - is the target text to search for


# Running the Utility
To run the utility execute `python file_searcher.py -p  -t` with the values for `-p` and `-t`

For example
`python file_searcher.py -p ~/Documents -t "foo"`    




