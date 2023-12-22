from scripts.max_height import run_max_height_script
from scripts.sensor_data import run_sensor_data_script
from scripts.average_velocity import run_average_velocity_script


if __name__ == "__main__":
    time, sensor_heights = run_sensor_data_script()
    max_heights = run_max_height_script()

    run_average_velocity_script(time, sensor_heights, max_heights)
