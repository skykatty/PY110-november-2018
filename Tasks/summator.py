




def sum(input):
    my_sum = 0
    for i in input:
        my_sum += i

        class TypeError(Exception):
            pass

        class NotTypeError(TypeError):
            pass
        if type(input) != list:
            raise NotTypeError("Input isn`t a list")
    return my_sum

def avg(input):
    my_avg = sum(input) / len(input)
    return my_avg


print(sum([1,2,3,4,5]))
print(avg([1,2,3,4,5]))

# def f_sum(my_list:list)->int:
#     """
#     It returns sum of all elements
#     :return:
#     """
#
#     class TypeError(Exception):
#         pass
#     class NotTypeError(TypeError):
#         pass
#
#
#     if type(my_list) != list:
#         raise NotTypeError("Input isn`t a list")
#
#
#     my_sum = 0
#     for i in my_list:
#         my_sum += i
#
#
#     return my_sum
#
# def avg(my_list:list)->int:
#     """
#     It returns avg of all elements
#     :return:
#     """
#     my_avg = f_sum(list) / len(my_list)
#     return my_avg
#
# print(f_sum([1,2,3,4,5]))