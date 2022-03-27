FROM registry.access.redhat.com/ubi8/python-38

# Add application sources with correct permissions for OpenShift
USER 0
ADD . .
RUN chown -R 1001:0 ./
USER 1001

# Install the dependencies
RUN pip install -U pip && \
    pip install -r requirements.txt

# Run the application
CMD python manage.py runserver 0.0.0.0:8080
