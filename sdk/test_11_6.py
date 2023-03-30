import time
from multi_robomaster import multi_robot


def v_size_task(robot_group):

    show_logo_up = '000rr00000rrrr000rrrrrr0rrrrrrrr00rrrr0000rrrr0000rrrr0000rrrr00'
    show_logo_down = '00rrrr0000rrrr0000rrrr0000rrrr00rrrrrrrr0rrrrrr000rrrr00000rr000'
    show_logo_zhong = '0000r0000000r0000rrrrrrr0r00r00r0rrrrrrr0000r0000000r0000000r000'
    show_logo_guo = '0rrrrrrr0r00000r0r0rrr0r0r00r00r0r0rrr0r0r00r0rr0r0rrrrr0rrrrrrr'
    show_logo_v = '0r00000r0r00000r0r00000r0r00000r0r00000r00r000r0000r0r000000r000'
    show_logo_gu = '0000000000r0r0r00r00r00r000r0r0000r000r00r0rrr0r000r0r00000rrr00'
    show_logo_ma = '0pprrrr000r000r000r000r000rrrrrr0000000r0rrrrr0r0000000r0000rrrr'
    show_logo_lan = '0r00r00r0r000rr0rrr0rrrrrrr00000rrr00rr00r0000000r0rrrrr00000000'
    show_logo_shan = '0000r0000000r0000000r0000r00r00r0r00r00r0r00r00r0rrrrrrr00000000'
    show_logo_love = '0000000000r00r000rrrrrr0rrrrrrrr0rrrrrr000rrrr00000rr00000000000'
    show_logo_wen = '0000r0000000r0000rrrrrrr00r000r0000r0r000000r000000r0r0000r000r0'
    show_logo_chuan = '00r0000r0rrr000rrr0rr00r0rrr0r0r0r0r0r0r0rrr0r0r0r00r0rr0rrrr0rr'
    show_logo_yuan = '0rrrrrrr0r0rrr0r0r00000r0rrrrrrr0r0r0r0r0r0r0r0r0rrr0rrr0rrrrrrr'
    mled_smile1 = '000000000r0000r0r0r00r0r000000000000000000r00r00000rr00000000000'
    mled_smile2 = '00rrrr000r0000r0r0r00r0rr000000rr0r00r0rr00rr00r0r0000r000rrrr00'

    #robot_group.set_led([0, 255, 0])
    # 呼吸灯效果
    robot_group.set_led_breath(command_dict={0: [1.5, 255, 0, 0], 1: [1.5, 255, 0, 0], 2: [
                               1.5, 255, 0, 0], 3: [1.5, 255, 0, 0], 4: [1.5, 255, 0, 0]})

    robot_group.set_mled_bright(64)
    # robot_group.set_mled_graph(show_logo_up)
    robot_group.set_mled_graph_scroll('u', 1.5, show_logo_up)
    robot_group.mission_pad_on()
    robot_group.motor_on().wait_for_completed()
    robot_group.takeoff().wait_for_completed()

    robot_group.set_led_breath(command_dict={0: [1.5, 0, 255, 0], 1: [1.5, 0, 255, 0], 2: [
                               1.5, 0, 255, 0], 3: [1.5, 0, 255, 0], 4: [1.5, 0, 255, 0]})

    robot_group.set_mled_graph(command_dict={
        0: [show_logo_zhong], 1: [show_logo_guo], 2: [show_logo_love],
        3: [show_logo_v], 4: [show_logo_gu]})
    robot_group.go({0: [-120, 0, 100, 100, "m12"],   # 1
                    1: [-60,  0, 100, 100, "m12"],   # 2
                    2: [0, 0, 100, 100, "m12"],      # 3
                    3: [60, 0, 100, 100, "m12"],     # 4
                    4: [120,  0, 100, 100, "m12"],   # 5
                    }).wait_for_completed()
    time.sleep(1)
    robot_group.set_mled_graph(command_dict={
        0: [show_logo_zhong], 1: [show_logo_guo], 2: [show_logo_love],
        3: [show_logo_v], 4: [show_logo_gu]})
    # 显示V
    robot_group.go({0: [-120, 120, 160, 70, "m12"],   # 1
                    1: [-60,  30, 125, 70, "m12"],    # 2
                    2: [0, -60, 75, 70, "m12"],       # 3
                    3: [60, 30, 125, 70, "m12"],      # 4
                    4: [120,  120, 175, 70, "m12"],   # 5
                    }).wait_for_completed()
    time.sleep(3)
    robot_group.set_mled_graph(command_dict={
        0: [show_logo_ma], 1: [show_logo_lan], 2: [show_logo_love],
        3: [show_logo_v], 4: [show_logo_shan]})
    # 显示T
    robot_group.go({0: [-90, 120, 160, 70, "m12"],   # 1
                    1: [0,  120, 160, 70, "m12"],    # 2
                    2: [0, -60, 100, 70, "m12"],     # 3
                    3: [0, 30, 130, 70, "m12"],      # 4
                    4: [90,  120, 160, 70, "m12"],   # 5
                    }).wait_for_completed()
    time.sleep(3)
    robot_group.set_mled_graph(command_dict={
        0: [show_logo_zhong], 1: [show_logo_guo], 2: [show_logo_love],
        3: [show_logo_v], 4: [show_logo_gu]})
    # 显示V
    robot_group.go({0: [-120, 120, 175, 70, "m12"],   # 1
                    1: [-60,  30, 125, 70, "m12"],    # 2
                    2: [0, -60, 75, 70, "m12"],       # 3
                    3: [60, 30, 125, 70, "m12"],      # 4
                    4: [120,  120, 175, 70, "m12"],   # 5
                    }).wait_for_completed()
    time.sleep(3)
    robot_group.set_mled_char(command_dict={0: ['p', 'D'], 1: ['p', 'J'], 2: [
                              'p', 'I'], 3: ['b', 'T'], 4: ['b', 'T']})
    robot_group.go({0: [-120, 0, 100, 100, "m12"],   # 1
                    1: [-60,  0, 100, 100, "m12"],   # 2
                    2: [0, 0, 100, 100, "m12"],      # 3
                    3: [60, 0, 100, 100, "m12"],     # 4
                    4: [120,  0, 100, 100, "m12"],   # 5
                    }).wait_for_completed()
    time.sleep(3)
    robot_group.set_mled_graph_scroll('d', 1.5, show_logo_down)
    # robot_group.set_mled_graph(show_logo_down)
    robot_group.land().wait_for_completed()
    robot_group.mission_pad_off()
    robot_group.motor_off().wait_for_completed()

    robot_group.set_mled_bright(0)
    robot_group.set_led_breath(command_dict={0: [1.5, 0, 0, 255], 1: [1.5, 0, 0, 255], 2: [
        1.5, 0, 0, 255], 3: [1.5, 0, 0, 255], 4: [1.5, 0, 0, 255]})


# | 新机1    | 0TQZH97CNT04AH |
# | 新机2    | 0TQZH79ED00HA3 |
# | 新机3    | 0TQZH97CNT046V |
# | 新机4    | 0TQZH97CNT0407 |
# | 新机5    | 0TQZHAGCNT0766 |
# | 新机6    | 0TQZHAGCNT0708 |
# | 新机7    | 0TQZHAFCNT060W |
# | 新机8    | 0TQZHAGCNT074V |
if __name__ == '__main__':
    robot_sn_list = ["0TQZH97CNT0407",
                     "0TQZHAGCNT0766",
                     "0TQZHAGCNT0708",
                     "0TQZHAFCNT060W",
                     "0TQZHAGCNT074V"]
    multi_drone = multi_robot.MultiDrone()
    multi_drone.initialize(robot_num=5)
    multi_drone.number_id_by_sn(
        [0, robot_sn_list[0]], [1, robot_sn_list[1]], [2, robot_sn_list[2]],
        [3, robot_sn_list[3]], [4, robot_sn_list[4]])
    multi_drone_group1 = multi_drone.build_group([0, 1, 2, 3, 4])
    multi_drone.run([multi_drone_group1, v_size_task])
    multi_drone.close()
