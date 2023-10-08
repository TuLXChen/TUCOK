import time

# 设置工作时间（以分钟为单位）
work_time = 25
# 设置休息时间（以分钟为单位）
break_time = 5

while True:
    print(f"开始工作 {work_time} 分钟...")
    time.sleep(work_time * 60)
    
    print(f"休息 {break_time} 分钟...")
    time.sleep(break_time * 60)
