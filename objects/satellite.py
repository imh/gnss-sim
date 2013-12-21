

class Satellite:
    def __init__(self, almanac, time):
        """
        :type almanac: sa.Almanac
        """
        self.time = time
        self.almanac = almanac
        self.state_ecef = almanac.calc_state(time)

    def propagate(self, dt):
        self.time += dt
        self.state_ecef = self.almanac.calc_state(self.time)

    #TODO make this a function of state and return an actual position
    def get_position(self):
        return [0, 0, 0]

    #TODO make this a function of state and return an actual velocity
    def get_velocity(self):
        return [0, 0, 0]
