def extended_gcd(a, b):
    """"
    Solves ax + by = g = 1
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('No Modular Inverse.')
    else:
        return x % m


class Deck:
    def __init__(self,
                 n_cards=None):
        self.size = n_cards
        self.top = 0
        self.offset = 1

    def deal_into_new_stack(self):
        self.top += self.offset * (self.size - 1)
        self.top %= self.size
        self.offset *= -1
        self.offset %= self.size

    def cut_n_cards(self, n):
        self.top += n * self.offset
        self.top %= self.size

    def deal_with_increment(self, k):
        self.offset *= modinv(k, self.size)
        self.offset %= self.size

    def __getitem__(self, item):
        return (self.top + item * self.offset) % self.size

    def find(self, card):
        j = modinv(self.offset, self.size)
        return j * (card - self.top) % self.size

    def __repr__(self):
        out = []
        for i in range(self.size):
            out.append(str(self[i]))
        return ', '.join(out)


def run_deck(deck, source_file, debug=False):
    with open(source_file) as f:
        techniques = [line.strip('\r\n') for line in f]

    for tech in techniques:
        tech_vec = tech.split(' ')
        if 'increment' in tech_vec:
            val = tech_vec[-1]
            deck.deal_with_increment(int(val))
        if 'cut' in tech_vec:
            val = tech_vec[-1]
            deck.cut_n_cards(int(val))
        if 'stack' in tech_vec:
            deck.deal_into_new_stack()
        if debug:
            print()
            print('debugging step: ', tech_vec)
            print(deck)

    return deck


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1: factors.append(n)
            break
    return factors

def geo_mod(n, b, m):
    t = 1
    e = b % m
    total = 0
    while n > 0:
        if n & 1 == 1:
            total = (e * total + t) % m
        t = ((e + 1) * t) % m
        e = (e * e) % m
        n = n // 2
    return total




if __name__ == '__main__':

    # source = 'input'
    # deck_size = 119315717514047
    # n_shuffles = 101741582076661
    # card = 2020

    source = 'test4'
    deck_size = 10
    n_shuffles = 9
    card = 2

    d = Deck(deck_size)
    run_deck(d, source_file=source)

    top = d.top
    off = d.offset
    print(d[card])

    nth_offset = pow(off, n_shuffles, deck_size)
    shift = geo_mod(n_shuffles, off, deck_size)
    nth_top = top * shift % deck_size

    d.offset = nth_offset
    d.top = nth_top
    print(d[card])

    input()
