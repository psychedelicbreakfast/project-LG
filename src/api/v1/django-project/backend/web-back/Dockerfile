# Python実行環境のDockerイメージを指定
FROM python:3.9.4

# pycファイルを残さないように設定
ENV PYTHONDONTWRITEBYTECODE 1

# Pythonの標準出力、標準エラー出力をバッファに保存しないように設定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを/code配下へ変更
WORKDIR /code

# requirements.txtへ記述したライブラリをインストール
COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# ビルドコンテキストのファイルを/code配下へコピー
COPY . ./

# コンテナのポートを公開
EXPOSE 8000
