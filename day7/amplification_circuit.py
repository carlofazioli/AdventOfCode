import pexpect
import itertools
from concurrent.futures import ProcessPoolExecutor, as_completed, wait


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


def analyze_perm_part1(perm):
    pc = pexpect.spawn('python', ['runner.py'])
    sig = 0
    out = None
    for inp in perm:
        pc.sendline(str(inp))
        pc.sendline(str(sig))
        for _ in range(3):
            pc.expect([b'\r\n', pexpect.EOF])
            out = pc.before
        sig = int(out.split(b'\r\n')[0])
    return sig


if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=120) as executor:
        futures = [executor.submit(analyze_perm_part2, phases)
                   for phases in itertools.permutations(range(5, 10))]
        results = [f.result() for f in as_completed(futures)]

    print(results)
    print(max(results))
