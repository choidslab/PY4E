class PartyAnimal:
    x = 0
    # 객체 생성자, 초기화
    def __init__(self, name):
        self.name = name
        print(self.name, "Constructor!")

    def party(self):
        self.x = self.x + 1
        print("So far",self.x)

    # 객체 소멸자, 할당된 메모리 해제, 일반적으로 자동 호출
    def __del__(self):
        print("Destructor!")

# 객체 생성
an = PartyAnimal("Timothy!")

# 객체 메소드 호출
an.party()
an.party()
an.party()

an.x = 30
print('an contain ', an.x)
