class BaseConstants:
    FILE_ROOT = "raw"
    CSV_FILE = "w20_s25_fine.csv"

    # Graph configs
    X_AXIS_LABEL = "Time (s)"
    Y_AXIS_LABEL = "h (m)"

    MIN_X_AXIS = 0
    MAX_X_AXIS = 140

    MIN_Y_AXIS = -0.03
    MAX_Y_AXIS = 0.10


class SensorDataConstants(BaseConstants):
    USE_COLUMNS = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    INITIAL_DEPTH = 100
    AVERAGE_DEPTH = 10
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

    MAX_Y_AXIS = 0.04
    MIN_Y_AXIS = 0.065
    MAX_X_AXIS = 9
    MIN_X_AXIS = 0
