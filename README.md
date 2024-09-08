# Advent of Code Helper

A python tool to automatically fetch inputs, run tests and submit answer to the Advent Of Code.

## How to use this helper ?

To use this, python must be installed on your computer.  
You can the run the aoc helper by using the following prompt in a terminal.

```
python3 aoc.py [command] [arguments] -[option] [value]
```

The available commands are the following ones:
- [`set-session`](#set-session):  
    Set the session cookie for the Advent of Code site.
- [`prep`](#prep):  
    Create all the necessary files.
- [`fetch`](#fetch):  
    Create all the necessary files.
- [`init`](#init):  
    Call `prep` then `fetch`.
- [`test`](#test):  
    Run all the tests in the test file.
- [`exec`](#exec):  
    Run the tests in the test files. If they all succeed, run the program on the input, and send the answer to the Adventof Code site.
- [`copy`](#copy):  
    Copy the test file and the program of the first part into the test file and the program of the second part.
- [`fill`](#fill):  
    Copy the test file and the program of the first part into the test file and the program of the second part.

The available options are the following ones:
- `-y [year]`:  
    Set the year to the given argument. If this option is not present, use the current year.
- `-d [day]`:  
    Set the day to the given argument. If this option is not present, use the current day.
- `-l [level]`:  
    Set the level to the given argument (must be 1 or 2). If this option is not present, the level will be 1 if the `part2.py` file doesn't exist or is empty ; else it will be 2.

### set-session

`python3 aoc.py set-session [session cookie]`

You have to set the session cookie to be able to get your inputs and submit your answers to the Advent of Code.  
You can get this session cookie by inspecting the [Advent of Code](https://adventofcode.com) page while being registered. Go to the "*network*" section, then to the "*cookies*" page of the request.


### prep

`python3 aoc.py prep [-y [year]] [-d [day]]`

Create the necessary files for the specified day.

If you want to get the input immediatly, use the [init](#init) command instead.


### fetch

`python3 aoc.py fetch [-y [year]] [-d [day]]`

Fetch your input for the specified day.


### init

`python3 aoc.py init [-y [year]] [-d [day]]`

Create the necessary files for the specified day, and fetch the input from the Advent of Code site.


### test

`python3 aoc.py test [-y [year]] [-d [day]] [-l [level]]`

Run all the tests in the test file. The test file must have this format:

```
input:
[test input 1]
output:
[test output 1]

input:
[test input 2]
output:
[test output 2]

...
```

### exec

`python3 aoc.py exec [-y [year]] [-d [day]] [-l [level]]`

Run the [test](#test) command first and if all the tests are successful, it will run the program on the input file then submit the answer to (adventofcode.com)[https://adventofcode.com].


### copy

`python3 aoc.py copy [-y [year]] [-d [day]]`

Copy the test file and program file for part 1 to the test file and program file for part 2. If thoses files aren't empty, a backup file will be created.


### fill

`python3 aoc.py fill [template_file] [-y [year]] [-d [day]]`

Copy the template file to the program file for part 1. If this files isn't empty, a backup file will be created.  
By default, the template file will be *templates/template.py*.


## TODO

- Automatically fetch tests in the aoc problem page
- Organize the code into more files
- Better argument gestion
- Add simple exemple usage
