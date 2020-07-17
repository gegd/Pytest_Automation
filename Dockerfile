FROM python:3.6.8
WORKDIR .
ADD . .
RUN pip install -r requirements.txt
CMD ["pytest", "-q","/cases","--alluredir","allure-results"]