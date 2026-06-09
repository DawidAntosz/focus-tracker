# Build stage
FROM node:23-alpine as build

WORKDIR /usr/server

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install --legacy-peer-deps

# Copy source files
COPY . .

# Build the React app
RUN npm run build

# Production stage
FROM node:23-alpine

WORKDIR /usr/server

# Install serve globally to serve the build
RUN npm install -g serve

# Copy the build output
COPY --from=build /usr/server/dist ./dist

# Expose port 80
EXPOSE 80

# Run serve to serve the React app
CMD ["nginx", "-g", "daemon off;"]
