import pexpect
import itertools
from concurrent.futures import ProcessPoolExecutor, as_completed


def analyze_perm_part1(phases):
    # Spawn 5 IntCode comps
    amps = [pexpect.spawn('python', ['ic2.py', '-s', '../day7/input']) for _ in range(5)]

    sig = 0
    out = None
    for i, p in enumerate(phases):
        # Each amp gets 2 inputs:
        #   1. The phase
        #   2. The output signal from the prev amp (or 0 for the first amp)
        amps[i].sendline(str(p))
        amps[i].sendline(str(sig))

        # Pexpect will read those same values from the CL, so extract the 3rd one as the
        # output signal from the amp:
        for _ in range(3):
            amps[i].expect([b'\r\n', pexpect.EOF])
            out = amps[i].before
        sig = int(out.split(b'\r\n')[0])

    # After all 5 amps have, run, this is the output signal:
    return sig


def analyze_perm_part2(perm):
    pcs = [pexpect.spawn('python', ['runner2.py']) for _ in range(5)]
    sig = 0
    out = None
    running = True
    # Initializes the PCs:
    for i, inp in enumerate(perm):
        pcs[i].sendline(str(inp))
        pcs[i].sendline(str(sig))
        for _ in range(3):
            index = pcs[i].expect([b'\r\n', pexpect.EOF])
            if index == 0:
                out = pcs[i].before
            if index == 1:
                running = False
                break
        sig = int(out.split(b'\r\n')[0])
    while running:
        for i in range(5):
            pcs[i].sendline(str(sig))
            for _ in range(2):
                index = pcs[i].expect([b'\r\n', pexpect.EOF])
                if index == 0:
                    out = pcs[i].before
                if index == 1:
                    running = False
                    break
            sig = int(out.split(b'\r\n')[0])
    return sig

if __name__ == '__main__':

    # For part 1, test all phases that permute 0..4:
    with ProcessPoolExecutor(max_workers=120) as executor:
        futures_1 = [executor.submit(analyze_perm_part1, phases)
                     for phases in itertools.permutations(range(0, 5))]
        results_1 = [f.result() for f in as_completed(futures_1)]
    print(max(results_1))

    # For part 2, test all phases that permute 5..9:
    with ProcessPoolExecutor(max_workers=120) as executor:
        futures_2 = [executor.submit(analyze_perm_part2, phases)
                     for phases in itertools.permutations(range(5, 10))]
        results_2 = [f.result() for f in as_completed(futures_2)]
    print(max(results_2))
