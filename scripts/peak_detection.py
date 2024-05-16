import numpy as np
from utils.constants import AverageVelocityConstants, BaseConstants

from utils.graph import GraphPlotter


class PeakDetector:
    def __init__(self, data, times, sensor_number, draw_graph=True) -> None:
        self.data = data
        self.times = times
        self.draw_graph = draw_graph
        self.sensor_number = sensor_number

        self.signals = None
        self.signal_times = None
        self.signal_peaks = None

    def thresholding(self, lag, threshold, influence):
        signals = np.zeros(len(self.data))
        filteredY = np.array(self.data)
        avgFilter = [0]*len(self.data)
        stdFilter = [0]*len(self.data)

        avgFilter[lag - 1] = np.mean(self.data[0:lag])
        stdFilter[lag - 1] = np.std(self.data[0:lag])
        for i in range(lag, len(self.data)):
            if abs(self.data[i] - avgFilter[i-1]) > threshold * stdFilter[i-1]:
                if self.data[i] > avgFilter[i-1]:
                    signals[i] = -1
                signals[i] = 1

                filteredY[i] = influence * self.data[i] + (1 - influence) * filteredY[i-1]
                avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
                stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
            else:
                signals[i] = 0
                filteredY[i] = self.data[i]
                avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
                stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])

        self.signals = signals
        self.set_signal_info()
        max_signal_time = self.get_longest_signal()
        if self.draw_graph:
            self.draw_signal_graph(signals)

        return max_signal_time

    def set_signal_info(self) -> None:
        x_values = []
        signal_peaks = []
        for index, signal in enumerate(self.signals):
            if index < len(self.signals) - 1:
                if self.signals[index + 1] - signal:
                    x_values.append(self.times[index+1])
                    signal_peaks.append(self.times[index+1])
                    print(f"signal peak: {self.times[index + 1]}")
                    continue
            x_values.append(self.times[index])

        self.signal_times, self.signal_peaks = x_values, signal_peaks

    def draw_signal_graph(self, signals):
        graph = GraphPlotter(
            "time",
            "signal",
            f"{self.sensor_number}.csv",
            f"results/signals/{BaseConstants.CSV_FILE.split('.csv')[0]}",
            min_x_axis=0,
            max_x_axis=140,
            min_y_axis=-2,
            max_y_axis=2,
            graph_title=self.sensor_number,
        )

        graph.plot(
            self.signal_times,
            signals,
            linestyle=AverageVelocityConstants.LINE_STYLE,
            save=True,
            grid=True,
        )

    def get_longest_signal(self):
        signal_pairs = []
        for index in range(0, len(self.signal_peaks), 2):
            if index < len(self.signal_peaks) - 1:
                difference = abs(self.signal_peaks[index] - self.signal_peaks[index + 1])
                signal_pairs.append((self.signal_peaks[index], self.signal_peaks[index + 1], difference))

        max_signal = max(signal_pairs, key=lambda x: x[2])
        return max_signal[0]
