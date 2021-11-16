while True:
    offset = color_sensor_in1.reflected_light_intensity - 50
    steering_drive.on(offset * 2, 20)
