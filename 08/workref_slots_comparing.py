import pstats
import timeit
import weakref
import cProfile
from io import StringIO


def cprofile_decorator(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        s = StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats()

        print(s.getvalue())

        return result

    return wrapper

class CustomObject:
    pass

class ClassWithAttributes:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class ClassWithSlots:
    __slots__ = ['a', 'b', 'c']

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class ClassWithWeakRef:
    def __init__(self, a, b, c):
        self.a = weakref.ref(a)
        self.b = weakref.ref(b)
        self.c = weakref.ref(c)
@cprofile_decorator
def create_instances():
    instances = [ClassWithAttributes(CustomObject(), CustomObject(), CustomObject()) for _ in range(1000000)]
    slot_instances = [ClassWithSlots(CustomObject(), CustomObject(), CustomObject()) for _ in range(1000000)]
    weakref_instances = [ClassWithWeakRef(CustomObject(), CustomObject(), CustomObject()) for _ in range(1000000)]
    time_attributes = timeit.timeit(lambda: ClassWithAttributes(CustomObject(), CustomObject(), CustomObject()), number=1000000)
    time_slots = timeit.timeit(lambda: ClassWithSlots(CustomObject(), CustomObject(), CustomObject()), number=1000000)
    time_weakref = timeit.timeit(lambda: ClassWithWeakRef(CustomObject(), CustomObject(), CustomObject()), number=1000000)

    print(f"Time for attributes: {time_attributes}")
    print(f"Time for slots: {time_slots}")
    print(f"Time for weakref: {time_weakref}")
    time_read_write_attributes = timeit.timeit(lambda: instances[0].a, number=1000000)
    time_read_write_slots = timeit.timeit(lambda: slot_instances[0].a, number=1000000)
    time_read_write_weakref = timeit.timeit(lambda: weakref_instances[0].a(), number=1000000)

    print(f"Time for read/write attributes: {time_read_write_attributes}")
    print(f"Time for read/write slots: {time_read_write_slots}")
    print(f"Time for read/write weakref: {time_read_write_weakref}")

if __name__ == "__main__":
    cProfile.run("create_instances()", sort="tottime")
