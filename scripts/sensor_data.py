import numpy as np

from utils.data import DataManager
from utils.graph import GraphPlotter
from utils.constants import Constants
from utils.logger import Logger


def get_average_initial_depth(data):
    transposed_data = np.transpose(data[:Constants.INITIAL_DEPTH])
    Logger().log_initial_depth_variance(transposed_data)

    data_chunk_average = []
    for datum in transposed_data:
        data_chunk_average.append(np.average(datum))

    return data_chunk_average


def get_max_heights(h_values):
    max_values = []
    for data in h_values:
        max_height = np.max(data)
        max_height_indx = np.argmax(data)
        max_values.append([max_height_indx, max_height])
    return max_values


def run_sensor_data_script():
    location = f"{Constants.FILE_ROOT}/{Constants.CSV_FILE}"
    data_manager = DataManager(location, Constants.USE_COLUMNS, Constants.READ_ROWS, skip_header=Constants.SKIP_HEADER)
    data = data_manager.get_data(Constants.AVERAGE_DEPTH)
    Logger().log_raw_data(data)
    Logger().log_data_points(data)

    time = [datum[0] for datum in data]
    sensor_data = np.delete(data, 0, axis=1)

    transposed_data = np.transpose(sensor_data)
    initial_depths = get_average_initial_depth(sensor_data)

    sensor_y_coordinates = []
    for sensor_number in range(len(transposed_data) - 1):
        sensor_datum = [initial_depths[sensor_number] - datum[sensor_number] for datum in sensor_data]
        sensor_y_coordinates.append(sensor_datum)

    max_height_coordinates = get_max_heights(np.array(sensor_y_coordinates))
    Logger().log_max_height(max_height_coordinates)
    graph = GraphPlotter(Constants.X_AXIS_LABEL, Constants.Y_AXIS_LABEL, location.split("/")[1])

    sensor_counter = 1
    for sensor_datum in sensor_y_coordinates:
        graph.plot(time, sensor_datum, f"Sensor {sensor_counter}")
        sensor_counter += 1

    data_manager.save_data(data=max_height_coordinates, path=f"{Constants.FILE_ROOT}/max_height/{Constants.CSV_FILE}")
