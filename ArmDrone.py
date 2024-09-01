from dronekit import connect, VehicleMode
import time

def arm_and_takeoff(vehicle):
    """
    Arms the vehicle and takes off to a specified altitude.
    """
    print("Basic pre-arm checks")
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Vehicle is armed!")

def main():
    # Connect to the vehicle using the ttyAMA0 serial port
    connection_string = 'ttyAMA0'
    print(f"Connecting to vehicle on {connection_string}...")
    vehicle = connect(connection_string, wait_ready=True)

    arm_and_takeoff(vehicle)
    vehicle.close()

    print("Script completed")

if __name__ == "__main__":
    main()
