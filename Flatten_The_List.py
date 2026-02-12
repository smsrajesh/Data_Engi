# Approach 1: Using type() to check if element is a list and recursive call to flatten sublist

def Flatten(lst,res=None):
    if res is None:
        res=[]
    for i in lst:
        if type(i)==list:
            Flatten(i,res)
        else:
            res.append(i)
    return res

n=[1,9,[5],[2,3,[8]],[6,7]]

print(Flatten(n))



# # Approach 2 :using isinstance() to check if element is a list and recursive call to flatten sublist

# def Single_list(n, result=None):
#     if result is None:
#         result = []   # create new empty list first time

#     for i in n:
#         if isinstance(i, list):        # ✅ check if element is a list
#             Single_list(i, result)     # recursive call if nested list
#         else:
#             result.append(i)           # add number to final list

#     return result

# val = [10, 20, 30, [40, 50, [60, 70, [80, [90]]]]]

# print(Single_list(val))


# # Approach 3: Using extend() method to add elements of sublist to result list

# def Single_list_1(n, result=None):
#     if result is None:
#         result = []   # create new empty list first time

#     for i in n:
#         if isinstance(i, list):        # ✅ check if element is a list
#             result.extend(Single_list_1(i))  # extend result with flattened sublist
#         else:
#             result.append(i)           # add number to final list

#     return result

# val = [10, 20, 30, [40, 50, [60, 70, [80, [90]]]]]

# print(Single_list_1(val))



