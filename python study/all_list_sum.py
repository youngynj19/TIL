# def all_list_sum(*args):
#     counts = 0
#     for lists in args:
#         #print(lists)
#         for sub_ls in lists:
#         #    print(i)
#             for i in sub_ls:
#                 counts += i
#     return counts


def all_list_sum(lists):
    counts = 0
    for sub_ls in lists:
        #print(lists)
        for i in sub_ls:
            counts += i
    return counts



print(all_list_sum([[1], [2,3], [4,5,6], [7,8,9,10]]))
