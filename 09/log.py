import argparse
import logging


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            logging.debug("Key '%s' not found in cache", key)
            return self.cache.get(key)
        self.order.remove(key)
        self.order.append(key)
        logging.debug("Key '%s' found in cache. Value: %s", key, self.cache[key])
        return self.cache[key]

    def set(self, key, value) -> None:
        if key in self.cache:
            logging.debug("Key '%s' already exists. Updating value.", key)
            self.order.remove(key)
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            evicted_key = self.order.pop(0)
            logging.debug("Evicting key '%s' to make space.", evicted_key)
            del self.cache[evicted_key]
        logging.debug("Setting key '%s' with value '%s' in cache.", key, value)
        self.cache[key] = value
        self.order.append(key)


def setup_logging(log_to_stdout, custom_filter):
    formatter_for_stream = logging.Formatter(
        "[%(levelname)s] [%(asctime)s] [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
    )
    formatter_for_file = logging.Formatter(
        "[%(levelname)s] [%(asctime)s] [%(module)s:%(lineno)d] - %(message)s"
    )

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG if log_to_stdout else logging.INFO)
    stream_handler.setFormatter(formatter_for_stream)
    file_handler = logging.FileHandler("cache.log", mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter_for_file)
    logger.addHandler(file_handler)
    if log_to_stdout:
        logger.addHandler(stream_handler)
    if custom_filter:
        class CustomFilter(logging.Filter):
            def filter(self, record):
                return len(record.msg.split()) % 2 != 0

        logger.addFilter(CustomFilter())
    logger.info("Logging setup completed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='LRUCache logging example')
    parser.add_argument('-s', action='store_true', help='Log to stdout')
    parser.add_argument('-f', action='store_true', help='Apply custom filter')
    args = parser.parse_args()
    cache = LRUCache(3)
    setup_logging(args.s, args.f)
    cache.set(1, 'one')
    cache.get(1)
    cache.get(2)
    cache.set(3, 'three')
    cache.set(4, 'four')
    logging.debug("Debug message")
    cache.get(1)
    cache.get(3)
    cache.set(5, 'five')
    logging.debug("Additional debug message")
