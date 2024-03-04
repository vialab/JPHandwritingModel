FROM tensorflow/tensorflow:2.14.0-gpu

# Env variables
ENV DEB_PYTHON_INSTALL_LAYOUT='deb'

RUN apt remove python3-blinker -y

# Full send everything to /server/ directory
WORKDIR /server

COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .

# Run on all addresses, port 5000
EXPOSE 5000
CMD [ "python", "app.py", "--host=0.0.0.0 --port=5000" ]