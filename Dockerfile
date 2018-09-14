FROM python:2.7-alpine


RUN apk --update add --virtual scipy-runtime python py-pip \
    && apk add --virtual scipy-build \
        build-base python-dev openblas-dev freetype-dev pkgconfig gfortran \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && pip install --no-cache-dir numpy \ 
    && pip install --no-cache-dir matplotlib \
    && pip install --no-cache-dir scipy \
    && pip install --no-cache-dir scikit-learn \
    && apk del scipy-build \
    && apk add --virtual scipy-runtime \
        freetype libgfortran libgcc libpng  libstdc++ musl openblas tcl tk \
    && apk add bash \
    && rm -rf /var/cache/apk/*

WORKDIR .

COPY . .

CMD ["python", "run.py"]
