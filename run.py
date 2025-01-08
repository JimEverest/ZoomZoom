import subprocess
import sys

def main():
    """
    启动 zoomzoom 应用程序。
    """
    try:
        # 使用 subprocess 调用 zoomzoom 命令
        subprocess.run([sys.executable, "-m", "zoomzoom"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"启动 zoomzoom 失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()