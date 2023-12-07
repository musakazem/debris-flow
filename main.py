import numpy as np

from utils.data import DataReader
from utils.graph import GraphPlotter
from utils.constants import Constants


def get_average_initial_depth(data, initial_data):
    transposed_data = np.transpose(data[:10])
    # sensor1_range = np.ptp(transposed_data[0])
    # sensor2_range = np.ptp(transposed_data[1])
    # sensor1_var = np.var(transposed_data[0])
    # sensor2_var = np.var(transposed_data[1])
    # log_data_points(None, sensor1_range, sensor2_range, sensor1_var, sensor2_var)
    data_chunk_average = []
    for datum in transposed_data:
        data_chunk_average.append(np.average(datum))

    return data_chunk_average


def log_data_points(data, *args, **kwargs):
    # print("----------")
    # print(f"Total data points: {len(data)}")
    # print("----------")

    for val in kwargs.values():
        print("----------")
        print(f"{val}: {val}")
        print("----------")


if __name__ == "__main__":

    file_name = Constants.CSV_FILE
    data_reader = DataReader(file_name, Constants.USE_COLUMNS, Constants.READ_ROWS, skip_header=Constants.SKIP_HEADER)
    data, initial_data = data_reader.get_data(Constants.AVERAGE_DEPTH)

    # log_data_points(data=data)

    time = [datum[0] for datum in data]
    sensor_data = np.delete(data, 0, axis=1)
    initial_depths = get_average_initial_depth(sensor_data, initial_data)  # TODO: Take the average of the first 1000 rows as average for EACH column

    sensor_y_coordinates = []
    for sensor_number in range(0, 9):
        sensor_datum = [initial_depths[sensor_number] - datum[sensor_number] for datum in sensor_data]
        sensor_y_coordinates.append(sensor_datum)
    graph = GraphPlotter(Constants.X_AXIS_LABEL, Constants.Y_AXIS_LABEL, file_name)
    counter = 1
    for sensor_datum in sensor_y_coordinates:
        graph.plot_graph(time, sensor_datum, f"Sensor {counter}")
        counter += 1

    print(data)
