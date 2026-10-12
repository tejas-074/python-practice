class ResultTracker:
    def __init__(self):
        self.results = []

    def add(self, name, status):
        self.results.append({"name": name, "status": status})

    def count(self, status):
        return len([r for r in self.results if r["status"] == status])

    def summary(self):
        return f"{self.count('pass')} passed, {self.count('fail')} failed"

tracker = ResultTracker()
tracker.add("login", "pass")
tracker.add("logout", "pass")
tracker.add("search", "fail")

print(tracker.count("pass"))
print(tracker.count("fail"))
print(tracker.summary())