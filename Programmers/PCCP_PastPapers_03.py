def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    m, s = map(int, pos.split(':'))
    opm, ops = map(int, op_start.split(':'))
    opm1, ops1 = map(int, op_end.split(':'))
    lm, ls = map(int, video_len.split(':'))

    if opm <= m <= opm1 and ops <= s <= ops1:
        m, s = opm1, ops1
    
    if commands == 'next':
        s += 10
        if s >= 60:
            m += s //60
            s %= 60
        if m > lm or (m == lm and s >= ls):
            m, s = lm, ls
    
    elif commands == 'prev':
        s -= 10      
        if s < 0:
            m += s //60
            s %= 60
        
        if m < 0:
            m, s = 0, 0
    
    if opm <= m <= opm1 and ops <= s <= ops1:
        m, s = opm1, ops1

    answer = f"{m:02d}:{s:02d}" 
                
    return answer

solution('34:33', '13:00', '00:55', '02:55', ['next','prev'])

# video_len = '34:33'

# a, b = video_len.split(':')

# print(a, b)