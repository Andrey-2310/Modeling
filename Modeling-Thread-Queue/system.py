from pseudo_random import PseudoRandom
from request import Request
import copy


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

    def add_tick(self):
        for request in self.requests_in_buffer:
            request.time_spend += 1
        if self.request_in_channel is not None:
            self.request_in_channel.time_spend += 1

    def move_back_to_buffer_with_check(self):
        # TODO: T_max should be normalized here
        if self.request_in_channel is not None and self.request_in_channel.time_spend > self.T__max:
            self.requests_in_buffer.insert(0, copy.copy(self.request_in_channel))
            self.request_in_channel = None

    def iteration(self):
        for tic in range(self.tics_in_iteration):
            # TODO: intensities should be normalized
            if self.generate_state(self.input_intensity):
                self.requests_in_buffer.insert(0, Request())
            if self.request_in_channel is not None:
                if self.generate_state(self.handling_intensity):
                    self.handled_requests.append(copy.copy(self.request_in_channel))
                    self.request_in_channel = None

            if len(self.requests_in_buffer) > 0 and self.request_in_channel is not None:
                self.request_in_channel = self.requests_in_buffer.pop()

            self.add_tick()
            self.move_back_to_buffer_with_check()
