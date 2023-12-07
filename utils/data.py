import numpy as np


class DataReader:

    def __init__(self, path, columns, max_rows=1000, skip_header=1) -> None:
        self.path = path
        self.columns = columns
        self.max_rows = max_rows
        self.skip_header = skip_header

    def get_data(self, avg_depth=None):
        data = self.convert_to_metre(self.read_data())
        initial_data = data[0]
        if not avg_depth:
            return data, initial_data

        return self.average_data(data, avg_depth), initial_data

    def read_data(self):
        return np.genfromtxt(
            self.path,
            delimiter=',',
            skip_header=self.skip_header,
            max_rows=self.max_rows,
            usecols=self.columns,
        )

    @staticmethod
    def average_data(data, avg_depth):
        total_average = []

        for i in range(0, len(data), avg_depth):
            chunk = data[i:i+avg_depth]
            chunk_avg = np.mean(chunk, axis=0)
            total_average.append(chunk_avg)

        return np.array(total_average)

    @staticmethod
    def convert_to_metre(data):
        return data / 1000
