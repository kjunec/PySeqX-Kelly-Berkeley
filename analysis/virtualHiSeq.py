#!/usr/bin/python

# HiSeq Simulater
class xstage():
    def __init__(self):
        self.spum = 100/244

class ystage():
    def __init__(self):
        self.spum = 100

class zstage():
    def __init__(self):
        self.spum = 0.656
        self.position = [21500, 21500, 21500]
        #self.xstep = [-10060, -10060, 44990]                                     # x step position of motors
        #self.ystep = [-2580000, 5695000, 4070000]                                # y step position of motors
        self.xstep = [60720,   -8930, -8930]
        self.ystep = [2950000, 7950000, -4050000]
    def get_motor_points(self):
        points = [[self.xstep[0], self.ystep[0], self.position[0]],
                  [self.xstep[1], self.ystep[1], self.position[1]],
                  [self.xstep[2], self.ystep[2], self.position[2]]]

        return points

class objstage():
    def __init__(self):
        self.spum = 262

class HiSeq():
    def __init__(self):
        self.x = xstage()
        self.y = ystage()
        self.z = zstage()
        self.obj = objstage()
        self.im_obj_pos = 30000
