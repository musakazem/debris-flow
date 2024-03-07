import numpy as np
from utils.constants import SensorDataConstants
from datetime import datetime


class Logger:
    @staticmethod
    def log_raw_data(data):
        print("----------")
        print(data)
        print("----------")

    @staticmethod
    def log_data_points(data, *args, **kwargs):
        print("----------")
        print(f"Total data points: {len(data)}")
        print("----------")

    @staticmethod
    def log_initial_depth_variance(transposed_data, *args):
        print("----------")
        print(f"Initial depth value: {SensorDataConstants.INITIAL_DEPTH}")
        print("Sensor data variance:")
        sensor_vars = [np.var(transposed_data[i]) for i in range(len(transposed_data))]
        [print(sensor_var) for sensor_var in sensor_vars]
        print("----------")

    @staticmethod
    def log_max_height(max_heights):
        print("----------")
        print("Max heights:")
        for max_height in max_heights:
            print(f"x: {max_height[0]}, y: {max_height[1]}")
        print("----------")

    @staticmethod
    def log_max_gradient_values(time_deltas):
        print("----------")
        print("Max gradients:")
        for time_delta in time_deltas:
            print(f"time: {time_delta[0]}, gradient: {time_delta[1]}")
        print("----------")

    @staticmethod
    def log_velocity_time_data(velocity, time):
        print("----------")
        print("Velocity and delta time:")
        for v, t in zip(velocity, time):
            print(f"velocity: {v}, time: {t}")
        print("----------")

    @staticmethod
    def log_exception(exception):
        print("xxxxxxxxxxxx")
        print(f"Failed to run script: {exception}")

    @staticmethod
    def log(message):
        indicator = "--------->"
        print(f"{indicator}{datetime.now()} - {message}")
