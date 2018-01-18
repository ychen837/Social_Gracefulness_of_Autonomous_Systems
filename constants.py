class CONSTANTS:

    # INITIAL CONDITIONS (machine)
    MACHINE_INITIAL_POSITION = (-1, 0)

    # DISPLAY
    FPS = 60

    CAR_WIDTH = 100
    CAR_LENGTH = 200
    LANE_WIDTH = 150
    SCREEN_WIDTH = LANE_WIDTH*2
    SCREEN_HEIGHT = 1000

    # SPEEDS
    VEHICLE_MOVEMENT_SPEED = 0.002
    VEHICLE_LATERAL_MOVEMENT_SPEED = 0.001

    VEHICLE_CLEARANCE = (CAR_LENGTH/LANE_WIDTH)*1.5

    VEHICLE_MOVEMENT_LIMITER = 0.01

    # OPTIMIZATION
    MACHINE_CRITERIA = 90
    MACHINE_INTENT = (0.1, 0.0)
    STEPS_FOR_CONSIDERATION = 10


    # DIVIDE BY ZERO CATCH
    EPS = 0.0000001
