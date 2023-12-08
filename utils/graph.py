import re
import matplotlib.pyplot as plt

from utils.constants import Constants


class GraphPlotter:
    def __init__(self, x_label, y_label, file_name, x_scale=30, y_scale=6):
        plt.figure(figsize=(x_scale, y_scale))
        plt.ylabel(y_label)
        plt.xlabel(x_label)

        self.formatted_file_name = self.get_formatted_file_name(file_name)

    def plot(self, x_values, y_values, label):
        plt.plot(x_values, y_values, label=label)
        plt.axis([Constants.MIN_X_AXIS, Constants.MAX_X_AXIS, Constants.MIN_Y_AXIS, Constants.MAX_Y_AXIS])
        plt.title(self.title)
        # plt.figtext(0, 0.1, "This is a test log", color="r", fontsize="large")
        plt.legend()
        plt.savefig(f"results/{self.formatted_file_name}.png")

    def get_formatted_file_name(self, file_name):
        components = file_name.split(".")
        return f"{components[0]}.{components[1]}" if len(components) > 2 else components[0]

    @property
    def title(self):
        file_name_components = self.formatted_file_name.split("_")
        re_pattern = r"(\d*\.?\d*)"
        soil_type = file_name_components[2]
        water_content = re.findall(re_pattern, file_name_components[0])[1]
        slope = re.findall(re_pattern, file_name_components[1])[1]
        return f"W={water_content}%, S={slope}%, {soil_type} material"
