# learn_gcp

## キャプチャ

![推論](https://user-images.githubusercontent.com/36921282/80777217-647a0280-8b9f-11ea-9057-ef96579f987a.gif)

## 環境構築

### Docker

GAE 用( `./analytics/Dockerfile` )と GCE 用( `./analytics/Dockerfile` )にそれぞれ Docker を立てる

```
# build
docker build -t <image name> .
# run
docker run --volume <マウント元>:<マウント先> -itd --name <container name> -p 8080:8080 <image name> bash
```

### GCP サービスの認証

コンテナ上で下記を実行する

```
gcloud auth login
gcloud config set project <pjoject id>
```
