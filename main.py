from scripts.max_height import run_max_height_script
from scripts.parallel_velocity_sum import run_parallel_velocity_script
from scripts.sensor_data import run_sensor_data_script, run_tank_sensor_data_script
from scripts.average_velocity import (
    get_max_gradient_times,
    get_sensor_gradients,
    run_average_velocity_script,
)
from utils.constants import SensorDataConstants
from utils.logger import Logger


def get_gradient_calc_range(time, sensor_heights):
    gradients, truncated_time = get_sensor_gradients(
        time, sensor_heights, {"GRADIENT_MIN_X": 0, "GRADIENT_MAX_X": 140}
    )
    max_times = get_max_gradient_times(gradients, truncated_time)

    min_x = min(max_times)
    max_x = max(max_times)
    return {
        "GRADIENT_MIN_X": min_x[0] - SensorDataConstants().GRACE_RANGE,
        "GRADIENT_MAX_X": max_x[0] + SensorDataConstants().GRACE_RANGE,
    }


if __name__ == "__main__":
    run_tank_sensor_data_script()

    time, sensor_heights = run_sensor_data_script()

    minimal_time_data, minimal_sensor_data = run_sensor_data_script(
        10, 200, save_graph=False
    )
    gradient_calc_range = get_gradient_calc_range(
        minimal_time_data, minimal_sensor_data
    )

    Logger().log(f"Gradient reading range: {gradient_calc_range}")

    max_heights = run_max_height_script()
    velocity = run_average_velocity_script(time, sensor_heights, gradient_calc_range)

    run_parallel_velocity_script(velocity)
