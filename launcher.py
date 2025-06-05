import subprocess
import sys
import os

def main():
    # 调用 test_update/main.py 进行更新
    python_exe = sys.executable
    script_path = os.path.join(os.path.dirname(__file__), "test_update", "main.py")
    subprocess.run([python_exe, script_path])
    # 退出自身
    sys.exit(0)

if __name__ == "__main__":
    main()