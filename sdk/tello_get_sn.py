import robomaster
from robomaster import robot
 # robomaster.config.LOCAL_IP_STR = "192.168.10.22"

if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    # 获取飞机SN信息
    SN = tl_drone.get_sn()
    print("drone sn: {0}".format(SN))

    tl_drone.close()

    