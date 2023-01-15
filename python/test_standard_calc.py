from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(-180) == -180
    assert bound_to_180(180) == -180
    assert bound_to_180(540) == -180
    assert bound_to_180(720) == 0
    assert bound_to_180(60) == 60
    assert bound_to_180(-45) == -45
    assert bound_to_180(120) == 120
    assert bound_to_180(-125) == -125
    assert bound_to_180(179) == 179
    assert bound_to_180(-179) == -179
    assert bound_to_180(-3779) == -179
    assert bound_to_180(3779) == 179
    assert bound_to_180(360) == 0
    assert bound_to_180(-233) == 53


""" Tests for is_angle_between() """


def test_between_basic1():
    """Checks different situations such as boundary conditions.
    For example, what happens when par1 == par2 == par3? In addition, what happens if we change the order of the parameters
    """
    assert is_angle_between(0, 1, 2) == 1
    assert is_angle_between(0, 20, 360) == 0
    assert is_angle_between(-20, 10, 40) == 1
    assert is_angle_between(0, 30, 60) == 1
    assert is_angle_between(0, 0, 0) == 1
    assert is_angle_between(10, 0, 5) == 0
    assert is_angle_between(180, 135, 90) == 1
    assert is_angle_between(360, 720, 90) == 0
    assert is_angle_between(1220, 120, -240) == 1

    # Checks negative angle conditions such as can it identify a negative angle between a positive and negative angle.
    assert is_angle_between(-170, -130, -90) == 1
    assert is_angle_between(-170, -130, 100) == 0
    assert is_angle_between(-135, 20, -90) == 0
    assert is_angle_between(-90, -90, -90) == 1
    assert is_angle_between(180, 100, -233) == 1
