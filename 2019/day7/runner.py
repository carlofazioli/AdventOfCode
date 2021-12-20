import itertools
from concurrent.futures import ProcessPoolExecutor, as_completed
from intcode import IntCodeComputer


# Part 1:
def analyze_perm(p):
    pcs = [IntCodeComputer(source='input', buffered=True) for _ in range(5)]
    sig = 0
    for i, phase in enumerate(p):
        inp = [phase, sig]
        out = pcs[i].run(inp)
        sig = out[0]
    return sig


test = analyze_perm([0, 1, 2, 3, 4])
print(test)

with ProcessPoolExecutor(max_workers=120) as executor:
    futures = [executor.submit(analyze_perm, phases)
               for phases in itertools.permutations(range(0, 5))]
    results = [f.result() for f in as_completed(futures)]
print(max(results))

# Part 2:
def analyze_perm_2(p):
    pcs = [IntCodeComputer(source='input', buffered=True) for _ in range(5)]
    sig = 0

