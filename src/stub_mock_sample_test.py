import random


# Stub(関節入力, patchを使わずに、コンストラクターインジェクション)
# テストしたい対象
class Geeting:
    def __init__(self, my_hour):
        self.my_hour = my_hour

    def hoge(self):
        try:
            # 関節入力の結果によって振る舞いが変わる
            x = self.my_hour.hour()
            if x in [7, 8, 9, 10, 11]:
                return 'Good Moring'
            else:
                return 'Hi'
        except IOError:
            return 'Fail!'


# スタブで差し替え関節入力をコントロールしたい対象
class MyHour:
    def hour(self):
        pass


class TestGeeting:
    def create_sut(self, mocker):
        my_hour_stub = mocker.Mock()
        print(my_hour_stub)
        return Geeting(my_hour_stub), my_hour_stub

    def test_hoge_return_Good_Morning_when_MyHour_return_from_7_to_11(self, mocker):
        sut, my_hour_stub = self.create_sut(mocker)

        my_hour_stub.hour = mocker.MagicMock(return_value=7)
        assert sut.hoge() == 'Good Moring'

        my_hour_stub.hour = mocker.MagicMock(return_value=11)
        assert sut.hoge() == 'Good Moring'

    def test_hoge_return_Hi_when_MyHour_else_hour(self, mocker):
        sut, my_hour_stub = self.create_sut(mocker)

        my_hour_stub.hour = mocker.MagicMock(return_value=6)
        assert sut.hoge() == 'Hi'
        my_hour_stub.hour = mocker.MagicMock(return_value=12)
        assert sut.hoge() == 'Hi'

    def test_hoge_return_Fail_when_MyHour_return_IOError(self, mocker):
        sut, my_hour_stub = self.create_sut(mocker)
        my_hour_stub.hour = \
            mocker.MagicMock(side_effect=IOError())
        # act & assert
        assert sut.hoge() == 'Fail!'


# Mock(関節出力, patchを使わずに、コンストラクターインジェクション)
# テストしたい対象
class XxxService:
    def __init__(self, sender):
        self.sender = sender

    def send_reverse(self, message):
        if len(message) == 0:
            return
        self.sender.send(message[::-1])  # 関節出力の検証をしたい箇所


# Mockで差し替えて関節出力を検証したい
class Sender:
    def send(self, message):
        pass


class TestXxxService:
    def create_service_sender(self, mocker):
        sender_mock = mocker.Mock()
        sender_mock.send = mocker.MagicMock()
        return XxxService(sender_mock), sender_mock

    def test_send_reverse_文字列反転してsendすること(self, mocker):
        # arrange
        service, sender_mock = self.create_service_sender(mocker)
        # act
        service.send_reverse('abc')
        # assert
        sender_mock.send.assert_called_once_with('cba')

    def test_send_reverse_空文字メッセージならsendしないこと(self, mocker):
        # arrange
        service, sender_mock = self.create_service_sender(mocker)
        # act
        service.send_reverse('')
        # assert
        sender_mock.send.assert_not_called()


# patchの利用例
def a_or_b():
    r = random.randint(1, 2)
    if r == 1:
        return 'A'
    else:
        return 'B'


def test_a_or_b_return_A_if_random_is_1(mocker):
    mocker.patch('random.randint', return_value=1)
    assert a_or_b() == 'A'


def test_a_or_b_return_A_if_random_is_2(mocker):
    mocker.patch('random.randint', return_value=2)
    assert a_or_b() == 'B'

# モックの詳細は
# https://pypi.org/project/pytest-mock/
# https://docs.python.org/ja/3/library/unittest.mock.html
