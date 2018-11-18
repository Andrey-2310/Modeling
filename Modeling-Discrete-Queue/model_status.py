class ModelStatus:
    queueLength = 0
    isThreadOneBlocked = False
    isThreadTwoBlocked = False

    def __init__(self, queueLength, isThreadOneBlocked, isThreadTwoBlocked):
        self.queueLength = queueLength
        self.isThreadOneBlocked = isThreadOneBlocked
        self.isThreadTwoBlocked = isThreadTwoBlocked

    def to_string(self):
        return self.queueLength, 1 if self.isThreadOneBlocked else 0, 1 if self.isThreadTwoBlocked else 0