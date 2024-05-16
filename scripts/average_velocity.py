import numpy as np

from typing import List

from utils.constants import AverageVelocityConstants

from utils.graph import GraphPlotter
from utils.logger import Logger


def run_average_velocity_script(max_times: List):
    delta_times = []
    for index, time in enumerate(max_times):
        if index + 1 < len(max_times):
            next_value = max_times[index + 1]
            delta_times.append(next_value - time)

    delta_x = []
    for i, x in enumerate(AverageVelocityConstants.DISTANCES):
        if i + 1 < len(AverageVelocityConstants.DISTANCES):
            next_value = AverageVelocityConstants.DISTANCES[i + 1]
            value = next_value - x
            delta_x.append(value)

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
        x_ticks=AverageVelocityConstants.DISTANCES,
        grid=True,
    )

    return velocity
