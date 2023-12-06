class LRUCache:
    def __init__(self, limit=100):
        self.cache = {}
        self.len = 0
        self.limit = limit

    def get(self, key):
        if key in self.cache:
            self.cache[key] = self.cache.pop(key)
        return self.cache.get(key)

    def set(self, key, value):
        if self.len < self.limit:
            if key in self.cache:
                self.cache.pop(key)
                self.cache[key] = value
            else:
                self.len += 1
                self.cache[key] = value
        else:
            if key in self.cache:
                self.cache.pop(key)
                self.cache[key] = value
            else:
                self.cache.pop(next(iter(self.cache.keys())))
                self.cache[key] = value