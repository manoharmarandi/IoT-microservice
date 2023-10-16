FROM node:14-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libcairo2-dev \
    libpango1.0-dev \
    libjpeg-dev \
    libgif-dev \
    librsvg2-dev

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files into the container
COPY package*.json ./

# Install all dependencies
RUN npm install express axios chart.js canvas --only=production

# Copy the application code into the container
COPY . .

# Expose the port on which the Node.js application will run
EXPOSE 3000

# Set the entrypoint command to run the Node.js application
CMD ["npm", "start"]
