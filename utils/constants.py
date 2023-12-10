class BaseConstants:
    FILE_ROOT = "raw"
    CSV_FILE = "w17.5_s20_coarse.csv"

    # Graph configs
    X_AXIS_LABEL = "Time (s)"
    Y_AXIS_LABEL = "h (m)"

    MIN_X_AXIS = 0
    MAX_X_AXIS = 140

    MIN_Y_AXIS = 0.0
    MAX_Y_AXIS = 0.10

    LINE_STYLE = None
    #  Line styles: '-', '--', '-.', ':', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

    MARKER = {
        "marker": "o",
        "ms": 15,  # marker size
        "mec": "r",  # border color
        "mfc": "w",  # filling color
    }
    H_MARK = {
        "color": "r",
        "linestyle": "dashed",
        "label": "Average"
    }


class SensorDataConstants(BaseConstants):
    USE_COLUMNS = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    INITIAL_DEPTH = 1000
    AVERAGE_DEPTH = None
    SKIP_HEADER = 37
    READ_ROWS = 27000


class MaxHeightConstants(BaseConstants):
    ENABLED = True
    USE_COLUMNS = [1]
    DISTANCES = [0.6, 1.6, 2.6, 3.6, 4.6, 5.6, 6.6, 7.6, 8.6]

    INITIAL_DEPTH = 100
    AVERAGE_DEPTH = 10
    SKIP_HEADER = 0
    READ_ROWS = 9

    # Graph configs
    X_AXIS_LABEL = "x (m)"
    Y_AXIS_LABEL = "h-front (m)"

    MAX_Y_AXIS = 0.2
    MIN_Y_AXIS = 0.0
    MAX_X_AXIS = 9
    MIN_X_AXIS = 0
    LINE_STYLE = "dashdot"


class AverageVelocityConstants(BaseConstants):
    ENABLED = True
    DISTANCES = [0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1]

    # Graph configs
    X_AXIS_LABEL = "x (m)"
    Y_AXIS_LABEL = "v-initial (m)"

    MAX_Y_AXIS = 3.0
    MIN_Y_AXIS = 0.0
    MAX_X_AXIS = 8.6
    MIN_X_AXIS = 0.6
    LINE_STYLE = "dashdot"
