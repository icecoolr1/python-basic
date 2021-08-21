import math  # 导入math库
print("hello")
print("*"*10)
x = 1
is_Male = True
# 获取字符串函数
print(len("hhhhhhhhhh"))
test = "testing"
print(test[0])
# 倒着数
print(test[-1])
# 不包括最后一个索引 0 1 2
print(test[0:3])
newTest = "test"+"test"
# \" \' \\ \n
newTest2 = "test\nnonono"
first = "james"
last = "bond"
# 格式化字符串
full = f"{first} {last}"
print(full)
#print("newTest: "+newTest)
#print("newTest2: "+newTest2)
course = "   lalala  "
# 取消字符前和后的空格
print(course.strip())
print(course.find("la"))
print(course.replace("lala", "ddd"))
# 返回boolean类型
print("la" in course)
print("la" not in course)
x = 1 + 3j  # 1+3i 复数
# 返回整数
print(10 // 3)
# 立方
print(10 ** 3)

# 绝对值
print(abs(-10))
# 四舍五入
print(round(2.9))
# 取整函数
math.ceil(2.9)
