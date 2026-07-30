import json
levels = ["INFO", "WARNING", "ERROR", "UNKNOWN"]
class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.count = {level: 0 for level in levels}
    
    def read_file(self):
        try:
            with open(self.log_file, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print("File not found.")
            return []

    def count_levels(self, lines):
        for line in lines:
            tokens = set(line.split())
            for level in self.count:
                if level in tokens:
                    self.count[level] += 1
        return self.count

    def output_summary(self, output_file="log_summary.json"):
        with open(output_file, "w") as json_file:
            json.dump(self.count, json_file, indent=4)

def main():
    log_file = "app.log"
    analyzer = LogAnalyzer(log_file) 

    lines = analyzer.read_file()
    if not lines:
        print("No logs to analyze.")
        return

    result = analyzer.count_levels(lines)

    for level, count in result.items():
        print(f"{level:10}: {count}")
        
    analyzer.output_summary()


if __name__ == "__main__":
    main()
