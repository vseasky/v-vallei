import time
from multi_robomaster import multi_robot


def v_size_task(robot_group):

    # 对不上序号？
    # show_logo = ['0000000000000000000000000000000000000000000000000000000000000000',
    #              # 20_10_31_16_05_09.jpg 0 中
    #              '0000r0000000r0000rrrrrrr0r00r00r0rrrrrrr0000r0000000r0000000r000'
    #              # 20_10_31_16_06_35.jpg 1 国
    #              '0rrrrrrr0r00000r0r0rrr0r0r00r00r0r0rrr0r0r00r0rr0r0rrrrr0rrrrrrr',
    #              # 20_10_31_16_07_33.jpg 2 V
    #              '0r00000r0r00000r0r00000r0r00000r0r00000r00r000r0000r0r000000r000',
    #              # 20_10_31_16_11_16.jpg 3 谷
    #              '0000000000r0r0r00r00r00r000r0r0000r000r00r0rrr0r000r0r00000rrr00',
    #              # 20_10_31_16_17_39.jpg 4 新
    #              '0r000000rrr0000rr0r0rrr0rrr0r000rrr0rrrr0r00r0r0rrr0r0r0rr0r00r0',
    #              # 20_10_31_16_19_41.jpg 5 媒
    #              '0r000r0r0r00rrrrrrrr0rrrr0r000r0r0r0rrrr0r0000r0r0r00rrr00r0r0r0',
    #              # 20_10_31_16_18_39.jpg 6 体
    #              '000r0r0000r00r000rrrrrrrr0r00r0000r0rrr000rr0r0r00r0rrr000r00r00',
    #              # 20_10_31_16_20_24.jpg 7 大
    #              '000000000000r0000000r0000rrrrrrr0000r000000r0r0000r000r00r00000r',
    #              # 20_10_31_16_25_55.jpg 8 会
    #              '000rrr0000r000r00r0rrr0r0000000000rrrrr0000r000000r000r00rrrrrrr']
    # show_logo_zhong = '0000r0000000r0000rrrrrrr0r00r00r0rrrrrrr0000r0000000r0000000r000'
    # show_logo_guo = '0rrrrrrr0r00000r0r0rrr0r0r00r00r0r0rrr0r0r00r0rr0r0rrrrr0rrrrrrr'
    # show_logo_v = '0r00000r0r00000r0r00000r0r00000r0r00000r00r000r0000r0r000000r000'
    # show_logo_gu = '0000000000r0r0r00r00r00r000r0r0000r000r00r0rrr0r000r0r00000rrr00'
    # show_logo_ma = '0pprrrr000r000r000r000r000rrrrrr0000000r0rrrrr0r0000000r0000rrrr'
    # show_logo_lan = '0r00r00r0r000rr0rrr0rrrrrrr00000rrr00rr00r0000000r0rrrrr00000000'
    # show_logo_shan = '0000r0000000r0000000r0000r00r00r0r00r00r0r00r00r0rrrrrrr00000000'
    # show_logo_love = '00rrrr000r0000r0r0r00r0rr000000rr0r00r0rr00rr00r0r0000r000rrrr00'
    # show_logo_wen = '0000r0000000r0000rrrrrrr00r000r0000r0r000000r000000r0r0000r000r0'
    # show_logo_chuan = '00r0000r0rrr000rrr0rr00r0rrr0r0r0r0r0r0r0rrr0r0r0r00r0rr0rrrr0rr'
    # show_logo_yuan = '0rrrrrrr0r0rrr0r0r00000r0rrrrrrr0r0r0r0r0r0r0r0r0rrr0rrr0rrrrrrr'
    # mled_smile1 = '000000000r0000r0r0r00r0r000000000000000000r00r00000rr00000000000'
    # 关闭起桨模式
    # robot_group.motor_off().wait_for_completed()

    robot_group.set_led([0, 32, 0])

    robot_group.set_mled_bright(32)
    # 分别设置点阵

    # robot_group.set_mled_graph(command_dict={
    #     0: show_logo_zhong, 1: show_logo_guo, 2: show_logo_v,
    #     3: show_logo_gu, 4: show_logo_ma, 5: show_logo_lan,
    #     6: show_logo_shan, 7: show_logo_love, 8: mled_smile1})

    robot_group.mission_pad_on()
    # 起桨模式5
    robot_group.motor_on().wait_for_completed()
    robot_group.takeoff().wait_for_completed()
    # dij右边为x正，上边为y正, 为了避免碰撞按以下位置摆放
    robot_group.go({0: [-120, -120, 100, 100, "m12"],
                    1: [0,  -120, 100, 100, "m12"],
                    2: [120, -120, 100, 100, "m12"],
                    3: [-120, 0, 100, 100, "m12"],
                    4: [0,  0, 100, 100, "m12"],
                    5: [120, 0, 100, 100, "m12"],
                    6: [-120, 120, 100, 100, "m12"],
                    7: [0,  120, 100, 100, "m12"],
                    8: [120, 120, 100, 100, "m12"]}).wait_for_completed()
    robot_group.go({0: [-120, -120, 80, 70, "m12"],  # 1
                    1: [-40,  -120, 80, 70, "m12"],  # 2
                    2: [40, -120, 80, 70, "m12"],    # 3
                    3: [-60, 30, 125, 70, "m12"],    # 4
                    4: [0,  -60, 100, 70, "m12"],    # 5
                    5: [120, -120, 80, 70, "m12"],   # 6
                    6: [-120, 120, 150, 70, "m12"],  # 7
                    7: [60,  80, 125, 70, "m12"],    # 8
                    8: [120, 120, 150, 70, "m12"]    # 9
                    }).wait_for_completed()
    robot_group.go({0: [-120, -120, 100, 70, "m12"],  # 1
                    1: [-40,  -60, 100, 70, "m12"],   # 2
                    2: [40, 0, 100, 100, "m12"],      # 3
                    3: [-60, 120, 150, 70, "m12"],    # 4
                    4: [0,  120, 150, 70, "m12"],     # 5
                    5: [120, 60, 100, 70, "m12"],     # 6
                    6: [-120, 120, 150, 70, "m12"],   # 7
                    7: [60,  120, 150, 70, "m12"],    # 8
                    8: [120, 120, 150, 70, "m12"]     # 9
                    }).wait_for_completed()
    robot_group.go({0: [0, -120, 75, 70, "m12"],     # 1
                    1: [0,  -60, 100, 70, "m12"],    # 2
                    2: [0, 0, 125, 100, "m12"],      # 3
                    3: [-60, 120, 175, 70, "m12"],   # 4
                    4: [0,  120, 175, 70, "m12"],    # 5
                    5: [0, 60, 150, 70, "m12"],      # 6
                    6: [-120, 120, 175, 70, "m12"],  # 7
                    7: [60,  120, 175, 70, "m12"],   # 8
                    8: [120, 120, 175, 70, "m12"]    # 9
                    }).wait_for_completed()

    robot_group.land().wait_for_completed()

    robot_group.mission_pad_off()
    # 关闭起桨模式
    robot_group.motor_off().wait_for_completed()


if __name__ == '__main__':
    robot_sn_list = ["0TQZH97CNT04AH",
                     "0TQZH79ED00HA3",
                     "0TQZH97CNT046V",
                     "0TQZH97CNT0407",
                     "0TQZHAGCNT0766",
                     "0TQZHAGCNT0708",
                     "0TQZHAFCNT060W",
                     "0TQZHAGCNT074V",
                     "0TQZHAFCNT05GE"]
    multi_drone = multi_robot.MultiDrone()
    multi_drone.initialize(robot_num=9)
    multi_drone.number_id_by_sn([0, robot_sn_list[0]], [1, robot_sn_list[1]], [2, robot_sn_list[2]],
                                [3, robot_sn_list[3]], [4, robot_sn_list[4]], [
                                    5, robot_sn_list[5]],
                                [6, robot_sn_list[6]], [7, robot_sn_list[7]], [8, robot_sn_list[8]])

    multi_drone_group1 = multi_drone.build_group([0, 1, 2, 3, 4, 5, 6, 7, 8])
    multi_drone.run([multi_drone_group1, basic_task2])
    multi_drone.close()
