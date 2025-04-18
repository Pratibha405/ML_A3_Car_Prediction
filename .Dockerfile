FROM python:3.12.6-bookworm

WORKDIR /root/code

RUN pip3 install dash
RUN pip3 install pandas
RUN pip3 install dash_bootstrap_components
RUN pip3 install numpy
RUN pip3 install scikit-learn
RUN pip3 install matplotlib
RUN pip3 install mlflow 
RUN pip3 install joblib
RUN pip3 install cloudpickle 

# Testing module
RUN pip3 install dash[testing]
RUN pip3 install pytest
RUN pip3 install pytest-depends


COPY ./code /root/code

CMD tail -f /dev/null