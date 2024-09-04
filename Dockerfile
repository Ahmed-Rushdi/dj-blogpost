FROM python:slim

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /app

# Copy Python dependencies and install them
COPY requirements.txt .
RUN pip install -U pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy Node.js package files and install dependencies
COPY package*.json ./
RUN apt-get update && apt-get install -y --no-install-recommends nodejs npm \
    && npm install

# Copy the rest of the application code
COPY . .

# Run the build process for Tailwind CSS
RUN npm run build

# Clean up unnecessary files, including Node.js, npm, and related caches
RUN apt-get purge -y --auto-remove nodejs npm \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm -rf node_modules

# Expose the desired port
EXPOSE 8080

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
