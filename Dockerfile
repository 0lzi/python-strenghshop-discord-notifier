FROM --platform=${BUILDPLATFORM} python:3.9-alpine

# Install dependencies
RUN apk update && apk add --no-cache build-base libxml2-dev libxslt-dev

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY main.py .

# Install Python dependencies
RUN pip install requests beautifulsoup4 discord-webhook

# Add cron job to execute the script daily
RUN echo "0 0 * * * python /app/scraper.py" > /etc/crontabs/root

# Start cron in the foreground
CMD ["crond", "-f"]
