
def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """

    # in360 bounds the angle within 0-360 degrees
    # in180 bounds the angle within 0-180 degrees

    if (angle < 0):  # Checks whether the angle is negative or positive
        in360 = angle % -360.0  # Bounds the angle within 360 degrees
        if (in360 < -180):
            in180 = abs(angle) % 180
        elif (in360 == -180):
            #  in180 = -180 % -180 == 0
            in180 = -180
        else:
            in180 = angle % -180
    else:
        in360 = angle % 360.0
        if (in360 > 180):
            in180 = -angle % -180
        elif (in360 == 180):
            #  in180 = 180 % 180 = 0 not -180
            in180 = -180
        else:
            in180 = angle % 180

    return in180


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    first_angle, second_angle = bound_to_180(first_angle), bound_to_180(second_angle)

    # Assuming all angles are positive
    diff_angle = abs(first_angle - second_angle)
    if (second_angle >= first_angle):
        max_angle, min_angle = second_angle, first_angle
    else:
        max_angle, min_angle = first_angle, second_angle

    if (diff_angle > 180):  # Reflex angle region
        #  Checks whether the angle is outside the reflex angle region
        if (middle_angle > max_angle or middle_angle < min_angle):
            return True
        else:
            return False
    else:
        if (min_angle <= middle_angle <= max_angle):  # Checks whether within anti-reflex region.
            return True
        else:
            return False
