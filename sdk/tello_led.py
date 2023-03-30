import time
from multi_robomaster import multi_robot


def basic_task1(robot_group1):
    robot_group1.takeoff().wait_for_completed()
   # time.sleep(0.5)
    robot_group1.land().wait_for_completed()


def basic_task2(robot_group2):
    robot_group2.takeoff().wait_for_completed()
    # time.sleep(0.25)
    robot_group2.up(50).wait_for_completed()
    # time.sleep(0.25)
    robot_group2.land().wait_for_completed()


# | 新机1    | 0TQZH97CNT04AH |
# | 新机2    | 0TQZH79ED00HA3 |
# | 新机3    | 0TQZH97CNT046V |
# | 新机4    | 0TQZH97CNT0407 |
# | 新机5    | 0TQZHAGCNT0766 |
# | 新机6    | 0TQZHAGCNT0708 |
# | 新机7    | 0TQZHAFCNT060W |
# | 新机8    | 0TQZHAGCNT074V |
if __name__ == '__main__':
    # get drone sn by run the expamles of /15_multi_robot/multi_drone/01_scan_ip.py

    # 定义无人机组网数量

    # 定义无人机编号
    robot_sn_list = ["0TQZH97CNT04AH", "0TQZH79ED00HA3",
                     "0TQZH97CNT046V", "0TQZH97CNT0407",
                     "0TQZHAGCNT0766", "0TQZHAGCNT0708",
                     "0TQZHAFCNT060W", "0TQZHAGCNT074V"]
    # 创建一个多机控制对象 multi_drone
    multi_drone = multi_robot.MultiDrone()
    # 初始化无人机，目前教育系列无人机的初始化需要传入想要控制的飞机数量
    multi_drone.initialize(robot_num=8)
    # 在初始化后，使用已经实例化后的 multi_drone 对SN进行编号
    multi_drone.number_id_by_sn(
        [0, robot_sn_list[0]], [1, robot_sn_list[1]],
        [2, robot_sn_list[2]], [3, robot_sn_list[3]],
        [4, robot_sn_list[4]], [5, robot_sn_list[5]],
        [6, robot_sn_list[6]], [7, robot_sn_list[7]])
    # 创建分组
    tello_group1 = multi_drone.build_group([0, 1, 2, 3, 4])
    tello_group2 = multi_drone.build_group([5, 6, 7])
    # 按组分配动作，
    multi_drone.run([tello_group1, basic_task1], [tello_group2, basic_task2])
    multi_drone.close()
