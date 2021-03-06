FROM alpine:edge

EXPOSE 8118 9050

RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' \
    >> /etc/apk/repositories && \
    apk --update add privoxy tor@testing runit@testing && \
    echo 'MaxCircuitDirtiness 30' \
        >> /etc/tor/torrc

COPY service /etc/service/

CMD ["runsvdir", "/etc/service"]
