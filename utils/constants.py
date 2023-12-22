class BaseConstants:
    FILE_ROOT = "raw"
    CSV_FILE = "w20_s20_fine.csv"

    # Graph configs
    SAVE_GRAPH = True
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
        "main": {"color": "r", "linestyle": "dashed", "label": "Average"},
        "extra": {"text_pos_x": 0.1, "text_pos_y": 0}
    }


class SensorDataConstants(BaseConstants):
    USE_COLUMNS = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    INITIAL_DEPTH = 100
    AVERAGE_DEPTH = 10
    SKIP_HEADER = 43
    READ_ROWS = 27000


class MaxHeightConstants(BaseConstants):
    ENABLED = True
    USE_COLUMNS = [1]
    DISTANCES = [0.6, 1.6, 2.6, 3.6, 4.6, 5.6, 6.6, 7.6, 8.6]

    INITIAL_DEPTH = 1000
    AVERAGE_DEPTH = None
    SKIP_HEADER = 0
    READ_ROWS = 9

    # Graph configs
    X_AXIS_LABEL = "x (m)"
    Y_AXIS_LABEL = "h-front (m)"

    MIN_Y_AXIS = 0.0
    MAX_Y_AXIS = 0.2

    MAX_X_AXIS = 9
    MIN_X_AXIS = 0

    LINE_STYLE = "dashdot"

    H_MARK = {
        "main": {"color": "r", "linestyle": "dashed", "label": "Average"},
        "extra": {"text_pos_x": 0.1, "text_pos_y": 0.01}
    }


class AverageVelocityConstants(BaseConstants):
    ENABLED = True
    DISTANCES = [0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1]

    GRADIENT_MIN_X = 20
    GRADIENT_MAX_X = 40

    # Graph configs
    X_AXIS_LABEL = "x (m)"
    Y_AXIS_LABEL = "v-initial (m)"

    MAX_Y_AXIS = 3
    MIN_Y_AXIS = 0
    MAX_X_AXIS = 8.6
    MIN_X_AXIS = 0.6
    LINE_STYLE = "dashdot"

    H_MARK = {
        "main": {"color": "r", "linestyle": "dashed", "label": "Average"},
        "extra": {"text_pos_x": 0.0, "text_pos_y": 0.01}
    }
