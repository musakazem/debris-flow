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

        self.plot_methods = []

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
        marker_configs={},
        x_ticks=[],
        save=True,
        **kwargs,
    ):
        if not save:
            return

        plt.plot(x_values, y_values, label=label, linestyle=linestyle, **marker_configs, **kwargs)
        plt.axis([self.min_x_axis, self.max_x_axis, self.min_y_axis, self.max_y_axis])
        plt.title(self.title)

        if h_line:
            self.plot_horizontal_line(h_line, h_line_configs)

        if x_ticks:
            plt.xticks(x_ticks)

        if label:
            plt.legend()

        plt.savefig(f"{self.dir}/{self.formatted_file_name}.png")

    def get_formatted_file_name(self, file_name):
        components = file_name.split(".")
        return (
            f"{components[0]}.{components[1]}" if len(components) > 2 else components[0]
        )

    def plot_horizontal_line(self, h_line, h_line_configs):
        plt.axhline(y=h_line, **h_line_configs["main"])
        text_pos_x = self.min_x_axis + h_line_configs["extra"].get("text_pos_x", 0)
        text_pos_y = h_line + h_line_configs["extra"].get("text_pos_y", 0)
        plt.text(
            text_pos_x,
            text_pos_y,
            f"v={h_line}",
            color="r",
            va="bottom",
            ha="left",
        )

    @property
    def title(self):
        file_name_components = self.formatted_file_name.split("_")
        re_pattern = r"(\d*\.?\d*)"
        soil_type = file_name_components[2]
        water_content = re.findall(re_pattern, file_name_components[0])[1]
        slope = re.findall(re_pattern, file_name_components[1])[1]
        return f"W={water_content}%, S={slope}%, {soil_type} material"
