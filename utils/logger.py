from utils.constants import Constants


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
    def log_initial_depth_variance(*args):
        print("----------")
        print(f"Initial depth value: {Constants.INITIAL_DEPTH}")
        print("Sensor data variance:")
        [print(sensor_var) for sensor_var in args]
        print("----------")
