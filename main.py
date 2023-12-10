from scripts.max_height import run_max_height_script
from scripts.sensor_data import run_sensor_data_script
from utils.constants import MaxHeightConstants


if __name__ == "__main__":
    scripts = [run_sensor_data_script]
    if MaxHeightConstants.ENABLED:
        scripts.append(run_max_height_script)

    for script in scripts:
        script()
