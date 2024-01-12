import numpy as np

from utils.data import DataManager
from utils.graph import GraphPlotter
from utils.constants import SensorDataConstants, TankSensorConstants
from utils.logger import Logger


def get_average_initial_depth(data):
    transposed_data = np.transpose(data[: SensorDataConstants.INITIAL_DEPTH])
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
    location = f"{SensorDataConstants.FILE_ROOT}/{SensorDataConstants.CSV_FILE}"
    data_manager = DataManager(
        location,
        SensorDataConstants.USE_COLUMNS,
        SensorDataConstants.READ_ROWS,
        skip_header=SensorDataConstants.SKIP_HEADER,
    )

    data = data_manager.get_data(SensorDataConstants.AVERAGE_DEPTH)
    Logger().log_raw_data(data)
    Logger().log_data_points(data)

    time = [datum[0] for datum in data]
    sensor_data = np.delete(data, 0, axis=1)
    transposed_data = np.transpose(sensor_data)
    initial_depths = get_average_initial_depth(sensor_data)

    sensor_y_coordinates = []
    for sensor_number in range(len(transposed_data)):
        sensor_datum = [
            initial_depths[sensor_number] - datum[sensor_number]
            for datum in sensor_data
        ]
        sensor_y_coordinates.append(sensor_datum)

    max_height_coordinates = get_max_heights(
        np.array(sensor_y_coordinates)
    )  # TODO: This probably should'nt be here
    Logger().log_max_height(max_height_coordinates)
    graph = GraphPlotter(
        SensorDataConstants.X_AXIS_LABEL,
        SensorDataConstants.Y_AXIS_LABEL,
        location.split("/")[1],
        min_x_axis=SensorDataConstants.MIN_X_AXIS,
        max_x_axis=SensorDataConstants.MAX_X_AXIS,
        min_y_axis=SensorDataConstants.MIN_Y_AXIS,
        max_y_axis=SensorDataConstants.MAX_Y_AXIS,
    )

    sensor_counter = 1
    for sensor_datum in sensor_y_coordinates:
        graph.plot(
            time,
            sensor_datum,
            f"Sensor {sensor_counter}",
            save=SensorDataConstants.SAVE_GRAPH,
            # x_ticks=SensorDataConstants.DISTANCES,
            grid=True,
        )
        sensor_counter += 1

    data_manager.save_data(
        data=max_height_coordinates,
        path=f"{SensorDataConstants.FILE_ROOT}/max_height/{SensorDataConstants.CSV_FILE}",
    )

    return time, sensor_y_coordinates


def run_tank_sensor_data_script():
    location = f"{SensorDataConstants.FILE_ROOT}/{SensorDataConstants.CSV_FILE}"
    data_manager = DataManager(
        location,
        TankSensorConstants.USE_COLUMNS,
        TankSensorConstants.READ_ROWS,
        skip_header=TankSensorConstants.SKIP_HEADER,
    )
    data = data_manager.get_data(TankSensorConstants.AVERAGE_DEPTH)

    time = [datum[0] for datum in data]
    sensor_data = np.delete(data, 0, axis=1)
    initial_depths = get_average_initial_depth(sensor_data)

    sensor_data = [initial_depths[0] - datum[0] for datum in sensor_data]

    graph = GraphPlotter(
        TankSensorConstants.X_AXIS_LABEL,
        TankSensorConstants.Y_AXIS_LABEL,
        location.split("/")[1],
        "results/tank_data",
        min_x_axis=TankSensorConstants.MIN_X_AXIS,
        max_x_axis=TankSensorConstants.MAX_X_AXIS,
        min_y_axis=TankSensorConstants.MIN_Y_AXIS,
        max_y_axis=TankSensorConstants.MAX_Y_AXIS,
    )

    graph.plot(
        time,
        sensor_data,
        save=TankSensorConstants.SAVE_GRAPH,
        # x_ticks=TankSensorConstants.DISTANCES,
        grid=True,
    )
