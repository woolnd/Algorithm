def to_sec(t):
    m, s = map(int, t.split(":"))
    return m * 60 + s

def to_str(sec):
    m, s = divmod(sec, 60)
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    v = to_sec(video_len)
    s = to_sec(pos)
    op_s = to_sec(op_start)
    op_e = to_sec(op_end)

    for command in commands:
        if op_s <= s <= op_e:
            s = op_e

        if command == 'next':
            s = min(s + 10, v)
        elif command == 'prev':
            s = max(s - 10, 0)

    if op_s <= s <= op_e:
        s = op_e

    return to_str(s)