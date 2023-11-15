FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt inside app directory
COPY ./requirements.txt /app

# Install all the app dependencies from requirements.txt 
RUN pip install -r requirements.txt

# Copy app source code
COPY . .

# Expose port 5000 as the app will run on port 5000
EXPOSE 5000

# Define the FLASK_APP environment variable
ENV FLASK_APP=app.py

# Specify the command to start the app
CMD ["flask", "run", "--host", "0.0.0.0"]