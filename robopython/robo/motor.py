class Motor(object):

    def __init__(self, name, ble, id_num, action_id):
        self.is_connected = 0
        self.name = name
        self.id = id_num
        self.wheel_diameter = 89
        self.action_id = action_id
        self.BLE = ble
        self.action_status = None
        self.max_velocity = 300

    def set_pwm(self, pwm):   # 0, 128, 255 = 0 --- 127 = 100% CW    129 = 100% CCW
        assert type(pwm) is int, "pwm must be an integer"
        if pwm < 0 or pwm > 255:
            print ("PWM must be 0-255")
            return

        packet_size = 0x04
        command_id = 0x50
        payload_size = 0x02
        module_id = self.id-1
        command = bytearray([packet_size, command_id, payload_size, module_id, pwm])

        if self.is_connected == 1:
            self.BLE.write_to_robo(self.BLE.write_uuid, command)
            return
        print (self.name + " is NOT Connected!")

    def set_speed_cw(self, speed):   # speed 0-100
        assert type(speed) is int, "speed must be an integer"
        if speed < 0 or speed > 100:
            print ("Speed must be 0 - 100")
        pwm = int((speed*127/100))
        self.set_pwm(pwm)

    def set_speed_ccw(self, speed):   # speed 0-100
        assert type(speed) is int, "speed must be an integer"
        if speed < 0 or speed > 100:
            print ("Speed must be 0 - 100")
            return
        pwm = int((speed*127/100))
        pwm = 256 - pwm
        self.set_pwm(pwm)

    def stop(self):
        self.set_pwm(0)

    def set_velocity(self, vel):
        pass

    def get_encoder(self):
        pass

    def spin_distance(self, vel, distance, wd=89):  # distance < 100 and vel < 300
        assert type(wd) is int, "Wheel Diameter must be an integer in mm"
        assert type(distance) is int, "Distance must be an integer in cm"
        assert type(vel) is int, "Velocity must be an integer 0-100%"

        vel = (vel*self.max_velocity/100)

        packet_size = 10
        command_id = 0xa0
        payload_size = 0x08
        module_id = self.id-1
        velocity_h = vel/256
        velocity_l = vel % 256
        wd_h = wd/256
        wd_l = wd % 256
        distance_h = distance / 256
        distance_l = distance % 256
        command = bytearray([packet_size, command_id, payload_size, self.action_id, module_id, velocity_h, velocity_l,
                             wd_h, wd_l, distance_h, distance_l])
        if self.is_connected == 1:
            self.BLE.write_to_robo(self.BLE.write_uuid, command)
            return
        print (self.name + " is NOT Connected!")

    def spin_velocity(self, vel, wd=89):
        self.spin_distance(vel, 65000, wd)

    def action_complete(self, cmd_status):
        self.action_status = cmd_status

    def check_action(self):
        value = self.action_status
        if self.action_status is None:
            return
        self.action_status = None
        return value
