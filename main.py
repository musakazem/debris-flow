from scripts.max_height import run_max_height_script
from scripts.parallel_velocity_sum import run_parallel_velocity_script
from scripts.peak_detection import PeakDetector
from scripts.sensor_data import run_sensor_data_script, run_tank_sensor_data_script
from scripts.average_velocity import (
    run_average_velocity_script,
)


if __name__ == "__main__":
    run_tank_sensor_data_script()

    time, sensor_heights = run_sensor_data_script()

    peak_times = []
    for index, sensor_data in enumerate(sensor_heights):
        sensor_number = f"sensor_{index + 1}"
        peak_time = PeakDetector(sensor_data, time, sensor_number).thresholding(550, 4, 0.7)
        peak_times.append(peak_time)

    max_heights = run_max_height_script()
    velocities = run_average_velocity_script(peak_times)
    run_parallel_velocity_script(velocities)
