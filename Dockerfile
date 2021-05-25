FROM python:3
ENV PIP_NO_CACHE_DIR=1
# RUN pip install --upgrade pip && pip install \
#     'Django>=3.0,<4.0' \
#     'psycopg2-binary>=2.8' \
#     'Pillow>=8.0.0'\
#     'django-filter>=2.4.0'\
#     'djangorestframework>=3.12.4'\
#     'Markdown>=3.3.4'


WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

ADD ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]