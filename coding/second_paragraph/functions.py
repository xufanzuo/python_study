'''
搜索；两个字符串公共元素
'''
# def intersect(seq1, seq2):
#     res = []
#     for x in seq1:
#         if x in seq2:
#             res.append(x)
#         return res
# #快速方法，列表解析；[x for x in s1 if x in s2]

'''
作用域实例
'''
X = 99
def func(Y):
    X = 55
    Z = X + Y
    return print(Z)

func(1)