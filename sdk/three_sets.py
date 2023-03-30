import time
from multi_robomaster import multi_robot


def basic_task1(robot_group):
    # 20_10_31_16_05_09.jpg 中
    show_logo = ['0000r0000000r0000rrrrrrr0r00r00r0rrrrrrr0000r0000000r0000000r000'
                 # 20_10_31_16_06_35.jpg 国
                 '0rrrrrrr0r00000r0r0rrr0r0r00r00r0r0rrr0r0r00r0rr0r0rrrrr0rrrrrrr',
                 # 20_10_31_16_07_33.jpg V
                 '0r00000r0r00000r0r00000r0r00000r0r00000r00r000r0000r0r000000r000',
                 # 20_10_31_16_11_16.jpg 谷
                 '0000000000r0r0r00r00r00r000r0r0000r000r00r0rrr0r000r0r00000rrr00',
                 # 20_10_31_16_17_39.jpg 新
                 '0r000000rrr0000rr0r0rrr0rrr0r000rrr0rrrr0r00r0r0rrr0r0r0rr0r00r0',
                 # 20_10_31_16_18_39.jpg 体
                 '000r0r0000r00r000rrrrrrrr0r00r0000r0rrr000rr0r0r00r0rrr000r00r00',
                 # 20_10_31_16_19_41.jpg 媒
                 '0r000r0r0r00rrrrrrrr0rrrr0r000r0r0r0rrrr0r0000r0r0r00rrr00r0r0r0',
                 # 20_10_31_16_20_24.jpg 大
                 '000000000000r0000000r0000rrrrrrr0000r000000r0r0000r000r00r00000r',
                 # 20_10_31_16_25_55.jpg 会
                 '000rrr0000r000r00r0rrr0r0000000000rrrrr0000r000000r000r00rrrrrrr']
    # robot_group1.set_led(255, 255, 255)
    # 关闭起桨模式
    robot_group.motor_off().wait_for_completed()

    # 获取电量
    robot_group.get_battery()

    robot_group.set_led(command_dict={0: [32, 0, 0], 1: [
        0, 32, 0], 2: [0, 0, 32]})
    #  tl_drone.led.set_mled_graph(mled_smile1)
    # robot_group.set_mled_graph(mled_smile1)
    # robot_group.set_mled_graph(mled_smile2)

    robot_group.set_mled_bright(32)
    # 分别设置点阵

    robot_group.set_mled_graph(command_dict={
        0: [show_logo[0]], 1: [show_logo[1]], 2: [show_logo[2]]})
    time.sleep(0.5)
    robot_group.set_mled_graph(command_dict={
        0: [show_logo[3]], 1: [show_logo[4]], 2: [show_logo[5]]})

    # robot_group.set_mled_graph_scroll('l', 1.5, mled_smile1)
    # robot_group._set_mled_scroll(command_dict={0: [l, 1.5, mled_smile1], 1: [
    #     l, 1.5, mled_smile1], 2: [l, 1.5, mled_smile1]})

    # 起桨模式
    # robot_group.motor_on().wait_for_completed()
    # robot_group.mission_pad_on()
    # robot_group.takeoff().wait_for_completed()
    # robot_group.go({1: [-100, -100, 125, 100, "m12"],
    #                 2: [100, 100, 125, 100, "m12"]}).wait_for_completed()
    # robot_group.set_mled_char("r", "heart")
    # robot_group.go({1: [-100, 100, 125, 100, "m12"],
    #                 2: [100, -100, 125, 100, "m12"]}).wait_for_completed()
    # robot_group.set_mled_char("p", "heart")
    # robot_group.go({1: [100, 100, 125, 100, "m12"],
    #                 2: [-100, -100, 125, 100, "m12"]}).wait_for_completed()
    # robot_group.go({1: [100, -100, 125, 100, "m12"],
    #                 2: [-100, 100, 125, 100, "m12"]}).wait_for_completed()
    # robot_group.land().wait_for_completed()
    # robot_group.mission_pad_off()


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

    # 定义无人机编号
    robot_sn_list = ["0TQZHAGCNT0708", "0TQZHAFCNT060W", "0TQZHAGCNT074V"]
    # 创建一个多机控制对象 multi_drone
    multi_drone = multi_robot.MultiDrone()

    # 初始化无人机，目前教育系列无人机的初始化需要传入想要控制的飞机数量，定义无人机组网数量
    multi_drone.initialize(robot_num=3)
    # 在初始化后，使用已经实例化后的 multi_drone 对SN进行编号
    multi_drone.number_id_by_sn([0, robot_sn_list[0]], [
                                1, robot_sn_list[1]], [2, robot_sn_list[2]])
    # 创建分组
    tello_group1 = multi_drone.build_group([0, 1, 2])
    # 按组分配动作，
    multi_drone.run([tello_group1, basic_task1])
    multi_drone.close()
