from intcode import IntCodeComputer
from concurrent.futures import ProcessPoolExecutor, as_completed


# Part 1:
# count = 0
# for y in range(50):
#     row = []
#     row_count = 0
#     xmin = 0
#     xmax = 0
#     prev_res = 0
#     for x in range(50):
#         pc = IntCodeComputer(source='input', buffered=True)
#         result = pc.run([x, y])
#         count += result[0][0]
#         row_count += result[0][0]
#         if result[0][0]:
#             row.append('#')
#         else:
#             row.append(' ')
#         if result[0][0] and not prev_res:
#             xmin = x
#         if not result[0][0] and prev_res:
#             xmax = x
#         prev_res = result[0][0]
#     print(''.join(row) + '  --  {}-{}={} '.format(xmin, xmax, xmax-xmin))
#
# print(count)

def check_square(x, y):
    pc = IntCodeComputer(source='input', buffered=True)
    res_0 = pc.run([x, y])[0][0]
    pc = IntCodeComputer(source='input', buffered=True)
    res_1 = pc.run([x + 99, y])[0][0]
    pc = IntCodeComputer(source='input', buffered=True)
    res_2 = pc.run([x, y + 99])[0][0]
    pc = IntCodeComputer(source='input', buffered=True)
    res_3 = pc.run([x + 99, y + 99])[0][0]
    if res_0 and res_1 and res_2 and res_3:
        return 'SUCCESS! x,y = {},{}'.format(x, y)


# with ProcessPoolExecutor(max_workers=100) as executor:
#     futures = executor.map(check_square, range(370, 10000), range(500, 10000))
#     for f in futures:
#         if f:
#             print(f)

# Part 2:
for y in range(650, 100000):
    print('checking row ', y)
    for x in range(37*y//50, 10000):
        pc = IntCodeComputer(source='input', buffered=True)
        result_1 = pc.run([x, y])[0][0]
        if result_1:
            pc = IntCodeComputer(source='input', buffered=True)
            result_2 = pc.run([x + 99, y])[0][0]
        else:
            result_2 = 0
        if result_1 and not result_2:
            break
        else:
            pc = IntCodeComputer(source='input', buffered=True)
            result_3 = pc.run([x, y + 99])[0][0]
            if result_2 and result_3:
                print('FOUND IT')
                print(x, y)
                break
