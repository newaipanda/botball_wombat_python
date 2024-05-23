def alloff():
    """
    Turns all motors off.

    See also:
        ao
    """
    pass


def ao():
    """
    Turns all motors off.

    See also:
        alloff
    """
    pass


def bk(motor):
    """
    Moves the given motor backward at full power.

    Parameters:
        motor (int): The motor's port.
    """
    pass


def block_motor_done(motor):
    """
    Wait until the motor is at its goal.

    Parameters:
        motor (int): The motor port.

    See also:
        bmd
    """
    pass


def bmd(motor):
    """
    Wait until the motor is at its goal.

    Parameters:
        motor (int): The motor port.

    See also:
        block_motor_done
    """
    pass


def clear_motor_position_counter(motor):
    """
    Clears the motor position counter.

    Parameters:
        motor (int): The motor port.

    See also:
        cmpc
    """
    pass


def cmpc(motor):
    """
    Clears the motor position counter.

    Parameters:
        motor (int): The motor port.

    See also:
        clear_motor_position_counter
    """
    pass


def fd(motor):
    """
    Moves the given motor forward at full power.

    Parameters:
        motor (int): The motor's port.
    """
    pass


def freeze(motor):
    """
    Active braking to stop a motor.

    Parameters:
        motor (int): The motor port.

    Returns:
        int: 1 if at goal, 0 if not at goal.
    """
    pass


def get_motor_done(motor):
    """
    Check if the motor has reached its goal.

    Parameters:
        motor (int): The motor port.

    Returns:
        int: 1 if at goal, 0 if not at goal.
    """
    pass


def get_motor_position_counter(motor):
    """
    Gets the current motor position.

    Parameters:
        motor (int): The motor port.

    See also:
        gmpc
    """
    pass


def get_pid_gains(motor, p, i, d, pd, id, dd):
    """
    Get the motor PID gains, represented as fractions.

    Parameters:
        motor (int): The motor port.
        p (short): The P (proportional) gain numerator.
        i (short): The I (integral) gain numerator.
        d (short): The D (derivative) gain numerator.
        pd (short): The P (proportional) gain denominator.
        id (short): The I (integral) gain denominator.
        dd (short): The D (derivative) gain denominator.
    """
    pass


def getpwm(motor):
    """
    Get the current motor PWM command.

    Parameters:
        motor (int): The motor port.
    """
    pass


def gmpc(motor):
    """
    Gets the current motor position.

    Parameters:
        motor (int): The motor port.

    See also:
        get_motor_position_counter
    """
    pass


def mav(motor, velocity):
    """
    Set a goal velocity in ticks per second.

    Parameters:
        motor (int): The motor port.
        velocity (int): The goal velocity in -1500 to 1500 ticks/second.

    See also:
        move_at_velocity
    """
    pass


def motor(motor, percent):
    """
    Moves a motor at a percent velocity.

    Parameters:
        motor (int): The motor port.
        percent (int): The percent of the motor's velocity, between -100 and 100.
    """
    pass


def motor_power(motor, percent):
    """
    Moves a motor at a percent power.

    Parameters:
        motor (int): The motor port.
        percent (int): The power of the motor, between -100 and 100.
    """
    pass


def move_at_velocity(motor, velocity):
    """
    Set a goal velocity in ticks per second. The range is -1500 to 1500, though motor position accuracy may be decreased outside of -1000 to 1000.

    Parameters:
        motor (int): The motor port.
        velocity (int): The goal velocity in -1500 to 1500 ticks/second.

    See also:
        mav
    """
    pass


def move_relative_position(motor, speed, delta_pos):
    """
    Set a goal position (in ticks) for the motor to move to, relative to the current position.

    Parameters:
        motor (int): The motor port.
        speed (int): The speed to move at, between -1500 and 1500 ticks/second.
        delta_pos (int): The position to move to (in ticks) given the current position.

    See also:
        mrp
    """
    pass


def move_to_position(motor, speed, goal_pos):
    """
    Set a goal position (in ticks) for the motor to move to. There are approximately 1500 ticks per motor revolution. This function is more accurate if speeds between -1000 and 1000 are used.

    Parameters:
        motor (int): The motor port.
        speed (int): The speed to move at, between -1500 and 1500 ticks/second.
        goal_pos (int): The position to move to (in ticks).

    See also:
        mtp
    """
    pass


def mrp(motor, speed, delta_pos):
    """
    Set a goal position (in ticks) for the motor to move to, relative to the current position.

    Parameters:
        motor (int): The motor port.
        speed (int): The speed to move at, between -1500 and 1500 ticks/second.
        delta_pos (int): The position to move to (in ticks) given the current position.

    See also:
        move_relative_position
    """
    pass


def mtp(motor, speed, goal_pos):
    """
    Set a goal position (in ticks) for the motor to move to.

    Parameters:
        motor (int): The motor port.
        speed (int): The speed to move at, between -1500 and 1500 ticks/second.
        goal_pos (int): The position to move to (in ticks).

    See also:
        move_to_position
    """
    pass


def off(motor):
    """
    Turns the specified motor off.

    Parameters:
        motor (int): The motor's port.
    """
    pass


def set_pid_gains(motor, p, i, d, pd, id, dd):
    """
    Set the motor PID gains, represented as fractions.

    Parameters:
        motor (int): The motor port.
        p (short): The P (proportional) gain numerator.
        i (short): The I (integral) gain numerator.
        d (short): The D (derivative) gain numerator.
        pd (short): The P (proportional) gain denominator.
        id (short): The I (integral) gain denominator.
        dd (short): The D (derivative) gain denominator.
    """
    pass


def setpwm(motor, pwm):
    """
    Set the motor PWM (percent power) command.

    Parameters:
        motor (int): The motor port.
        pwm (int): A new motor PWM command between 0 and 100.
    """
    pass
