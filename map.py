k = [1,2,3,4,5,10,2.3,]
# 1 sposob
# nowa_lista =[]
# for x in k:
#     nowa_lista.append(x*2)
# print(nowa_lista)

# 2 sposob

# def razy_dwa(elem):
#     return elem * 2
#
# print(list(map(razy_dwa,k)))
#3 sposob
#print((list(map(lambda elem: elem * 2,k))))

print((list(map(lambda elem: elem *2,"string"))))