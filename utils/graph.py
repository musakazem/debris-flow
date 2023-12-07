import matplotlib.pyplot as plt


class GraphPlotter:
    def __init__(self, x_label, y_label, file_name, x_scale=30, y_scale=6):
        plt.figure(figsize=(x_scale, y_scale))
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        self.file_name = file_name.split(".")[0]

    def plot_graph(self, x_values, y_values, label):
        plt.plot(x_values, y_values, label=label)
        plt.legend()
        plt.savefig(f"results/{self.file_name}")
