FROM centos:7

RUN yum update -y
RUN yum groupinstall -y "Development Tools"
RUN yum install -y \
    kernel-devel kernel-headers \
    gcc gcc-c++ \
    patch libyaml-devel libffi-devel \
    autoconf automake make \
    libtool bison \
    tk-devel \
    zip wget tar zlib zlib-devel \
    bzip2 bzip2-devel \
    readline readline-devel \
    sqlite sqlite-devel \
    openssl openssl-devel \
    git \
    gdbm-devel \
    python-devel 

# apacheのインストール
RUN yum install -y httpd
RUN systemctl enable httpd

# python3のインストール
WORKDIR /root
RUN wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
RUN tar xzvf Python-3.9.1.tgz
WORKDIR /root/Python-3.9.1
RUN LD_RUN_PATH=/usr/local/lib ./configure
RUN LD_RUN_PATH=/usr/local/lib make
RUN LD_RUN_PATH=/usr/local/lib make install
# python3をpythonコマンドで使用できるように
# yumが動かなかったのでコメントアウト
# python3コマンドで実行
# RUN mv /usr/bin/python /usr/bin/python.bk
# RUN ln -s /usr/local/bin/python3 /usr/local/bin/python

RUN pip3 install readline
RUN pip3 install virtualenv

# Flask
RUN pip3 install flask
RUN pip3 install flask_restful
RUN pip3 install mysql-connector-python
RUN pip3 install sqlalchemy
RUN pip3 install pymysql
RUN pip3 install flask-sqlalchemy
RUN pip3 install flask-migrate

# Django
RUN pip3 install Django==3.1.2
RUN pip3 install django-cors-headers==3.4.0
RUN pip3 install djangorestframework==3.11.1
RUN pip3 install djangorestframework-simplejwt==4.6.0
RUN pip3 install djoser==2.0.3
RUN pip3 install python-decouple
RUN pip3 install dj-database-url
RUN pip3 install dj_static

# 自動フォーマットライブラリ
RUN pip3 install autopep8

WORKDIR /var/www/html

ENV TZ Asia/Tokyo

CMD ["/sbin/init"]

EXPOSE 80
EXPOSE 443
EXPOSE 22
# Flaskのデフォルトポート
EXPOSE 5000
# Djangoのデフォルトポート
EXPOSE 8000