#python监控脚本说明

导入模块

```
import psutil  # 用于获取系统资源使用情况（CPU、内存等）  
import time  # 用于控制循环的时间间隔  
from datetime import datetime  # 用于获取当前时间并格式化  		
```

```
def 定义函数():  
    # 定义CPU和内存的使用阈值  
    cpu_cetain = 75  
    mem_cetain = 75  

    # 无限循环，持续监控系统资源  
    while True:  
        try:  
            # 获取当前CPU使用率  
            cpu_usage = psutil.cpu_percent()  
            # 获取当前内存使用率  
            mem_usage = psutil.virtual_memory().percent  

            # 如果CPU或内存使用率超过阈值，打印警告信息  
            if cpu_usage > cpu_cetain or mem_usage > mem_cetain:  
                print(f"CPU{cpu_cetain}%，内存{mem_usage}%")  

            # 打开日志文件，以追加模式写入  
            with open("monitor.log", "a") as f:  
                # 获取当前时间并格式化  
                current_time = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")  
                # 构造日志条目  
                log_entry = f"CPU:{cpu_usage}, 内存:{mem_usage}, Time:{current_time}\n"  
                # 将日志条目写入文件  
                f.write(log_entry)  

            # 等待10秒后继续下一次监控  
            time.sleep(10)  

        # 捕获键盘中断（Ctrl+C），停止监控  
        except KeyboardInterrupt:  
            print("监控资源停止")
```



\# 如果脚本作为主程序运行，调用监控函数

```
if __name__ == "__mian__":
	函数名()
```

