#FROM centos:6.7
FROM python:3
#RUN yum update -y
#RUN yum -y install epel-release
#RUN yum -y install python36u
#RUN yum -y install python36u-pip
#RUN yum -y install python36u-devel
#RUN yum install -y python36u python36u-pip python36u-devel
#RUN yum clean all

RUN pip3.6 install flask

COPY . /app
WORKDIR /app

ENTRYPOINT ["python3.6"]
EXPOSE 80
CMD ["app.py"]

