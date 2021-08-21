y = 1
count = 0
# range函数左闭右开 在python中字符串 列表等也是被视为可迭代的
# for x in range(1, 10):
#     if(x % 2 == 0):
#         count += 1
#         print(x)
# print("there is "+str(count)+" even numbers")


while y < 10:
    if(y % 2 == 0):
        print(y)
        count += 1
    y += 1
else:
    #print("there is "+str(count)+" even numbers")
    print(f"we have {count} even numbers")
