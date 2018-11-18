class PseudoRandom:

    a = 134279
    Rn = 1
    m = 313107

    def random(self):
        self.Rn = self.a * self.Rn % self.m
        return self.Rn / self.m
