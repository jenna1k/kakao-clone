
# num_range = range(1,1000)
# num_list = []
#
# for i in num_range:
#     if i % 3 == 0:
#         num_list.append()
#     return
#     else i % 5 == 0:
#         num_list.append()
#     return
# # return
#
# print num_list
# ----------------------------------
c = 0
for x in range(1000):
       if x%3 == 0 or x%5 == 0:
           c += x
print(c)

# ----------------------------------
print(sum(x for x in range(1000) if x%3==0 or x%5==0))
# ----------------------------------
list_3 = [x for x in range(0,1000,3)]
list_5 = [x for x in range(0,1000,5)]
list_15 = [x for x in range(0,1000,15)]

answer = sum(list_3) + sum(list_5) - sum(list_15)

print answer
# ----------------------------------


# ----------------------------------
# ----------------------------------

# xn_list = []
# minus_list = []
#
# for i in xn_list:
#     if i < 0:
#

list = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 7, 6, 9, 8, 11, 10]

def sort_item(list):
    t1, t2 = [], []
    for i in list:
        if i < 0:
            t1.append(i)
        else:
            t2.append(i)
    result = t1 + t2
    return result

print sort_item(list)
