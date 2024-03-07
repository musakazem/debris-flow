import numpy as np

from utils.constants import MaxHeightConstants
from utils.data import DataManager
from utils.graph import GraphPlotter


def run_max_height_script():
    location = (
        f"{MaxHeightConstants.FILE_ROOT}/max_height/{MaxHeightConstants.CSV_FILE}"
    )
    data_manager = DataManager(
        location,
        MaxHeightConstants.USE_COLUMNS,
        MaxHeightConstants.READ_ROWS,
        metre_conversion=False,
    )

    data = data_manager.get_data()
    graph = GraphPlotter(
        MaxHeightConstants.X_AXIS_LABEL,
        MaxHeightConstants.Y_AXIS_LABEL,
        MaxHeightConstants.CSV_FILE,
        "results/max_height",
        min_x_axis=MaxHeightConstants.MIN_X_AXIS,
        max_x_axis=MaxHeightConstants.MAX_X_AXIS,
        min_y_axis=MaxHeightConstants.MIN_Y_AXIS,
        max_y_axis=MaxHeightConstants.MAX_Y_AXIS,
    )
    average_height = np.round(np.mean(data), decimals=3)
    x_coordinates = np.array(MaxHeightConstants.DISTANCES)
    graph.plot(
        x_coordinates,
        data,
        linestyle=MaxHeightConstants.LINE_STYLE,
        h_line=average_height,
        h_line_configs=MaxHeightConstants.H_MARK,
        marker_configs=MaxHeightConstants.MARKER,
        x_ticks=MaxHeightConstants.DISTANCES,
        grid=True,
    )

    return data
