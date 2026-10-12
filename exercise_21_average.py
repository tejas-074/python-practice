import csv

def load_duration(path):
    durations = []
    with open(path, newline='') as file:
        for row in csv.DictReader(file):
            durations.append(float(row["duration"]))
        return durations
        
durations = load_duration("results.csv")
average = sum(durations) / len(durations)

print(len(durations))
print(round(average, 2))
print(max(durations))