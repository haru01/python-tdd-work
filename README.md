# 前提条件
 * Docker がインストール済み
 * Docker Compose がインストール済み

# 実行確認

### コンテナの起動 & コンテナへの接続
```
docker-compose up -d --build
docker-compose exec python3 bash
```

### pytestを 実行する場合(コンテナに接続後)
```
pytest
```

### watch-testを実行する場合(コンテナに接続後)
```
pytest-watch
```

## dockerを使わない場合

python3, pipがインストール済み前提で下記を実行

```
pip install -r requirements.txt
pytest-watch
```

# 次は？

src/tutorial_test.py に pytestでテストを書く最低限の文法を説明します。
詳しく調べたい場合は次を参照

https://docs.pytest.org/
