import time
import random

class LoRaModule:
    def __init__(self):
        # Initialize LoRa module
        self.connected = False
    
    def initialize(self):
        # Initialize LoRa module connection
        print("LoRa module initialized.")
        self.connected = True
    
    def send_data(self, data):
        # Simulate sending data over LoRa
        if self.connected:
            print("Sending data over LoRa:", data)
            time.sleep(1)
            print("Data sent successfully.")
        else:
            print("Error: LoRa module not connected.")

    def close(self):
        # Close LoRa module connection
        self.connected = False
        print("LoRa module connection closed.")


class GPSModule:
    def __init__(self):
        # Initialize GPS module
        self.connected = False
    
    def initialize(self):
        # Initialize GPS module connection
        print("GPS module initialized.")
        self.connected = True
    
    def read(self):
        # Simulate reading GPS data
        if self.connected:
            latitude = round(random.uniform(-90, 90), 6)
            longitude = round(random.uniform(-180, 180), 6)
            altitude = round(random.uniform(0, 5000), 2)
            print("GPS data read successfully.")
            return {'latitude': latitude, 'longitude': longitude, 'altitude': altitude}
        else:
            print("Error: GPS module not connected.")
            return None

    def close(self):
        # Close GPS module connection
        self.connected = False
        print("GPS module connection closed.")


def main():
    # Initialize LoRa and GPS modules
    lora_module = LoRaModule()
    lora_module.initialize()
    
    gps_module = GPSModule()
    gps_module.initialize()

    try:
        while True:
            # Read GPS data
            gps_data = gps_module.read()
            if gps_data:
                latitude = gps_data['latitude']
                longitude = gps_data['longitude']
                altitude = gps_data['altitude']

                # Send GPS data over LoRa
                lora_module.send_data(f'Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude}')

                # Wait for some time before reading GPS again
                time.sleep(10)
    
    except KeyboardInterrupt:
        print("Exiting program...")
        lora_module.close()
        gps_module.close()

if __name__ == "__main__":
    main()
