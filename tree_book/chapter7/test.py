# def echo(message):
#     print(message)

# schedule = [(echo,"SPAM!"),(echo,'Ham!')]
# for (func,arg) in schedule:
#     func(arg)


#######################################
#计算一个嵌套的子列表结构中所有数字的总和:
#[1,[2,[3,4],5],6,[7,8]]

'''
def sumtree(L):
    tot = 0
    for x in L:
        #isinstance(obj,class)判断obj是不是class的实例化
        #isisntance(1,int)->True
        if not isinstance(x,list):
            tot += x
        else:
            tot += sumtree(x)
    return tot
L=[1,[2,[3,4],5],6,[7,8]]
print(sumtree(L))
'''

########################################################
