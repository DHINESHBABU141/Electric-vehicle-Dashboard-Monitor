import time
import random

class ElectricVehicle:
    def __init__(self, battery_capacity=100, temperature=25, motor_status=True):
        self.battery_level = battery_capacity  # Battery percentage
        self.temperature = temperature  # in Celsius
        self.motor_status = motor_status  # True means motor is working
        self.faults = []  # Stores detected faults
        self.light_indicator = "OFF"  # Light status
        self.charging_status = False  # Charging status
    
    def battery_drain(self):
        if not self.charging_status:
            drain_rate = random.uniform(0.5, 2.0)  # Simulating drain rate per cycle
            self.battery_level -= drain_rate
            if self.battery_level < 20:
                self.faults.append("Battery Low Warning!")
                self.light_indicator = "ON"  # Turn on vehicle light for low battery
            else:
                self.light_indicator = "OFF"
            if self.battery_level <= 0:
                self.battery_level = 0
                self.faults.append("Battery Drained! EV Stopped.")
    
    def charge_battery(self):
        if self.charging_status:
            charge_rate = random.uniform(2.0, 5.0)  # Simulating charge rate per cycle
            self.battery_level += charge_rate
            if self.battery_level > 100:
                self.battery_level = 100
            print("Battery Charging...")
    
    def check_faults(self):
        self.faults.clear()  # Reset faults each cycle
        
        if random.random() < 0.05:  # 5% chance of motor failure
            self.motor_status = False
            self.faults.append("Motor Fault Detected!")
        
        if random.random() < 0.03:  # 3% chance of overcurrent
            self.faults.append("Overcurrent Fault Detected!")
        
        self.temperature += random.uniform(-1, 3)  # Random temp fluctuation
        if self.temperature > 60:
            self.faults.append("Overheating Detected!")
    
    def dashboard(self):
        print("\n----- EV Dashboard -----")
        print(f"Battery Level: {self.battery_level:.2f}%")
        print(f"Temperature: {self.temperature:.1f}°C")
        print(f"Motor Status: {'Running' if self.motor_status else 'Faulty'}")
        print(f"Battery Low Light: {self.light_indicator}")
        print(f"Charging Status: {'Charging' if self.charging_status else 'Not Charging'}")
        if self.faults:
            print("Faults:")
            for fault in self.faults:
                print(f"  - {fault}")
        else:
            print("No faults detected.")
        print("------------------------")
    
    def run(self):
        while self.battery_level > 0:
            self.charge_battery()
            self.battery_drain()
            self.check_faults()
            self.dashboard()
            time.sleep(2)  # Simulate real-time monitoring
            if "Battery Drained! EV Stopped." in self.faults:
                break

# Create an EV instance and start monitoring
ev = ElectricVehicle()
ev.run()
