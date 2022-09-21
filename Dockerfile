FROM python:3.7

# Install nano editor just in case we need to write some file
RUN apt-get update 
RUN apt-get -y install nano 

# Install the python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files in the existing folder into /usr/src/app
WORKDIR /usr/src/app
COPY . .

# Export google application credentials to have the necessary permission
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/data-fellowship-7-c9fe8504e2f8.json"