from model_status import ModelStatus
from pseudo_random import PseudoRandom
import random
from collections import Counter

pseudo_random = PseudoRandom()

statusHistory = []
handle_request = []

p = 0.1
pi_1 = 0.7
pi_2 = 0.5

maxQueueLength = 2

isNewRequest = False
queueLength = 0
isThreadOneBlocked = False
isThreadTwoBlocked = False


def generate_state(probability):
    return pseudo_random.random() < probability


def iterate():
    global isNewRequest
    global queueLength
    global isThreadOneBlocked
    global isThreadTwoBlocked

    handling_requests_calculater = 0

    isNewRequest = not generate_state(p)
    if isThreadOneBlocked:
        isThreadOneBlocked = generate_state(pi_1)
        if not isThreadOneBlocked:
            handling_requests_calculater += 1

    if isThreadTwoBlocked:
        isThreadTwoBlocked = generate_state(pi_2)
        if not isThreadTwoBlocked:
            handling_requests_calculater += 1

    if isNewRequest and queueLength < maxQueueLength:
        queueLength += 1

    if not isThreadOneBlocked and queueLength > 0:
        isThreadOneBlocked = True
        queueLength -= 1

    if not isThreadTwoBlocked and queueLength > 0:
        isThreadTwoBlocked = True
        queueLength -= 1

    statusHistory.append(ModelStatus(queueLength, isThreadOneBlocked, isThreadTwoBlocked).to_string())
    handle_request.append(handling_requests_calculater)

iterations = 1000000
for i in range(iterations):
    iterate()


counter = Counter(statusHistory)

for state in counter:
    print(state, round(counter[state]/iterations * 100, 2),'%')


L__q = sum(list(map(lambda state: state[0] * counter[state], counter))) / iterations
print("\nL__q:", L__q)

A = sum(handle_request) / iterations
print("A:", A)

W__q = L__q / A
print("W__q: ", W__q)

K__1 = sum(list(map(lambda state: state[1] * counter[state], counter))) / iterations
print("K__1:", K__1)
K__2 = sum(list(map(lambda state: state[2] * counter[state], counter))) / iterations
print("K__2:", K__2)




