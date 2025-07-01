# Learning: Multi-stage build for React TypeScript application
FROM node:20-alpine as base

# Learning: Set working directory
WORKDIR /app

# Learning: Copy package files for dependency installation
COPY package*.json ./

# Development stage
FROM base as development

# Learning: Install all dependencies (including devDependencies)
RUN npm ci

# Learning: Copy source code
COPY . .

# Learning: Expose port
EXPOSE 3000

# Learning: Command for development with hot reload
CMD ["npm", "run", "dev"]

# Build stage
FROM base as build

# Learning: Install dependencies
RUN npm ci --only=production && npm cache clean --force

# Learning: Copy source code
COPY . .

# Learning: Build the application
RUN npm run build

# Production stage
FROM nginx:alpine as production

# Learning: Copy built application to nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Learning: Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Learning: Expose port
EXPOSE 80

# Learning: Start nginx
CMD ["nginx", "-g", "daemon off;"]