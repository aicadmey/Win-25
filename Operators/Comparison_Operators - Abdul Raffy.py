#  1. Comparison Operators (==, !=, <, >, <=, >=)
# A Bit based on robotics

''' == '''

robot_speed, max_speed = 5, 5
print(robot_speed == max_speed)  

ai_model1, ai_model2 = 'Jarvis', 'BayMax'
print(ai_model1 == ai_model2)  

sensor_value1, sensor_value2 = 3.14, 2.71
print(sensor_value1 == sensor_value2)  

path1, path2 = [1, 0, 1], [1, 0, 1]
print(path1 == path2)  

mode1, mode2 = True, False 
print(mode1 == mode2)  

''' != '''

robot1_id, robot2_id = 101, 102
print(robot1_id != robot2_id)  

order_1, order_2 = 'ABCDE', 'ABCDE'
print(order_1 != order_2)  

battery_level1, battery_level2 = 80, 75
print(battery_level1 != battery_level2)  

robot1_path, robot2_path = [1, 0, 1], [1, 0, 0]
print(robot1_path != robot2_path)  

charged1, charged2 = True,True 
print(charged1 != charged2)  

''' < '''

current_speed, max_speed = 10, 20
print(current_speed < max_speed)  

scan_accuracy, target_accuracy = 90.5, 85.0
print(scan_accuracy < target_accuracy)  

sensor1, sensor2 = 4.5, 4.5
print(sensor1 < sensor2)  

robot1_distance, robot2_distance = 100, 200
print(robot1_distance < robot2_distance)  

minimum, max_temp = 10, 30
print(minimum < max_temp)  

''' > '''

robot1_speed, robot2_speed = 15, 10
print(robot1_speed > robot2_speed)  

processing_time1, processing_time2 = 3, 5
print(processing_time1 > processing_time2)  

battery_level1, battery_level2 = 80, 95
print(battery_level1 > battery_level2)  

robot_range1, robot_range2 = 500, 300
print(robot_range1 > robot_range2)  

score1, score2 = 85, 90
print(score1 > score2)  

''' <= '''

robot_weight, max_weight = 10, 10
print(robot_weight <= max_weight)  

cost1, cost2 = 80, 75
print(cost1 <= cost2)  

training_time1, training_time2 = 6, 10
print(training_time1 <= training_time2)  

safe_temparature, max_temparature = 45, 40
print(safe_temparature <= max_temparature)  

sensor_limit, sensor_max = 3, 5
print(sensor_limit <= sensor_max)  

''' >= '''

robot_uptime, min_uptime = 24, 24
print(robot_uptime >= min_uptime)  

ai_version1, ai_version2 = '3.2', '3.5'
print(ai_version1 >= ai_version2)  

training_accuracy, required_accuracy = 90, 95
print(training_accuracy >= required_accuracy)  

robot_battery1, robot_battery2 = 50, 40
print(robot_battery1 >= robot_battery2)  

current_fps, max_fps = 30, 60
print(current_fps >= max_fps)  


