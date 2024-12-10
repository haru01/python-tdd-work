import pytest
from stack import Stack, EmptyError, FullStackError


def empty_stack():
    return Stack(10)

def full_stack():
    stack = Stack(2)
    stack.push(10)
    stack.push(20)
    return stack


def stack_in_10_20():
    stack = Stack(10)
    stack.push(10)
    stack.push(20)
    return stack

# is_empty()のテスト
def test_スタックが空の場合はTrueを返すこと():
    # act & assert
    stack = empty_stack()
    assert stack.is_empty() is True

def test_スタックが空でない場合はFlaseを返すこと():
    # arrange
    stack = empty_stack()
    stack.push(10)
    # act & assert
    assert stack.is_empty() is False

# is_full()のテスト
def test_満杯の場合はTrueを返す():
    # act & assert
    assert full_stack().is_full() is True

def test_満杯でない場合はFalseを返す():
    # arrange
    stack = full_stack()
    stack.pop()
    # act & assert
    assert stack.is_full() is False

# size()のテスト
def test_スタックが空の場合はゼロを返すこと():
    # act & assert
    assert empty_stack().size() == 0

def test_複数回Pushしたらその回数を返すこと():
    # arrange
    stack = empty_stack()
    stack.push(10)
    stack.push(10)
    # act & assert
    assert stack.size() == 2

def test_複数回PushAndPopしたらPushマイナスPopした回数を返すこと():
    stack = empty_stack()
    # act & assert 1
    stack.push(10)
    stack.push(10)
    assert stack.size() == 2
    # act & assert 2
    stack.pop()
    assert stack.size() == 1
    # act & assert 3
    stack.pop()
    assert stack.size() == 0

# push()のテスト
def test_１回pushでき_サイズが増えること():
    # arrange
    stack = empty_stack()
    # act
    stack.push(10)
    # assert
    assert str(stack) == '<Stack:[10]>'

def test_複数pushでき_サイズが増えること():
    # arrange
    stack = empty_stack()
    # act
    stack.push(10)
    stack.push(20)
    stack.push(30)
    # assert
    assert str(stack) == '<Stack:[10, 20, 30]>'

def test_FullStackErrorが投げられること満杯の場合():
    with pytest.raises(FullStackError):
            full_stack().push(300)

# pop()のテスト
def test_１回Popできサイズが減ること＿最後に積まれた要素が取得できる():
    # arrange
    stack = stack_in_10_20()
    # act
    result = stack.pop()
    # assert
    assert stack.size() == 1
    assert result == 20

def test_複数Popできサイズが減ること＿最後に積まれた要素が取得できる():
    # arrange
    stack = stack_in_10_20()
    # act
    resultA = stack.pop()
    resultB = stack.pop()
    # assert
    assert stack.size() == 0
    assert resultA == 20
    assert resultB == 10

def test_EmptyErrorが投げられること空の場合():
    with pytest.raises(EmptyError):
        empty_stack().pop()

# is_full()のテスト
def test_デフォルト容量は10であること():
    stack = Stack()
    for i in range(10):
        stack.push(i)
    assert stack.is_full() is True

def test_容量指定できること():
    capacity = 3
    stack = Stack(capacity)
    for i in range(capacity):
        stack.push(i)
    assert stack.is_full() is True
