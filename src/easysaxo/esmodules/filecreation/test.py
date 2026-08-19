class MyClass:
    def __init__(self, build):
        self.build = build

me = MyClass("2")
import time
print(f"Build: {me.build}")
time.sleep(3)