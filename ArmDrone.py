import argparse
from dronekit import connect, VehicleMode
import time

def arm_and_takeoff(vehicle):
    """
    Arms the vehicle and takes off to a specified altitude.
    """
    print("Basic pre-arm checks")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Set the vehicle to GUIDED mode and then arm
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Vehicle is armed!")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Connect to a vehicle and arm it.")
    parser.add_argument('--connect', type=str, required=True, help='Connection string to the vehicle')
    args = parser.parse_args()

    # Connect to the Vehicle (SITL or real vehicle)
    connection_string = args.connect
    print(f"Connecting to vehicle on {connection_string}...")
    vehicle = connect(connection_string, wait_ready=True)

    # Call the arm and takeoff function
    arm_and_takeoff(vehicle)

    # Close vehicle object before exiting script
    vehicle.close()

    print("Script completed")

if __name__ == "__main__":
    main()
