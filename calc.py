__version__ = 0.1 #변수

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# 실행코드
print(__name__)
if __name__ == '__main__':
    result = minus(10, 5)
    print(result)