import sys
import os
import shutil
from datetime import date
import requests
from aocHtmlParser import AocHtmlParser


#####################
# Environment setup #
#####################

def load_environment(file_path: str) -> dict:
    # If there is no .env file, the environment is empty
    if not os.path.isfile(file_path):
        return {}

    res = {}
    with open(file_path) as f:
        for line in f:
            if line.startswith("#"):
                continue
            split_pos = line.index('=')
            res[line[:split_pos].strip()] = line[split_pos+1:].strip()
    return res

def update_environment(file_path: str, variable: str, value: str) -> None:

    # If there is no .env file, create on
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as f:
            f.write(f"#.env\n{variable}={value}")
        return

    temp_path = ".env.temp"
    with open(file_path) as fs, open(temp_path, 'w') as fd:
        seen = False
        for line in fs:
            if line.startswith('#'):
                fd.write(line)
                continue
            split_pos = line.index('=')
            if line[:split_pos].strip() == variable:
                seen = True
                fd.write(variable + "=" + value + '\n')
                continue
            fd.write(line)
        if not seen:
            fd.write(variable + "=" + value + '\n')
    shutil.copyfile(temp_path, file_path)
    os.remove(temp_path)

env_path = ".env"
environ = load_environment(env_path)



######################
# parameters gestion #
######################

# Creation of the options and parameters objects
options = {}
parameters = []
command = None

nb_param = len(sys.argv)
i = 1
# Get the command if it exists
if nb_param > 1 and sys.argv[1][0] != '-':
    command = sys.argv[1]
    i = 2

# Get parameters
while i < nb_param:
    if sys.argv[i][0] == '-':
        if i+1 == nb_param:
            raise Error("An option should have a following parameter.")
        options[sys.argv[i]] = sys.argv[i+1]
        i += 2
    else:
        parameters.append(sys.argv[i])
        i += 1


# Get wanted dates
today = date.today()
year = today.year
day = today.day

# Check year and day options
if "-d" in options:
    is_error = False
    try:
        day = int(options["-d"])
    except ValueError:
        is_error = True
    if is_error or day <= 0 or day > 31:
        print("Error in argument: the day option should be an integer between 1 and 31.", file=sys.stderr)
        exit(1)

if "-y" in options:
    is_error = False
    try:
        year = int(options["-y"])
    except ValueError:
        is_error = True
    if is_error or year < 2015 or year > today.year:
        print("Error in argument: the year option should be an integer bigger than 2015.", file=sys.stderr)
        exit(1)

# Set the correct paths
year_path = os.path.join(".", str(year))
day_path = os.path.join(year_path, ("0" if day < 10 else "") + str(day))
input_path = os.path.join(day_path, "input.txt")
part1_path = os.path.join(day_path, "part1.py")
part2_path = os.path.join(day_path, "part2.py")
test1_path = os.path.join(day_path, "test1.txt")
test2_path = os.path.join(day_path, "test2.txt")



#############
# Functions #
#############

def is_file_empty(file_path: str) -> bool:
    return (not os.path.isfile(part2_path)) or os.path.getsize(part2_path) == 0

def prep():
    """Prepare the files for the wanted day."""
    if not os.path.isdir(year_path):
        os.makedirs(year_path)
    if not os.path.isdir(day_path):
        os.makedirs(day_path)
    if not os.path.isfile(input_path):
        open(input_path, 'a').close()
    if not os.path.isfile(part1_path):
        open(part1_path, 'a').close()
    if not os.path.isfile(part2_path):
        open(part2_path, 'a').close()
    if not os.path.isfile(test_path):
        open(test_path, 'a').close()

def init():
    """Fetch the input from Advent Of Code site."""
    input_url = "https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input"
    r = requests.get(input_url, cookies={"session": environ["SESSION"]})
    with open(input_path, "w") as f:
        f.write(r.text)


def test(level: int) -> bool:
    """Run all the tests present in the test file."""
    # Get the right paths
    part_path = part1_path if level == 1 else part2_path
    test_path = test1_path if level == 1 else test2_path

    # create a list of inputs
    inputs = []
    with open(test_path) as test_file:
        for test_case in test_file.read().strip().split('\n\n'):
            inp, out = test_case.split("\noutput:\n")
            assert(inp.startswith("input:\n"))
            inp = inp[7:].strip()
            out = out.strip()
            inputs.append([inp, out])
    
    # Run all the tests
    res = True
    i = 0
    for inp, out in inputs:
        i += 1
        with open("input.temp", "w") as input_file:
            input_file.write(inp)

        # call the program, and manage the return status
        status = os.system(f"python3 {part_path} < input.temp > output.temp 2> output.temp")
        if not (os.WIFEXITED(status) and (os.WEXITSTATUS(status)==0)):
            with open("output.temp") as output_file:
                print(f"ERROR while in test {i}:\n\n{output_file.read().strip()}")
            os.remove("input.temp")
            os.remove("output.temp")
            return False

        # Get and check the answer
        response = ""
        with open("output.temp") as output_file:
            response = output_file.read().strip()
        if response == out:
            print(f"Test {i}: SUCCES")
        else:
            res = False
            print(f"Test {i}: FAILED")
            print(f"Expected value:\n{out}")
            print(f"Response gotten:\n{response}")
    os.remove("input.temp")
    os.remove("output.temp")
    return res


def execute(level: int):
    """Run the program with the input, and submit the answer."""

    # Run the right program, and get the answer
    part_path = part1_path if level == 1 else part2_path
    os.system(f"python3 {part_path} < {input_path} > output.temp")
    answer = ""
    with open("output.temp") as output_file:
        answer = output_file.read().strip()
    os.remove("output.temp")

    # Submit the answer to the advent of code site
    print(f"Answer {answer} will be send to adventofcode.com")
    submit_url = "https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/answer"
    r = requests.post(submit_url,
                      cookies={"session": environ["SESSION"]},
                      data={"level":str(level), "answer":str(answer)})
    if (r.status_code != 200):
        print(f"The submission request came back with the code {r.status_code}.")
        return
    
    parser = AocHtmlParser()
    parser.feed(r.text)
    print(parser.message) 



def copy():
    """Copy the first part file in the second part file.
    If needed, a backup of the second part will be made.
    """
    # the first part must exist
    if not os.path.isfile(part1_path):
        raise ValueError("The first part file doesn't exist.")

    # Create backup if needed
    if not is_file_empty(part2_path):
        shutil.copyfile(part2_path, os.path.join(day_path, "part2_backup.py"))
    if not is_file_empty(test2_path):
        shutil.copyfile(test2_path, os.path.join(day_path, "test2_backup.txt"))
    
    # Copy the files
    shutil.copyfile(part1_path, part2_path)
    if os.path.isfile(test1_path):
        shutil.copyfile(test1_path, test2_path)



def set_session():
    if len(parameters) == 0:
        raise ValueError("Please add a session cookie.")
    environ["SESSION"] = parameters[0]
    update_environment(env_path, "SESSION", parameters[0])



##################
# Commands logic #
##################

if command == "prep":
    prep()
elif command == "init":
    prep()
    init()
elif command == "test":
    level = 1
    if not is_file_empty(part2_path):
        level = 2
    test(level)
elif command == "exec":
    level = 1
    if not is_file_empty(part2_path):
        level = 2
    if test(level):
        execute(level)
elif command == "copy":
    copy()
elif command == "fill":
    fill()
elif command == "set-session":
    set_session()
else:
    raise ValueError("Unknown command.")