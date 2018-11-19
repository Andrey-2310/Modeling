from pseudo_random import PseudoRandom
from request import Request

class System:

    input_intensity = 0.02
    handling_intensity = 0.025
    T__max = 0.4
    tics_in_iteration = 100
    pseudo_random = PseudoRandom()

    requests_in_buffer = []
    request_in_channel = None

    handled_requests = []

    def generate_state(self, probability):
        return self.pseudo_random.random() < probability

    def iteration(self):
        for tic in range(self.tics_in_iteration):
            if self.generate_state(self.input_intensity):
                self.requests_in_buffer.append(Request())
            if self.request_in_channel is not None:
                if self.generate_state(self.handling_intensity):
                    self.request_in_channel = None

            if len(self.requests_in_buffer) > 0 and self.request_in_channel is not None:
                self.request_in_channel = self.requests_in_buffer.pop()



