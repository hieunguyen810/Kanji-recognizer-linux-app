FROM ubuntu:20.04
RUN yes | apt update 
RUN apt -y install python3
RUN apt -y install python3-pip
RUN pip3 install pyautogui
RUN pip3 install sklearn
RUN pip3 install pandas
RUN mkdir /home/kanji
WORKDIR /home/kanji
COPY index.py .
COPY recognizer.py .
# load data set
COPY .
CMD ["index.py"]