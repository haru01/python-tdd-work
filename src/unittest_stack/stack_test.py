import pytest
from stack import Stack, EmptyError, FullStackError


@pytest.fixture
def empty_stack():
    return Stack(10)


@pytest.fixture
def full_stack():
    stack = Stack(2)
    stack.push(10)
    stack.push(20)
    return stack


@pytest.fixture
def stack_in_10_20():
    stack = Stack(10)
    stack.push(10)
    stack.push(20)
    return stack


class TestStackIsEmpty(object):
    def test_スタックが空の場合はTrueを返すこと(self, empty_stack):
        # act & assert
        assert empty_stack.is_empty() is True

    def test_スタックが空でない場合はFlaseを返すこと(self, empty_stack):
        # arrange
        stack = empty_stack
        stack.push(10)
        # act & assert
        assert stack.is_empty() is False


class TestStackIsFull(object):
    def test_Trueを返す_満杯の場合(self, full_stack):
        # act & assert
        assert full_stack.is_full() is True

    def test_Falseを返す_満杯でない場合(self, full_stack):
        # arrange
        stack = full_stack
        stack.pop()
        # act & assert
        assert stack.is_full() is False


class TestStackSize(object):
    def test_スタックが空の場合はゼロを返すこと(self, empty_stack):
        # act & assert
        assert empty_stack.size() == 0

    def test_複数回Pushしたらその回数を返すこと(self, empty_stack):
        # arrange
        stack = empty_stack
        stack.push(10)
        stack.push(10)
        # act & assert
        assert stack.size() == 2

    def test_複数回PushAndPopしたらPushマイナスPopした回数を返すこと(self, empty_stack):
        stack = empty_stack
        stack.push(10)
        stack.push(10)
        assert stack.size() == 2
        stack.pop()
        assert stack.size() == 1
        stack.pop()
        assert stack.size() == 0


class TestStackPush(object):
    def test_１回pushでき_サイズが増えること(self, empty_stack):
        # arrange
        subject = empty_stack
        # act
        subject.push(10)
        # assert
        assert str(subject) == "<Stack:[10]>"

    def test_複数pushでき_サイズが増えること(self, empty_stack):
        # arrange
        subject = empty_stack
        # act
        subject.push(10)
        subject.push(20)
        subject.push(30)
        # assert
        assert str(subject) == "<Stack:[10, 20, 30]>"

    def test_FullStackErrorが投げられること満杯の場合(self, full_stack):
        with pytest.raises(FullStackError):
            full_stack.push(300)


class TestStackPop(object,):
    def test_１回Popできサイズが減ること＿最後に積まれた要素が取得できる(self, stack_in_10_20):
        # arrange
        subject = stack_in_10_20
        # act
        result = subject.pop()
        # assert
        assert subject.size() == 1
        assert result == 20

    def test_複数Popできサイズが減ること＿最後に積まれた要素が取得できる(self, stack_in_10_20):
        # arrange
        subject = stack_in_10_20
        # act
        resultA = subject.pop()
        resultB = subject.pop()
        # assert
        assert subject.size() == 0
        assert resultA == 20
        assert resultB == 10

    def test_EmptyErrorが投げられること空の場合(self, empty_stack):
        with pytest.raises(EmptyError):
            empty_stack.pop()


class TestStackコンストラクタ(object):
    def test_デフォルト容量は10であること(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        assert stack.is_full() is True

    def test_容量指定できること(self):
        capacity = 3
        stack = Stack(capacity)
        for i in range(capacity):
            stack.push(i)
        assert stack.is_full() is True
