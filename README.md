# learn_gcp



## 環境構築

```
# From Dockerfile directory
## build
docker build -t <image name> .
## run
docker run --volume <マウント元>:<マウント先> -itd --name <container name> -p 8080:8080 <image name> bash
```

