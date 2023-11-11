<div align="center">
  <br>
  <p>
    <img src="https://github.com/qvco/mindreader-ai/assets/77382767/50e8a50a-6f6b-4bd9-9880-5b527c716eb7" width="500px">
  </p>
  <h3>MindReader AI</h3>
   <p>
        MindReader AIのソースコード<br />
        <br />
        <br />
        <a href="https://github.com/qvco/yaylib">
            <strong>Yay! のライブラリはこちらから »</strong>
        </a>
        <br />
        <br />
        <a href="https://github.com/qvco/mindreader-ai/issues">Report Bug</a>
        ·
        <a href="https://github.com/qvco/mindreader-ai/issues">Request Feature</a>
        ·
        <a href="https://discord.gg/MEuBfNtqRN">Join the discord</a>
    </p>
</div>

## Installation

**※ Python 3.10 以上のバージョンが必要です。**

1. リポジトリをクローン:

```bash
git clone https://github.com/qvco/mindreader-ai.git
```

2. MindReader AI のディレクトリに移動:

```bash
cd mindreader-ai
```

3. (推奨) プログラム実行用の仮想環境を作成:

```bash
py -m venv venv
```

4. 仮想環境を起動する

   - Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   - MacOS or Linux

   ```bash
   source venv/bin/activate
   ```

5. `requirements.txt`から依存モジュールのインストール:

```bash
pip install -r requirements.txt
```

6. `.env.example`を参考に`.env`ファイルを作成し、環境変数を設定:

```sh
YAY_ACCOUNT_EMAIL=Yayで使用しているメールアドレス
YAY_ACCOUNT_PASSWORD=Yayで使用しているパスワード
ROOT_POST_ID=起点にする投稿のID
DB_PATH=.unchi
```

7. MindReader AI を実行する:

```
py main.py
```

## Links

## Help

もしドキュメントを読んでもわからないことがあったり、なかなか解決しない問題があった場合は、遠慮なく ライブラリの公式 [Discord サーバー](https://discord.gg/Y8f2K74URa)に参加してください！
