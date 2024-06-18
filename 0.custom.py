# custom.py

from jetbot import Robot
robot = Robot()

def forward():
    robot.left_motor.value = 0.5 # 0~1
    robot.right_motor.value = 0.5
    
def backward():
    robot.left_motor.value = -0.5
    robot.right_motor.value = -0.5
def left():
    robot.left_motor.value = 0.5
    robot.right_motor.value = 1
def right():
    robot.left_motor.value = 1
    robot.right_motor.value = 0.5
    
def stop():
    robot.left_motor.value = 0.0
    robot.right_motor.value = 0.0
    
print("hello")

if __name__ == "__main__" :
    print("main")