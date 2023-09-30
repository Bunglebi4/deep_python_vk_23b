import time


def mean(k):
    def decorator(func):
        def inner(*args, **kwargs):
            if not hasattr(inner, 'call_times'):
                inner.call_times = []
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            inner.call_times.append(execution_time)
            if len(inner.call_times) > k:
                inner.call_times.pop(0)

            average_time = sum(inner.call_times) / len(inner.call_times)

            print(f"Среднее время выполнения последних {len(inner.call_times)} вызовов: {average_time:.6f} секунд")
            return result

        return inner
    return decorator

# @mean(k=10)
# def some_func():
#     time.sleep(1)
#
#
# for _ in range(10):
#     some_func()
