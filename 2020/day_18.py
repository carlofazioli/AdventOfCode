import utilities


def tokenize(e):
    num = ''
    tokens = []
    for ch in e:
        if ch in '+*()':
            if num:
                tokens.append(int(num))
                num = ''
            tokens.append(ch)
        elif ch.isnumeric():
            num += ch
    if num:
        tokens.append(int(num))
    return tokens


def evaluate_tokens(tokens):
    stack = []
    ops = []
    while tokens:
        t = tokens.pop(0)
        if isinstance(t, int):
            stack.append(t)
        elif t in '+*':
            ops.append(t)
        elif t in '(':
            t, tokens = evaluate_tokens(tokens)
            stack.append(t)
        elif t in ')':
            return stack[0], tokens
        if len(stack) == 2:
            assert len(ops) == 1
            op = ops.pop()
            b2 = stack.pop()
            b1 = stack.pop()
            if op == '+':
                result = b1 + b2
            elif op == '*':
                result = b1 * b2
            stack.append(result)
            op = None
            b2 = None
            b1 = None
    return stack[0]


def eval_v2(tokens):
    out = []
    ops = []
    while tokens:
        t = tokens.pop(0)
        if isinstance(t, int):
            out.append(t)
            if ops and ops[-1] == '+':
                out.append(out.pop() + out.pop())
                ops.pop()
        elif t in '+*':
            ops.append(t)
        elif t == '(':
            t, tokens = eval_v2(tokens)
            out.append(t)
            if ops and ops[-1] == '+':
                out.append(out.pop() + out.pop())
                ops.pop()
        elif t == ')':
            while ops:
                out.append(out.pop() * out.pop())
                ops.pop()
            return out[0], tokens
    while ops:
        out.append(out.pop() * out.pop())
        ops.pop()
    return out[0]


if __name__ == '__main__':
    expressions = utilities.input_to_list('day_18.txt')
    expressions = [e.replace(' ', '') for e in expressions]
    tokens = [tokenize(e) for e in expressions]
    # out = [evaluate_tokens(t) for t in tokens]
    # print(sum(out))
    results = [eval_v2(t) for t in tokens]
    print(sum(results))
    # print(eval_v2(tokens[2]))
