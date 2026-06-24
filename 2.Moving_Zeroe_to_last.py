x=[1,0,2,0,3,4,0]
# y=[]
# for i in x:
#     if i==0:
#         x.remove(i)
#         x.append(i)    
# # for i in y:
# #     x.append(i)
# print(x)
x=[i for i in x if i!=0]+[i for i in x if i==0]
print(x)