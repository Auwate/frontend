FROM debian:bullseye
# OS we want
RUN apt update && apt-get upgrade -y
# Update and upgrade os software
RUN apt-get install -y git python3-pip
# Get necessary packages
WORKDIR /opt
# Clone
RUN git clone https://github.com/Auwate/frontend.git

WORKDIR /opt/frontend

RUN pip install -r requirements.txt

WORKDIR /opt/frontend/frontend

EXPOSE 80

CMD [ "python3", "-m", "streamlit", "run", "HCI_Frontend.py", "--server.port 80" ]