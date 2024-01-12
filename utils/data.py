import numpy as np


class DataManager:
    def __init__(
        self, path, columns, max_rows=1000, skip_header=0, metre_conversion=True
    ):
        self.path = path
        self.columns = columns
        self.max_rows = max_rows
        self.skip_header = skip_header
        self.metre_conversion = metre_conversion

    def get_data(self, avg_depth=None):
        data = self.read_data()

        if self.metre_conversion:
            data = self.convert_to_metre(data)

        if not avg_depth:
            return data

        return self.average_data(data, avg_depth)

    def read_data(self):
        return np.genfromtxt(
            self.path,
            delimiter=",",
            skip_header=self.skip_header,
            max_rows=self.max_rows,
            usecols=self.columns,
        )

    def save_data(self, data, path, header="", delimiter=","):
        np.savetxt(path, data, delimiter=",", header=header)

    @staticmethod
    def average_data(data, avg_depth):
        total_average = []

        for i in range(0, len(data), avg_depth):
            chunk = data[i: i + avg_depth]
            chunk_avg = np.mean(chunk, axis=0)
            total_average.append(chunk_avg)

        return np.array(total_average)

    @staticmethod
    def convert_to_metre(data):
        modified_data = data / 1000

        try:  # TODO: Find a solution for this!!
            modified_data[:, 0] = data[:, 0]
        except Exception:
            pass

        return modified_data
