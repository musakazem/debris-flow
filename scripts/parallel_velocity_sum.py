import numpy as np

from utils.graph import GraphPlotter
from utils.constants import ParallelVelocitySumConstants as constants


def run_parallel_velocity_script(velocities):
    parallel_velocity_sums = []

    for index, velocity in enumerate(velocities):
        if index + 1 < len(velocities):
            v2 = velocities[index + 1]
            parallel_velocity_sums.append(calculate_parallel_velocity_sum(velocity, v2))

    y_values = np.array(parallel_velocity_sums)
    x_values = np.array(constants.DISTANCES)
    average_parallel_velocity = np.round(np.mean(y_values), decimals=3)

    graph = GraphPlotter(
        constants.X_AXIS_LABEL,
        constants.Y_AXIS_LABEL,
        constants.CSV_FILE,
        "results/parallel_velocity_sum",
        min_x_axis=constants.MIN_X_AXIS,
        max_x_axis=constants.MAX_X_AXIS,
        min_y_axis=constants.MIN_Y_AXIS,
        max_y_axis=constants.MAX_Y_AXIS,
    )

    graph.plot(
        x_values,
        y_values,
        linestyle=constants.LINE_STYLE,
        h_line=average_parallel_velocity,
        h_line_configs=constants.H_MARK,
        marker_configs=constants.MARKER,
        x_ticks=constants.DISTANCES,
        grid=True,
    )


def calculate_parallel_velocity_sum(v1, v2):
    return (v1 * v2) / (v1 + v2)
