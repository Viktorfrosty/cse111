def water_column_height(tower_height, tank_height):

    """Function that calculates and returns the height of a column of water from a tower height and a tank wall height."""

    height_of_the_water_column = tower_height + ( 3 * tank_height / 4 )
    return height_of_the_water_column

def pressure_gain_from_water_height(height, gravity_acceleration, water_density):

    """Function that calculates and returns the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank."""

    pressure_from_water_height = (water_density * gravity_acceleration * height) / 1000
    return pressure_from_water_height

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity, water_density):

    """Function that calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through."""

    pressure_loss = - friction_factor * pipe_length * water_density * fluid_velocity ** 2 / ( 2000 * pipe_diameter )
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings, water_density):

    """Function that calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline."""

    lost_pressure = ( -0.04 * water_density * fluid_velocity ** 2 * quantity_fittings ) / 2000
    return lost_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity, water_density, dynamic_viscocity):

    """Function that calculates and returns the Reynolds number for a pipe with water flowing through it. The Reynolds number is a unitless ratio of the inertial and viscous forces in a fluid that is useful for predicting fluid flow in different situations."""

    reynolds_number = ( water_density * hydraulic_diameter * fluid_velocity ) / dynamic_viscocity
    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, water_density):

    """Function that calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter."""

    computed_constant = - ( ( 0.1 + ( 50 / reynolds_number ) ) * ( ( ( larger_diameter / smaller_diameter ) ** 4) - 1 ) )

    loss_pressure_from_pipe_reduction = ( computed_constant * water_density * fluid_velocity ** 2 ) / 2000
    return loss_pressure_from_pipe_reduction

def kilopascals_to_pounds_per_square_inch(pressure): # challenge
    converted_pressure = pressure * 0.14503773800722
    return converted_pressure

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

# Challenge
EARTH_ACCELERATION_OF_GRAVITY = 9.80665 # meter / second^2
WATER_DENSITY = 998.2 # kilogram / meter^3
WATER_DYNAMIC_VISCOSITY = 0.0010016 # Pascal seconds

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)

    gravity_acceleration = EARTH_ACCELERATION_OF_GRAVITY # challenge
    water_density = WATER_DENSITY # challenge
    pressure = pressure_gain_from_water_height(water_height, gravity_acceleration, water_density)

    dynamic_viscocity = WATER_DYNAMIC_VISCOSITY # challenge
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity, water_density, dynamic_viscocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity, water_density,)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles, water_density)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER, water_density)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity, water_density)
    pressure += loss

    converted_pressure = kilopascals_to_pounds_per_square_inch(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals ({converted_pressure:.1f} psi)") # challenge

if __name__ == "__main__":
    main()