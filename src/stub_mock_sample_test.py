import random


# Stub(関節入力, patchを使わずに、コンストラクターインジェクション)
# テストしたい対象
class SUT:
    def __init__(self, doc):
        self.doc = doc

    def hoge(self):
        try:
            # 関節入力の結果によって振る舞いが変わる
            x = self.doc.one_or_two_or_IOError()
            if x == 1:
                return "A"
            else:
                return "B"
        except IOError:
            return "Fail"


# スタブで差し替え関節入力をコントロールしたい対象
class DOC:
    def one_or_two_or_IOError(self):
        pass


class TestSUT:
    def create_sut(self, mocker):
        doc_stub = mocker.Mock()
        print(doc_stub)
        return SUT(doc_stub), doc_stub

    def test_hoge_return_A_when_DOC_return_1(self, mocker):
        sut, doc_stub = self.create_sut(mocker)
        doc_stub.one_or_two_or_IOError = mocker.MagicMock(return_value=1)
        # act & assert
        assert sut.hoge() == "A"

    def test_hoge_return_A_when_DOC_return_2(self, mocker):
        sut, doc_stub = self.create_sut(mocker)
        doc_stub.one_or_two_or_IOError = mocker.MagicMock(return_value=2)
        # act & assert
        assert sut.hoge() == "B"

    def test_hoge_return_A_when_DOC_return_IOError(self, mocker):
        sut, doc_stub = self.create_sut(mocker)
        doc_stub.one_or_two_or_IOError = \
            mocker.MagicMock(side_effect=IOError())
        # act & assert
        assert sut.hoge() == "Fail"


# Mock(関節出力, patchを使わずに、コンストラクターインジェクション)
# テストしたい対象
class SUT2:
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


class TestSUT2:
    def create_sut2_sender(self, mocker):
        sender_mock = mocker.Mock()
        sender_mock.send = mocker.MagicMock()
        return SUT2(sender_mock), sender_mock

    def test_send_reverse_文字列反転してsendすること(self, mocker):
        # arrange
        sut2, sender_mock = self.create_sut2_sender(mocker)
        # act
        sut2.send_reverse("abc")
        # assert
        sender_mock.send.assert_called_once_with("cba")

    def test_send_reverse_空文字メッセージならsendしないこと(self, mocker):
        # arrange
        sut2, sender_mock = self.create_sut2_sender(mocker)
        # act
        sut2.send_reverse("")
        # assert
        sender_mock.send.assert_not_called()


# patchの利用例
def a_or_b():
    r = random.randint(1, 2)
    if r == 1:
        return "A"
    else:
        return "B"


def test_a_or_b_return_A_if_random_is_1(mocker):
    mocker.patch("random.randint", return_value=1)
    assert a_or_b() == "A"


def test_a_or_b_return_A_if_random_is_2(mocker):
    mocker.patch("random.randint", return_value=2)
    assert a_or_b() == "B"

# モックの詳細は
# https://pypi.org/project/pytest-mock/
# https://docs.python.org/ja/3/library/unittest.mock.html
