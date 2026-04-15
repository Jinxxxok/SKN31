def second(mm,ss):
        result =  ss + (mm * 60)
        
        return result

def solution(video_len, pos, op_start, op_end, commands):
    m, s = map(int, pos.split(':'))
    opm, ops = map(int, op_start.split(':'))
    opm1, ops1 = map(int, op_end.split(':'))
    lm, ls = map(int, video_len.split(':'))

    ss = second(m,s) # 초로 변환환 pos
    op = second(opm, ops) # 초로 변환한 op_start
    op1 = second(opm1, ops1) # 초로 변환한 op_end
    l = second(lm,ls) # 초로 변환한 video_len

    if op <= ss <= op1:
        ss = op1
    
    for cm in commands:
        if cm == 'next':
            ss += 10
            if ss > l:
                ss = l
    
        elif cm == 'prev':
            ss -= 10      
            if ss < 0:
                ss = 0
    
    if op <= ss <= op1:
        ss = op1

    m1 = ss // 60
    s1 = ss % 60

    answer = f"{m1:02d}:{s1:02d}" 
                
    return answer