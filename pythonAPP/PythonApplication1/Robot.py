import math

class Robot():
    """general control methods for robot"""


    def __init__(self): ## class contructor
        print("initialised")
        self.m_lookdir = [0,1]  # look direction of the robot
        self.m_position = [0,0] # physical position of the robot
        self.m_velocity = [0,0] # velocity of the robot
        self.m_linearVel = 0    # scaler value to adjust the velocity
        self.m_currentAngle = 0;

    def setPosition(pos):
        m_position = pos
    
    def getPosition():
        return m_position

    def setVelocity(vel):
        m_velocity = vel

    def logic():
        xld = math.cos(m_currentAngle) *m_lookdir[0] - math.sin(m_currentAngle)*m_lookdir[1]
        yld = math.sin(m_currentAngle)*m_lookdir[0] + math.cos(m_currentAngle)*m_lookdir[1]
        m_lookdir = [xld,yld]

   
