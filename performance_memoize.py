import timeit

CACHE = dict()


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def run_factorial(n: int)-> int:
    if n in CACHE.keys():
        return CACHE[n]
    if n == 0:
        return 1
    else:
        CACHE[n] = n * factorial(n - 1)
        return CACHE[n]


stmt_no_cache = "" \
                "factorial(500);" \
                "factorial(400);" \
                "factorial(450);" \
                "factorial(350)"

stmt_cache = "" \
             "run_factorial(500);" \
             "run_factorial(400);" \
             "run_factorial(450);" \
             "run_factorial(350)"

print(timeit.timeit(stmt=stmt_no_cache, setup="from __main__ import factorial, run_factorial, CACHE", number=10000))
print(timeit.timeit(stmt=stmt_cache, setup="from __main__ import factorial, run_factorial, CACHE", number=10000))

