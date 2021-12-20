import itertools
import collections

from utilities import load_data, submit

input_data = load_data(day=19)

# input_data = '''--- scanner 0 ---
# 404,-588,-901
# 528,-643,409
# -838,591,734
# 390,-675,-793
# -537,-823,-458
# -485,-357,347
# -345,-311,381
# -661,-816,-575
# -876,649,763
# -618,-824,-621
# 553,345,-567
# 474,580,667
# -447,-329,318
# -584,868,-557
# 544,-627,-890
# 564,392,-477
# 455,729,728
# -892,524,684
# -689,845,-530
# 423,-701,434
# 7,-33,-71
# 630,319,-379
# 443,580,662
# -789,900,-551
# 459,-707,401
#
# --- scanner 1 ---
# 686,422,578
# 605,423,415
# 515,917,-361
# -336,658,858
# 95,138,22
# -476,619,847
# -340,-569,-846
# 567,-361,727
# -460,603,-452
# 669,-402,600
# 729,430,532
# -500,-761,534
# -322,571,750
# -466,-666,-811
# -429,-592,574
# -355,545,-477
# 703,-491,-529
# -328,-685,520
# 413,935,-424
# -391,539,-444
# 586,-435,557
# -364,-763,-893
# 807,-499,-711
# 755,-354,-619
# 553,889,-390
#
# --- scanner 2 ---
# 649,640,665
# 682,-795,504
# -784,533,-524
# -644,584,-595
# -588,-843,648
# -30,6,44
# -674,560,763
# 500,723,-460
# 609,671,-379
# -555,-800,653
# -675,-892,-343
# 697,-426,-610
# 578,704,681
# 493,664,-388
# -671,-858,530
# -667,343,800
# 571,-461,-707
# -138,-166,112
# -889,563,-600
# 646,-828,498
# 640,759,510
# -630,509,768
# -681,-892,-333
# 673,-379,-804
# -742,-814,-386
# 577,-820,562
#
# --- scanner 3 ---
# -589,542,597
# 605,-692,669
# -500,565,-823
# -660,373,557
# -458,-679,-417
# -488,449,543
# -626,468,-788
# 338,-750,-386
# 528,-832,-391
# 562,-778,733
# -938,-730,414
# 543,643,-506
# -524,371,-870
# 407,773,750
# -104,29,83
# 378,-903,-323
# -778,-728,485
# 426,699,580
# -438,-605,-362
# -469,-447,-387
# 509,732,623
# 647,635,-688
# -868,-804,481
# 614,-800,639
# 595,780,-596
#
# --- scanner 4 ---
# 727,592,562
# -293,-554,779
# 441,611,-461
# -714,465,-776
# -743,427,-804
# -660,-479,-426
# 832,-632,460
# 927,-485,-438
# 408,393,-506
# 466,436,-512
# 110,16,151
# -258,-428,682
# -393,719,612
# -211,-452,876
# 808,-476,-593
# -575,615,604
# -485,667,467
# -680,325,-822
# -627,-443,-432
# 872,-547,-609
# 833,512,582
# 807,604,487
# 839,-516,451
# 891,-625,532
# -652,-548,-490
# 30,-46,-14
# '''

input_data = input_data.split('\n\n')
n = len(input_data)
scanner_data = {}
for i, s in enumerate(input_data):
    s = s.splitlines()
    pts = []
    for pt in s[1:]:
        pts.append(list(map(int, pt.split(','))))
    scanner_data[i] = {
        'i': i,
        'points': pts,
        'coords': [0, 0, 0],
        'matched': False,
        't_idx': 0,
        'candidates': list(range(n))
    }
    scanner_data[i]['candidates'].remove(i)
scanner_data[0]['coords'] = [0, 0, 0]
scanner_data[0]['matched'] = True


def t(loc, i):
    x, y, z = loc
    if i % 3 == 1:
        x, y, z = loc[2], loc[0], loc[1]
    if i % 3 == 2:
        x, y, z = loc[1], loc[2], loc[0]
    if i % 4 == 1:
        y *= -1
        z *= -1
    if i % 4 == 2:
        x *= -1
        z *= -1
    if i % 4 == 3:
        x *= -1
        y *= -1
    if i >= 12:
        x, y, z = x, z, -y
    return x, y, z


def match_scanners(already_matched, unmatched):
    for t_idx in range(24):
        transformed = [t(p, t_idx) for p in unmatched['points']]
        for p0 in already_matched['points']:
            for p1 in transformed:
                matches = 0
                delta = [a-b for a, b in zip(p0, p1)]
                for tp in transformed:
                    tps = [a+b for a, b in zip(tp, delta)]
                    if tps in already_matched['points']:
                        matches += 1
                if matches >= 12:
                    print(f'Found matching sets with transformation index {t_idx}')
                    unmatched['coords'] = delta
                    unmatched['matched'] = True
                    unmatched['t_idx'] = t_idx
                    new_pts = []
                    for p in unmatched['points']:
                        tp = t(p, t_idx)
                        tps = [a + b for a, b in zip(tp, delta)]
                        new_pts.append(tps)
                    unmatched['points'] = new_pts
                    return t_idx
    return -1


matched = [s for s in scanner_data.values() if s['matched']]
unmatched = [s for s in scanner_data.values() if not s['matched']]
while unmatched:
    s = unmatched.pop(0)
    for m in matched:
        if m['i'] not in s['candidates']:
            print(f'Unmatched set {s["i"]} already tried against matched set {m["i"]}... skipping.')
            continue
        print(f'Trying to match unmatched set {s["i"]} against matched set {m["i"]}.  ')
        match = match_scanners(m, s)
        if match >= 0:
            matched.append(s)
            break
        else:
            s['candidates'].remove(m['i'])
            print(f'No match found with any index.  Removing candidate.')
    if match < 0:
        unmatched.append(s)


beacons = set()
for s in scanner_data.values():
    for p in s['points']:
        beacons.add(tuple(p))
print(len(beacons))


def manhattan(p1, p2):
    return sum(abs(a-b) for a, b in zip(p1, p2))



answer = 0
for x, y, in itertools.combinations(matched, 2):
    answer = max(answer, manhattan(x['coords'], y['coords']))

print(answer)