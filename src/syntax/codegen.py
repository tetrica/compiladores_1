class __buffer:
    i = 0
    fifo = []

def gera(op, dir, sep, esq):
    __buffer.fifo.append(f"[{op} {dir} {sep} {esq} {'-' if not sep else ''}]")
    print(__buffer.fifo)
def geratemp():
    __buffer.i += 1
    return f"t{__buffer.i}"

def remenda(quad, cmd, side, idx, sep):
    # __buffer.fifo.append(f"[{cmd} {quad} {inx} {esq} {'-' if not sep else ''}]")
    pass
def current_list_code_index():
    return len(__buffer.fifo)