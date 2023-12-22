import numpy as np

from utils.constants import AverageVelocityConstants
from utils.graph import GraphPlotter
from utils.logger import Logger


def run_average_velocity_script(time, sensor_heights, max_heights):
    gradients, truncated_time = get_sensor_gradients(time, sensor_heights)
    max_times = get_max_gradient_times(gradients, truncated_time)

    delta_times = []
    for i, t in enumerate(max_times):
        if i + 1 < len(max_times):
            next_value = max_times[i + 1]
            delta_times.append(next_value[0] - t[0])

    delta_x = []
    for i, x in enumerate(AverageVelocityConstants.DISTANCES):
        if i + 1 < len(AverageVelocityConstants.DISTANCES):
            next_value = AverageVelocityConstants.DISTANCES[i + 1]
            value = next_value - x
            delta_x.append(value)
    Logger().log_max_gradient_values(max_times)

    graph = GraphPlotter(
        AverageVelocityConstants.X_AXIS_LABEL,
        AverageVelocityConstants.Y_AXIS_LABEL,
        AverageVelocityConstants.CSV_FILE,
        "results/average_velocity",
        min_x_axis=AverageVelocityConstants.MIN_X_AXIS,
        max_x_axis=AverageVelocityConstants.MAX_X_AXIS,
        min_y_axis=AverageVelocityConstants.MIN_Y_AXIS,
        max_y_axis=AverageVelocityConstants.MAX_Y_AXIS,
    )

    velocity = np.array(delta_x) / np.array(delta_times)
    x_coordinates = np.array(AverageVelocityConstants.DISTANCES[1:])
    average_velocity = np.round(np.mean(velocity), decimals=3)
    Logger().log_velocity_time_data(velocity, delta_times)
    graph.plot(
        x_coordinates,
        velocity,
        linestyle=AverageVelocityConstants.LINE_STYLE,
        h_line=average_velocity,
        h_line_configs=AverageVelocityConstants.H_MARK,
        marker_configs=AverageVelocityConstants.MARKER,
        x_ticks=AverageVelocityConstants.DISTANCES
    )


def get_max_gradient_times(gradients, time):
    max_gradients = []
    for gradient in gradients:
        max_gradient = np.max(gradient)
        max_gradient_indx = np.argmax(gradient)
        max_gradients.append([time[max_gradient_indx], max_gradient])
    return max_gradients


def get_sensor_gradients(time, sensor_heights):
    gradients = []
    truncated_times = []
    for sensor in sensor_heights:
        time_sensor_data = np.column_stack((time, sensor))
        sensor_gradients = []
        truncated_time = []
        for index, time_sensor_datum in enumerate(time_sensor_data):
            if (
                time_sensor_datum[0] < AverageVelocityConstants.GRADIENT_MIN_X
                or time_sensor_datum[0] > AverageVelocityConstants.GRADIENT_MAX_X
            ):
                continue
            truncated_time.append(time_sensor_datum[0])
            try:
                next_datum = time_sensor_data[index + 1]
            except Exception:
                break
            gradient = slope(time_sensor_datum, next_datum)
            sensor_gradients.append(gradient)
        gradients.append(sensor_gradients)

        if not truncated_times:
            truncated_times.extend(truncated_time)

    return gradients, truncated_times


def slope(point_a, point_b):
    return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
