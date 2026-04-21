# simple_memo.py

# 1. 저장할 파일명 사용자로부터 입력받기
file_path = input('저장할 파일명 입력:')
print('저장할 내용을 입력하세요. 다 입력하면 !q를 입력하세요.')
# 2. 1의 파일과 연결
with open(file_path, mode='wt', encoding= 'utf-8') as fw:
# 3. 사용자로부터 저장할 문자를 입력받고 그것을 파일에 출력
    line_input = input('>>>')
    while line_input != '!q':
        fw.write(line_input+'\n')
        line_input = input('>>>')
# 4. 3을 반복 !q가 나오기 전까지.

with open(file_path, mode='rt', encoding= 'utf-8') as fr:
    txt = fr.read()

print(txt)