import psutil
import time
from datetime import datetime


def monitor_src():
    cpu_cetain = 75
    mem_cetain = 75

    while True:
        try:
            cpu_usage = psutil.cpu_percent()
            mem_usage = psutil.virtual_memory().percent

            print(f"CPU{cpu_cetain}%，内存{mem_usage}")
            if cpu_usage > cpu_cetain or mem_usage > mem_cetain:
                print(f"CPU{cpu_cetain}%，内存{mem_usage}%")


            with open("monitor.log", "a") as f:
                current_time = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")
                log_entry = f"CPU:{cpu_usage}, 内存:{mem_usage}, Time:{current_time}\n"
                f.write(log_entry)

            time.sleep(10)

        except KeyboardInterrupt:
            print("监控资源停止")



if __name__ == "__main__":
    monitor_src()