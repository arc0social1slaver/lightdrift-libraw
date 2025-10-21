FROM ubuntu:noble-20250127

RUN apt-get update && \
    apt-get install -y python3 python3-pip curl && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g node-gyp && \
    apt-get install -y libraw-dev

WORKDIR /home

COPY . .

CMD ["/bin/bash"]