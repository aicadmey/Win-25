# 2. Logical Operators (AND, OR, NOT)

# 1 with and

robot_online, battery_charged = True, True
print(robot_online and battery_charged)  

ai_training, data_available = True, False
print(ai_training and data_available)  

sensor_active, hardware_ready = False, True
print(sensor_active and hardware_ready)  

network_connected, server_operational = True, True
print(network_connected and server_operational)

obstacle_detected, stop_signal = True, False
print(obstacle_detected and stop_signal)  

# 2 with or

robot_connected, fallback_mode = False, True
print(robot_connected or fallback_mode)

training, data_loaded = False, False
print(training or data_loaded)  

sensor_fault, maintenance = True, False
print(sensor_fault or maintenance) 

path_clear, low_battery = True, True
print(path_clear or low_battery) 

critical_error, restart_required = False, False
print(critical_error or restart_required)  

# 3 with not

robot_active = True
print(not robot_active)  

path_blocked = False
print(not path_blocked)

battery_low = True
print(not battery_low)  

ai_model = False
print(not ai_model)
 
maintenance_mode = True
print(not maintenance_mode)  
