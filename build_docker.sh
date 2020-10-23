docker rm -f hlju
docker build -t hlju . && \
docker run --name=hlju --rm -itd hlju