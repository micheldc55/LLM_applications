# Start from a core stack version
FROM python:3.11-slim-buster

# Name the workspace in the container
WORKDIR /workspace

# Add the f**** certificate
ADD zscaler.pem /usr/local/share/ca-certificates/zscaler.pem

# Update certificate store
RUN chmod 644 /usr/local/share/ca-certificates/zscaler.pem && update-ca-certificates

ENV REQUESTS_CA_BUNDLE=/usr/local/share/ca-certificates/zscaler.pem

# Copy requirements.txt to container
COPY requirements.txt ./requirements.txt

# Updating pip and nstall dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port (on CONTAINER!)
EXPOSE 8501

# Run the command to start the app (not working)
CMD ["streamlit", "run", "app.py"]
