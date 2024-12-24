import subprocess

def auto_install():
    commands = (
        "pkg i wget -y",
        "wget https://raw.githubusercontent.com/Hoang2255/install-pip/refs/heads/main/setup.sh",
        "sh setup.sh",
        "rm setup.sh"
    )
    
    try:
        print("Đang Chẩn bị")
        for cmd in commands:
            print(f"Đang chạy {cmd}")
            result = subprocess.run(cmd, shell=True, check=True, text=True)
            if result.returncode == 0:
                print(f"xong {cmd}")
            else:
                print(f"Lỗi {cmd}")
                break
        print("Cài đặt hoàn tất")
    except subprocess.CalledProcessError as e:
        print(f"Lỗ {e}")
    except Exception as ex:
        print(f"Lỗi {ex}")

if __name__ == "__main__":
    auto_install()