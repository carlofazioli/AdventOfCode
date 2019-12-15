from intcode import IntCodeComputer as IC3


pc = IC3(source='input', buffered=True)
frame = pc.run()

