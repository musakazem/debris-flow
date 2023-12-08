import numpy as np

from utils.data import DataReader
from utils.graph import GraphPlotter
from utils.constants import Constants
from utils.logger import Logger


def get_average_initial_depth(data, transposed_data):
    sensor1_var = np.var(transposed_data[0])
    sensor2_var = np.var(transposed_data[1])
    Logger().log_initial_depth_variance(sensor1_var, sensor2_var)

    data_chunk_average = []
    for datum in transposed_data:
        data_chunk_average.append(np.average(datum))

    return data_chunk_average


if __name__ == "__main__":

    location = Constants.CSV_FILE
    data_reader = DataReader(location, Constants.USE_COLUMNS, Constants.READ_ROWS, skip_header=Constants.SKIP_HEADER)
    data, initial_data = data_reader.get_data(Constants.AVERAGE_DEPTH)
    Logger().log_data_points(data=data)

    time = [datum[0] for datum in data]
    sensor_data = np.delete(data, 0, axis=1)

    transposed_data = np.transpose(sensor_data[:Constants.INITIAL_DEPTH])
    initial_depths = get_average_initial_depth(sensor_data, transposed_data)

    sensor_y_coordinates = []
    for sensor_number in range(len(transposed_data) - 1):
        sensor_datum = [initial_depths[sensor_number] - datum[sensor_number] for datum in sensor_data]
        sensor_y_coordinates.append(sensor_datum)

    graph = GraphPlotter(Constants.X_AXIS_LABEL, Constants.Y_AXIS_LABEL, location.split("/")[1])

    sensor_counter = 1
    for sensor_datum in sensor_y_coordinates:
        graph.plot(time, sensor_datum, f"Sensor {sensor_counter}")
        sensor_counter += 1

    Logger().log_raw_data(data)
