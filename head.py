from servoserial import ServoSerial
servo = ServoSerial()

# 중앙값 세팅
# servo.Servo_serial_double_control(1, 3300, 2, 2150)

# 1번 ServoMotor -> Pan
# 2번 ServoMotor -> Tilt

global pan, tilt
pan = 3300   # 좌우 중앙값, 인덱스 1번
tilt = 2150  # 상하 중앙값, 인덱스 2번

def pan_left():  # 왼쪽으로 머리 돌리기
    global pan
    pan += 100
    servo.Servo_serial_control(1, pan)
    
def pan_right():  # 오른쪽으로 머리 돌리기
    global pan
    pan -= 100
    servo.Servo_serial_control(1, pan)
    
def tilt_up():   # 위로 머리 올리기
    global tilt
    tilt += 100
    servo.Servo_serial_control(2, tilt)
    
def tilt_down(): # 아래로 머리 내리기
    global tilt
    tilt -= 100
    servo.Servo_serial_control(2, tilt)
    
def center():
    global pan, tilt
    pan = 2100
    tilt = 2700
    servo.Servo_serial_double_control(1, pan, 2, tilt)