
def cache(fn):
    def wrapper(*args, **kwargs):
        str_args = str(args)
        str_kwards = str(kwargs) + str_args
        if str_kwards in wrapper.cash:
            result = wrapper.cash[str_kwards]
        else:
            result = fn(*args, **kwargs)
        wrapper.cash[str_kwards] = result
        return result
    wrapper.cash = {}
    return wrapper

def counter(fn):
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        print("Функция была вызвана {} раз".format(wrapper.count))
        result = fn(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper

@cache
@counter
def fibonachi(n, n1, first, second=2):
    if n <= 1:
        return first
    else:
        return fibonachi(n - 1, n1, first) + fibonachi(n - 2, n1, first)
N = 10
print(f"Функция Фибоначи от {N}: ", fibonachi(N, 5, first=1, second=2))

