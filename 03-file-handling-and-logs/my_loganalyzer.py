import json
def read_file(path):
    try:
        with open(path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return []

def count_levels(lines, levels):
    count = {level: 0 for level in levels}
   
    for line in lines:
        tokens = set(line.split())
        for level in levels:
            if level in tokens:
                count[level] += 1
    return count

def output_summary(summary):
    print("Log Summary:")
    print(summary)
    with open(output_file, "w") as json_file:
        json.dump(summary, json_file, indent=4)

levels = ["INFO", "WARNING", "ERROR"]
path = input("Enter the path to the log file: ")
output_file = input("Enter the path to the output JSON file: ")
lines = read_file(path)
summary = count_levels(lines, levels)
output_summary(summary)