FROM tensorflow/tensorflow:latest-gpu

# Env variables
ENV DEB_PYTHON_INSTALL_LAYOUT='deb'

# Full send everything to /server/ directory
WORKDIR /server
COPY . /server

# Update everything, uninstall blinker because Flask will yell if I don't 
RUN apt update && apt upgrade -y
RUN apt remove python3-blinker -y

# Let Piplups install packages (warning: not recommended)
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Run 
EXPOSE 5000
CMD [ "python", "app.py" ]
