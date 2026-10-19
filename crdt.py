class Counter:
    """Warm-up CRDT: G-Counter. Har replica sirf apna count badhata hai."""

    def __init__(self, replica_id):
        self.replica_id = replica_id
        self.counts = {}  # {replica_id: count}

    def increment(self):
        self.counts[self.replica_id] = self.counts.get(self.replica_id, 0) + 1

    def value(self):
        return sum(self.counts.values())

    def merge(self, other):
        for rid, c in other.counts.items():
            self.counts[rid] = max(self.counts.get(rid, 0), c)