import re
import matplotlib.pyplot as plt


class GraphPlotter:
    def __init__(
            self,
            x_label,
            y_label,
            file_name,
            dir=None,
            x_size=30,
            y_size=6,
            min_x_axis=1,
            max_x_axis=1,
            min_y_axis=1,
            max_y_axis=1,
    ):
        plt.figure(figsize=(x_size, y_size))
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        self.formatted_file_name = self.get_formatted_file_name(file_name)
        self.dir = dir if dir else "results"

        self.min_x_axis = min_x_axis
        self.min_y_axis = min_y_axis
        self.max_x_axis = max_x_axis
        self.max_y_axis = max_y_axis

    def plot(
            self,
            x_values,
            y_values,
            label=None,
            linestyle=None,
            h_line=None,
            h_line_configs={},
            **kwargs
    ):
        plt.plot(x_values, y_values, label=label, linestyle=linestyle, **kwargs)
        plt.axis([self.min_x_axis, self.max_x_axis, self.min_y_axis, self.max_y_axis])
        plt.title(self.title)

        if h_line:
            plt.axhline(y=h_line, **h_line_configs)
            plt.text(self.min_x_axis + .1, h_line + .1, f'v={h_line}', color='r', va='bottom', ha='left')
        if label:
            plt.legend()

        plt.savefig(f"{self.dir}/{self.formatted_file_name}.png")

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
