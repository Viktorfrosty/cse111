def water_column_height(tower_height, tank_height):

    """Function that calculates and returns the height of a column of water from a tower height and a tank wall height."""

    height_of_the_water_column = tower_height + ( 3 * tank_height / 4 )
    return height_of_the_water_column

def pressure_gain_from_water_height(height):

    """Function that calculates and returns the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank."""

    pressure_from_water_height = (998.2 * 9.80665 * height) / 1000
    return pressure_from_water_height

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):

    """Function that calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through."""
    
    pressure_loss = - friction_factor * pipe_length * 998.2 * fluid_velocity ** 2 / ( 2000 * pipe_diameter )
    return pressure_loss