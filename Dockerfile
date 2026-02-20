FROM ubuntu:latest
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev python3-pip mediainfo

RUN wget -q "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz" && \
    tar -xvf ffmpeg-master-latest-linux64-gpl.tar.xz && \
    cp ffmpeg-master-latest-linux64-gpl/bin/* /usr/local/bin/ && \
    rm -rf ffmpeg-master-latest-linux64-gpl*
    
COPY . .
RUN pip config set global.break-system-packages true
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
