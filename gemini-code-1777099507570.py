# hello.py
def say_hello(name):
    """사용자로부터 이름을 받아 인사말을 반환하는 함수"""
    return f"안녕하세요, {name}님! GitHub에 오신 것을 환영합니다."

if __name__ == "__main__":
    user_name = "사용자"
    print(say_hello(user_name))