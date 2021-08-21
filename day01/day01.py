# 获取用户输入
# 不要在runner里打开 runner控制台只读
# x输入为string类型 需要进行类型转换
x = input("x: ")
y = int(x)+1
#print(f"x:{x} y:{y}")
print("y="+str(y))
# if条件后面必须使用:来代表条件结束 所有的条件执行语句必须缩进 当想要结束循环时不使用缩进
if y > 10:
    print('yes')
elif y < 5:
    print('not bad')
else:
    print("no")
print('end')

age = 21
message = "eligible" if age >= 20 else "lalala"
print(message)
# PYTHON允许使用数学表达式作为if条件判断
if 18 < age <= 45:
    print("young")

# and有假则假 or有真则真 not取反
