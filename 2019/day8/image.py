def parse_image(source):
    if isinstance(source, str):
        with open(source) as f:
            img = f.readline()
    return img.rstrip('\r\n')

def counts(layer):
    ones = 0
    zeros = 0
    twos = 0
    for c in layer:
        if c == '0':
            zeros += 1
        if c == '1':
            ones += 1
        if c == '2':
            twos += 1
    return zeros, ones, twos


if __name__ == '__main__':
    w = 25
    h = 6
    img_raw = parse_image('input')
    layers = []
    while len(img_raw) > 0:
        layers.append(img_raw[:w*h])
        img_raw = img_raw[w*h:]

    result = None
    z_min = w * h + 1
    for layer in layers[:-1]:
        z, o, t = counts(layer)
        if z < z_min:
            z_min = z
            result = o*t

    decoded_img = ''
    for i in range(h):
        for j in range(w):
            pixel = i*w + j
            for layer in layers:
                if layer[pixel] == '0':
                    decoded_img += ' '
                    break
                if layer[pixel] == '1':
                    decoded_img += 'X'
                    break
                if layer[pixel] == '2':
                    continue
        decoded_img += '\n'

    print(decoded_img)
    input()
