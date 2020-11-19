from simpylc import *


class Control(Module):
    def __init__(self):
        Module.__init__(self)

        self.page('sailboat movement control')

        self.group('control', True)
        self.movement_speed_x = Register(0)
        self.movement_speed_y = Register(0)

        self.group('sail')
        self.target_sail_angle = Register()
        
        self.group('rudder')
        self.target_gimbal_rudder_angle = Register()

    def sweep(self):
        #self.movement_speed = 0.1
        if self.target_sail_angle > 90:
            self.target_sail_angle.set(90)

        if self.target_sail_angle < -90:
            self.target_sail_angle.set(-90)

        if self.target_gimbal_rudder_angle > 45:
            self.target_gimbal_rudder_angle.set(45)
        
        if self.target_gimbal_rudder_angle < -45:
            self.target_gimbal_rudder_angle.set(-45)