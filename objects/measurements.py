

class Measurement:
    def __init__(self,
                 prn,
                 t,
                 pseudorange,
                 phase):
        self.prn = prn
        self.t = t
        self.pseudorange = pseudorange
        self.phase = phase

class MeasurementsSnapshot:
    def __init__(self, t):
        self.measurements = {}
        self.prns = set()
        self.t = t

    #measurement :: Measurement
    def addMeasurement(self, measurement):
        self.prns.add(measurement.prn)
        self.measurements[measurement.prn] = measurement









