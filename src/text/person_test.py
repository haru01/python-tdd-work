import pytest

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def clear(self):
        self.name = ''
        self.age = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ArgumentError('マイナスの年齢は設定できません')
        self.__age = age

    def __str__(self):
        return 'Person{name=' + self.__name + \
            ', age=' + str(self.__age) + '}'

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.__dict__ == other.__dict__

class ArgumentError(BaseException):
    pass

def test_clear_アクセサーメソッドで確認():
    # arrange
    person = Person('Taro', 32)
    # act
    person.clear()
    # assert
    assert person.name == ''
    assert person.age == 0

def test_clear_strで確認():
    # arrange
    person = Person('Taro', 32)
    # act
    person.clear()
    # assert
    assert str(person) == 'Person{name=, age=0}'


def test_clear_eqで確認():
    # arrange
    person = Person('Taro', 32)
    # act
    person.clear()
    # assert
    assert person == Person('', 0)


def test_set_age_年齢が設定できること＿年齢が0歳以上の場合():
    # arrange
    person = Person('Taro', 32)
    # act
    person.age = 0
    # assert
    assert person.age == 0


def test_set_age_例外が投げられること＿年齢マイナスの場合():
    # arrange
    person = Person('Taro', 0)
    # act & assert
    with pytest.raises(ArgumentError, \
        match='マイナスの年齢は設定できません'):
        person.age = -1
