from day5.intcode import IntCodeComputer

pcs = [IntCodeComputer('input') for _ in range(5)]

for pc in pcs:
    pc.run()
