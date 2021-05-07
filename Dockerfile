FROM registry.access.redhat.com/ubi8/ubi-minimal as base

# Use a build image, may have to include other build tools for wheel
RUN microdnf install python3; microdnf clean all
RUN python3 -m venv /opt/venv

COPY requirements.txt .
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r requirements.txt

# Build the runtime image
FROM registry.access.redhat.com/ubi8/ubi-minimal as run-image
RUN microdnf install python3
COPY --from=base /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /flask

EXPOSE 8080

COPY app.py .
CMD ["python3","./app.py"]
