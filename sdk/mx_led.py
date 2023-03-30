import robomaster
import multi_robomaster 
from robomaster import robot
from multi_robomaster import multi_robot

if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    # 获取飞机电池电量信息
    tl_battery = tl_drone.battery
    battery_info = tl_battery.get_battery()
    print("Drone battery soc: {0}".format(battery_info))


    tl_led = tl_drone.led

    tl_led.set_led([255, 0, 0])


    # 切换飞行器WiFi模式为组网模式，指定路由器SSID和密码
    #tl_drone.config_sta(ssid="TELLO_TEST", password="12345678")


    tl_drone.close()
