LQR:
def Gyro():
    return hub.imu.heading()

def Gyro_reset(angle=0):
    hub.imu.reset_heading(angle)

def map_value(x, in_min, in_max, out_min, out_max):
    
    if in_max == in_min:
        return out_max
    x = max(min(x, max(in_min, in_max)), min(in_min, in_max))
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



def lqr_gains(Q, R, b, kd=0.08):
    K1 = sqrt(Q / R) / b
    K2 = kd          
    return K1, K2


def turn_lqr(GyroDeg, Q=1, R=0.01, b=2, kd=0.08,
                  Maxpower=80, Minpower=12,
                  Tolerance=1.0, Settle=150, Timeout=3000, Brake=True):
 
    K1 = sqrt(Q / R) / b
    K2 = kd

    timer = StopWatch()
    total = StopWatch()
    last_time = timer.time()
    last_error = GyroDeg - Gyro()
    error_rate = 0
    settled = 0

    while total.time() < Timeout:
        now = timer.time()
        dt = (now - last_time) / 1000
        error = GyroDeg - Gyro()
        if dt > 0:
            raw_rate = (error - last_error) / dt
            error_rate = 0.7 * error_rate + 0.3 * raw_rate

        u = K1 * error + K2 * error_rate

        
        u = max(-Maxpower, min(Maxpower, u))
        if abs(error) > Tolerance and abs(u) < Minpower:
            u = Minpower if u >= 0 else -Minpower   

    
        if abs(error) <= Tolerance and abs(error_rate) < 15:
            settled += now - last_time
            u = 0
            if settled >= Settle:
                break
        else:
            settled = 0

        motor_B.dc(u)
        motor_F.dc(-u)

        last_error = error
        last_time = now
        wait(10)

    if Brake:
        Drive_base.stop()
    else:
        motor_B.dc(0)
        motor_F.dc(0)

turn with one wheel:

def turnl_lqr(GyroDeg, Q=1.5, R=0.01, b=2, kd=0.11,
              Maxpower=75, Minpower=15,
              Tolerance=1.5, Settle=150, Timeout=3000, Brake=True):
 
    K1 = sqrt(Q / R) / b
    K2 = kd
 
    timer = StopWatch()
    total = StopWatch()
    last_time = timer.time()
    last_error = angle_error(GyroDeg, Gyro())
    error_rate = 0
    settled = 0
 
    while total.time() < Timeout:
        now = timer.time()
        dt = (now - last_time) / 1000
        error = angle_error(GyroDeg, Gyro())
 
        if dt > 0:
            raw_rate = (error - last_error) / dt
            error_rate = 0.7 * error_rate + 0.3 * raw_rate
 
        u = K1 * error + K2 * error_rate
 
        u = max(-Maxpower, min(Maxpower, u))
        if abs(error) > Tolerance and abs(u) < Minpower:
            u = Minpower if u >= 0 else -Minpower
 
        if abs(error) <= Tolerance and abs(error_rate) < 15:
            settled += now - last_time
            u = 0
            if settled >= Settle:
                break
        else:
            settled = 0
 
        motor_F.dc(SIGN * (-u))
 
        last_error = error
        last_time = now
        wait(10)
 
    if Brake:
        motor_F.brake()
        Drive_base.stop()
    else:
        motor_F.dc(0)

def turn_lqr(GyroDeg, Q=1, R=0.01, b=2, kd=0.08,
                  Maxpower=80, Minpower=12,
                  Tolerance=1.0, Settle=150, Timeout=3000, Brake=True):
    K1 = sqrt(Q / R) / b
    K2 = kd
    timer = StopWatch()
    total = StopWatch()
    last_time = timer.time()
    last_error = GyroDeg - Gyro()
    error_rate = 0
    settled = 0
    while total.time() < Timeout:
        now = timer.time()
        dt = (now - last_time) / 1000
        error = GyroDeg - Gyro()
        if dt > 0:
            raw_rate = (error - last_error) / dt
            error_rate = 0.7 * error_rate + 0.3 * raw_rate
        u = K1 * error + K2 * error_rate
        u = max(-Maxpower, min(Maxpower, u))
        if abs(error) > Tolerance and abs(u) < Minpower:
            u = Minpower if u >= 0 else -Minpower   
        if abs(error) <= Tolerance and abs(error_rate) < 15:
            settled += now - last_time
            u = 0
            if settled >= Settle:
                break
        else:
            settled = 0
        motor_B.dc(u)
        motor_F.dc(-u)
        last_error = error
        last_time = now
        wait(10)
    if Brake:
        Drive_base.stop()
    else:
        motor_B.dc(0)
        motor_F.dc(0)

DEFAULT Code:

def move_deg(Power_B, Power_F, Deg, Brake=True):
    motor_B.reset_angle(0)
    motor_F.reset_angle(0)

    while (abs(motor_B.angle()) + abs(motor_F.angle())) / 2 < Deg:
        motor_B.dc(Power_B)
        motor_F.dc(Power_F)
        wait(10)   

    motor_B.dc(0)
    motor_F.dc(0)

    if Brake:
        motor_B.brake()
        motor_F.brake()

def move_time(Power_B, Power_F, ms, Brake=True):
    timer_move.reset()
    while timer_move.time() < ms:
        motor_B.dc(Power_B)
        motor_F.dc(Power_F)
    if Brake:
        Drive_base.stop()  

def a_motor(Power, Deg, is_wait=True):
    motor_A.run_angle(Power * 11, Deg, wait=is_wait)

def turn_gyro(hdg, Brake=True):
    Drive_base.settings(turn_rate=50 * 3.6)
    Drive_base.turn(hdg)
    if Brake:
        Drive_base.stop()

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.robotics import DriveBase
from umath import pi

global hub, motor_B, motor_F, motor_E, motor_A, Drive_base,Chassis_sensor
hub = PrimeHub()
hub.system.set_stop_button(Button.CENTER)
motor_B = Motor(Port.B,Direction.COUNTERCLOCKWISE) 
motor_F = Motor(Port.F) 
motor_E = Motor(Port.E) 
motor_A = Motor(Port.A)

DriveBase parameters:

Drive_base = DriveBase(motor_B,motor_F,wheel_diameter=88,axle_track=112)
Drive_base.use_gyro(True)
Drive_base.settings(turn_rate=60 * 3.6)
timer_move = StopWatch()

