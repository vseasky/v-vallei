import time
from multi_robomaster import multi_robot


def v_size_task(robot_group):

    # robot_group.motor_off().wait_for_completed()
    # robot_group.set_led([0, 32, 0])
    # robot_group.set_mled_bright(32)
    # 分别设置点阵
    robot_group.mission_pad_on()
    robot_group.motor_on().wait_for_completed()
    robot_group.takeoff().wait_for_completed()
    robot_group.go({0: [-120, -120, 100, 100, "m12"],
                    1: [0,  -120, 100, 100, "m12"],
                    2: [120, -120, 100, 100, "m12"],
                    3: [-120, 0, 100, 100, "m12"],
                    4: [0,  0, 100, 100, "m12"],
                    5: [120, 0, 100, 100, "m12"],
                    6: [-120, 120, 100, 100, "m12"],
                    7: [0,  120, 100, 100, "m12"]
                    }).wait_for_completed()
    robot_group.go({0: [-120, -120, 80, 70, "m12"],  # 1
                    1: [-40,  -120, 80, 70, "m12"],  # 2
                    2: [40, -120, 80, 70, "m12"],    # 3
                    3: [-60, 30, 125, 70, "m12"],    # 4
                    4: [0,  -60, 100, 70, "m12"],    # 5
                    5: [120, -120, 80, 70, "m12"],   # 6
                    6: [-120, 120, 150, 70, "m12"],  # 7
                    7: [60,  80, 125, 70, "m12"]    # 8
                    }).wait_for_completed()
    robot_group.land().wait_for_completed()
    robot_group.mission_pad_off()
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
    multi_drone.initialize(robot_num=8)
    multi_drone.number_id_by_sn(
        [0, robot_sn_list[0]], [1, robot_sn_list[1]], [2, robot_sn_list[2]],
        [3, robot_sn_list[3]], [4, robot_sn_list[4]], [5, robot_sn_list[5]],
        [6, robot_sn_list[6]], [7, robot_sn_list[7]])
    multi_drone_group1 = multi_drone.build_group([0, 1, 2, 3, 4, 5, 6, 7])
    multi_drone.run([multi_drone_group1, v_size_task])
    multi_drone.close()
