# @Version  :1.0
# @Author   :李祎凡
# @File     :test7
# @Time     :2025/3/13 下午5:55

# 统计三个班成绩情况，每个班有5个学生，要求完成如下的任务，
# 第一个求出各个班的平均分和所有班级的平均分
# 学生的成绩要求从键盘输入
# 第二个要求统计三个班及格的人数
sum = 0
Average_score = 0
pass_num = 0
total = 0

for i in range(1,4):
    for j in range(1,6):
        n = int(input(f"请输入第{i}个班，第{j}个同学的成绩"))
        if n >= 65:
            pass_num += 1
        sum = sum + n
        total = total + n
    print(f"第{i}个班，平均成绩为{sum/5}")
    sum = 0
print(f"总及格人数为：{pass_num}")
print(f"总平均分为：{total/15}")