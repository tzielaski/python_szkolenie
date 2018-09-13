import timeit

CACHE = dict()


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def run_factorial(n: int)-> int:
    cached = CACHE.get(n)
    if cached:
        return cached
    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        CACHE[n] = result
        return result


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

duration_no_cache = timeit.timeit(stmt=stmt_no_cache, globals=globals(), number=10000)
duration_cache = timeit.timeit(stmt=stmt_cache, globals=globals(), number=10000)

print(f'Duration cache:    {duration_cache}')
print(f'Duration no cache: {duration_no_cache}')
print(f'{round(duration_no_cache/duration_cache)} times faster with cache.')

