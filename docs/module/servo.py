"""
Servo control module for the Wombat controller.

This module provides functions to control servos on the Wombat controller.
"""

def disable_servo(port):
    """
    Disable a specific servo.

    Parameters:
        port (int): The port, between 0 and 3, to disable.
    """
    pass

def disable_servos():
    """
    Disable all four servo channels.
    """
    pass

def enable_servo(port):
    """
    Enable a specific servo.

    Parameters:
        port (int): The port, between 0 and 3, to enable.
    """
    pass

def enable_servos():
    """
    Enable all four servo channels.
    """
    pass

def get_servo_enabled(port):
    """
    Check if a servo is enabled.

    Parameters:
        port (int): The port, between 0 and 3.

    Returns:
        int: The servo enable setting 0: disabled, 1: enabled.
    """
    pass

def get_servo_position(port):
    """
    Get the most recent commanded servo position.

    Parameters:
        port (int): The port of the servo.

    Returns:
        int: The servo's position as an 11 bit integer (which is an integer between 0 and 2047).

    Note:
        This method will return the last sent position, not the currently set position.
    """
    pass

def set_servo_enabled(port, enabled):
    """
    Enable or disable a specific servo.

    Parameters:
        port (int): The port, between 0 and 3, to enable.
        enabled (int): The new enable setting 0: disabled, 1: enabled.
    """
    pass

def set_servo_position(port, position):
    """
    Set a new servo goal position.

    Parameters:
        port (int): The port of the servo.
        position (int): The new servo position, between 0 and 2047.

    Note:
        Even though the servos have a theoretical range between 0 and 2047, the actual range is often less. Setting the servo to a position that it cannot physically reach will cause the servo to audibly strain and will consume battery very quickly.
    """
    pass
