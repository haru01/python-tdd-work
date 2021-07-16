import pytest


def div(a, b):
    return a / b


# メソッド名のプレフィックスは[test]
def test_assert_equal比較で検証():
    # assert
    assert 1 + 1 == 2
    assert div(12, 4) == 3, 'assertで検証'


# 例外のテスト
def test_div_ZeroDivisionErrorが発生すること_zeroで割った場合():
    with pytest.raises(ZeroDivisionError, match='division by zero'):
        div(10, 0)


# パラメタライズテスト 12/4=3, 10/5=2, 100/25=4
@pytest.mark.parametrize(
    'a, b, expected',
    [(12, 4, 3),
     (10, 5, 2),
     (100, 25, 4)],
)
def test_div_できること(a, b, expected):
    assert div(a, b) == expected


# assertの落ち葉拾い
def test_assert_inで含んでいるか検証():
    assert 'abc' in 'aaabcde'
    assert 20 in [10, 20, 30]


def test_イコールの否定():
    assert 1 + 1 != 1


def test_不等号():
    assert 3 > 2
    assert 3 >= 3


def test_TrueFalse():
    assert True
    assert not False
    assert isinstance('abc', str) is True
    assert isinstance(1, str) is False


# classでグルーピング
# クラス名のプレフィックスは[Test]
class TestDiv_割り算について(object):
    def test_割り算ができること(self):
        assert div(12, 4) == 3

    def test_例外を投げること_0で割った場合(self):
        with pytest.raises(ZeroDivisionError):
            div(10, 0)


# フィクスチャによる前提データの準備
class TestFixtureSample(object):
    @pytest.fixture
    def empty_list(self):
        return []

    @pytest.fixture
    def three_size_list(self):
        return [10, 20, 30]

    def test_xx(self, empty_list):
        assert len(empty_list) == 0
        assert empty_list == []

    def test_list_size_threeの場合(self, three_size_list):
        assert len(three_size_list) == 3
        assert three_size_list == [10, 20, 30]


# フィクスチャによるSetup, Teardown
global global_users
global_users = ['user0']


class TestFixtureSetupTeardown(object):
    @pytest.fixture
    def users(self):
        # 前処理
        global global_users
        temp = global_users.copy()
        global_users.append('userA')
        # テスト実行の際に引数で引き渡し
        yield global_users
        # 後処理
        global_users = temp
        assert global_users == ['user0']

    def test_appendB(self, users):
        users.append('userB')
        assert users == ['user0', 'userA', 'userB']

    def test_appendC(self, users):
        users.append('userC')
        assert users == ['user0', 'userA', 'userC']

# # スコープによって実行回数が異なる フィクスチャ
# # TODO
