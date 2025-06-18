# Dockerfile (inside frontend/)
FROM node:20-slim

# Set environment variable for backend URL
ENV BACKEND_URL=http://host.docker.internal:8000/api

# Create and switch to app directory
WORKDIR /app

# Copy package.json and package-lock.json first
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy rest of the app code
COPY . .

# Expose frontend port
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
