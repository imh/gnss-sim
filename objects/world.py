

class World:
    def __init__(self, time, satellites, base_station, rover, measurement_process):
        self.time = time
        self.satellites = satellites
        self.base_station = base_station
        self.rover = rover
        self.measurement_process = measurement_process

    def propagate(self, dt):
        self.time += dt
        for satellite in self.satellites:
            satellite.propagate(dt)
        self.base_station.propagate(dt)
        self.rover.propagate(dt)

    def take_measurements(self):
        return self.measurement_process.measure(self.satellites, {self.base_station, self.rover})


