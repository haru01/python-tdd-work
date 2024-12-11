def game_score(rolls):
    score = 0
    frame_index = 0
    for i in range(10):
        score += rolls[frame_index + 0] + rolls[frame_index + 1]
        frame_index += 2
    return score

# def test_スペアありのスコアが計算できること():
#     # assert
#     assert game_score([7,3, 2,1, 0,0, 0,0, 0,0,
#                        0,0, 0,0, 0,0, 0,0, 0,0,]) == 15

# def test_最終フレームがスペアありのスコアが計算できること():
#     # assert
#     assert game_score([0,0, 0,0, 0,0, 0,0, 0,0,
#                        0,0, 0,0, 0,0, 0,0, 7,3,4]) == 14

# def test_ストライクありのスコアが計算できること():
#     # assert
#     assert game_score([10, 2,3, 0,0, 0,0, 0,0,
#                        0,0, 0,0, 0,0, 0,0, 0,0]) == sum([10, 2,3,]) + sum([2,3])


def test_ボーナス計算なしの場合にスコアが計算できること():
    # assert
    assert game_score([1,1, 1,1, 1,1, 1,1, 1,1,
                       1,1, 1,1, 1,1, 1,1, 1,1,]) == 20