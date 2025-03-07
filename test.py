import keyboard
import time

def start():
    print("开始运行")

def stop():
    print("结束运行")
    #keyboard.unhook_all()  # 停止监听按键事件

def main():
    start_key = "a"  # 开始运行的按键
    stop_key = "b"   # 结束运行的按键

    #keyboard.on_press_key(start_key, lambda _: start())  # 监听开始运行的按键
        # 监听结束运行的按键

    # 进入一个无限循环，以便程序保持运行
    while True:
        keyboard.on_press_key(start_key, lambda _: start())
        keyboard.on_press_key(stop_key, lambda _: stop())
        time.sleep(1)

if __name__ == "__main__":
    main()
