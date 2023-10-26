class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return self.cache.get(key)
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def set(self, key, value) -> None:
        if key in self.cache:
            self.order.remove(key)
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            evicted_key = self.order.pop(0)
            del self.cache[evicted_key]
        self.cache[key] = value
        self.order.append(key)


cache = LRUCache(2)

cache.set("k1", "val1")
cache.set("k2", "val2")

assert cache.get("k3") is None
assert cache.get("k2") == "val2"
assert cache.get("k1") == "val1"

cache.set("k3", "val3")

assert cache.get("k3") == "val3"
assert cache.get("k2") is None
assert cache.get("k1") == "val1"
