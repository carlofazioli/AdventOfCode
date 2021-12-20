from intcode import IntCodeComputer


def parse_result_for_packets(result):
    packets = []
    while result:
        dest = result.pop(0)
        x = result.pop(0)
        y = result.pop(0)
        if dest == 255:
            print('PART 1: ', y)
        packets.append([dest, x, y])
    return packets


if __name__ == '__main__':

    network = [IntCodeComputer(source='input', buffered=True) for address in range(50)]
    packet_queue = [[i, i] for i in range(50)]
    nat = [None, None]
    nat_y = None
    nat_y_prev = None

    network_cycles = 0
    while True:
        try:
            packet = packet_queue.pop(0)
        except IndexError:
            packet = []
        if packet:
            dest = packet[0]
            inp = packet[1:3]
            if dest == 255:
                nat = inp
            else:
                result = network[dest].run(inp)
                output_packets = parse_result_for_packets(result[0])
                for p in output_packets:
                    packet_queue.append(p)
        else:
            token = 0
            while not packet_queue:
                if token >= 50:
                    nat_y_prev = nat_y
                    nat_y = nat[1]
                    if nat_y_prev == nat_y:
                        print('PART 2: ', nat_y)
                    result = network[0].run(nat)
                else:
                    result = network[token % 50].run(-1)
                output_packets = parse_result_for_packets(result[0])
                for p in output_packets:
                    packet_queue.append(p)
                token += 1


        if network_cycles % 10000 == 0:
            print('network cycle: ', network_cycles)
        network_cycles += 1







