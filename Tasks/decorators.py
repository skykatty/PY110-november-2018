import datetime
import time

def showtime(f):
    def showtime_wrapper (*ar, **kw):
        perf = time.perf_counter()
        # showtime_wrapper.starttime = datetime.datetime.now()
        # showtime_wrapper.count += 1
        # print("Функция {} была вызвана {} раз".format(showtime_wrapper.fname, showtime_wrapper.count ))
        res = f(*ar, **kw)
        perf = time.perf_counter() - perf
        print("Время работы функции {} {}".format(showtime_wrapper.fname, perf))
        return res
    showtime_wrapper.fname = f.__name__
    showtime_wrapper.count = 0
    print('Run showtime')
    return showtime_wrapper

def cache(f):
    def cache_wrapper(*args, **kwargs):
        # включаем в индекс позиционные аргументы
        index = str(args)
        # сортируем имена именованных аргументов и включаем их в индекс в отсортированном виде
        kwkeyssort = list(kwargs.keys())
        kwkeyssort.sort()
        for a in kwkeyssort:
            index = index + a+'='+str(kwargs[a])+'&'
        # print("index=>", index)
        # в принципе от index можно взать хеш и сохранять в кеше его, но мы не будем этого делать )

        if index in cache_wrapper.cache:
            res = cache_wrapper.cache[index]
        else:
            res = f(*args, **kwargs)
            cache_wrapper.cache[index] = res
        return res
    cache_wrapper.cache = {}
    print('Run cache')
    return cache_wrapper


def counter(f):
    def counter_wrapper(*args, **kwargs):
        counter_wrapper.count += 1
        print("Функция {} была вызвана {} раз".format(counter_wrapper.fname, counter_wrapper.count))
        res = f(*args, **kwargs)
        return res
    counter_wrapper.count = 0
    counter_wrapper.fname = f.__name__
    print('Run counter')
    return counter_wrapper


@cache  # для оценки варианта без кеширования данный декоратор нужно просто закомментировать
@counter
@showtime
def fibonachi(n, *args, **kwargs):
    if n <= 1:
        return 1
    else:
        return fibonachi(n - 1,*args, **kwargs) + fibonachi(n - 2, *args, **kwargs)

n = 30
ret = fibonachi(n, 123, 345, test2=22, test1=1) # в n количество чисел последовательности
print('fibonachi('+str(n)+')=', ret)