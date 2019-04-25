FROM python

# Add requirements (to leverage Docker cache)
COPY requirements.txt /tmp/requirements.txt

# Install requirements
RUN pip install -r /tmp/requirements.txt
