docker rm -f hlju
docker build -t hlju . && \
docker run --name=hlju -v /etc/localtime:/etc/localtime  -itd hlju
