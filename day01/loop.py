successful = False
for num in range(3):
    print("hello", num+1, (num+1)*'.')
    if(successful):
        print("success")
        break
# 个人理解是最终通知
else:
    print("fail")

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

for t in range(1, 4):
    print('*'*(t))
