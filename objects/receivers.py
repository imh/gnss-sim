class ReceiverOnRails:
    def __init__(self,
                 time,
                 position_function,
                 velocity_function):

        self.time = time

        self.position_function = position_function
        self.position = position_function(time)

        self.velocity_function = velocity_function
        self.velocity = velocity_function(time)

    def propogate(self, dt):
        self.time += dt
        self.position = self.position_function(self.time)
        self.velocity = self.velocity_function(self.time)


class ReceiverOnIntegrals:
    def __init__(self,
                 time,
                 initial_position,
                 initial_velocity,
                 update_function):
        self.time = time
        self.position = initial_position
        self.velocity = initial_velocity
        self.update_function = update_function

    def propagate(self, dt):
        self.time += dt
        self.position, self.velocity = self.update_function(self.position,self.velocity, dt)