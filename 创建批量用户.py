import subprocess




users = [
    ("user1","password1"),
    ("user2","password2"),
]

def cretae_users():
    for username,password in users:
        try:
            subprocess.run(f"sudo useradd -m {username}",shell=True,check=True)
            subprocess.run(f"sudo echo '{username}:{password}' | chpasswd",shell=True,check=True)
            print(f"创建用户: {username}")
        except subprocess.CalledProcessError as e:
            print(f"创建用户 {username} 失败：{str(e)}")


if __name__ == "__main__":
    cretae_users()