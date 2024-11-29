
# 実行確認

## テスト実行
python3, pipがインストール済み前提で下記を実行

```
pip install -r requirements.txt
pytest-watch
```

## Dockerを使う場合
### コンテナの起動 & コンテナへの接続
 * Docker がインストール済み
 * Docker Compose がインストール済み

```
docker-compose up -d --build
docker-compose exec python3 bash
```

```
pytest
```

TODO: コンテナで保存すると即時テスト実行する方法

# 次は？

src/tutorial_test.py に pytestでテストを書く最低限の文法を説明します。
詳しく調べたい場合は次を参照

https://docs.pytest.org/
