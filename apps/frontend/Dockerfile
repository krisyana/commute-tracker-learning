# Learning: Simple Dockerfile for React TypeScript application with Vite
FROM node:20-alpine

# Learning: Install pnpm
RUN npm install -g pnpm

# Learning: Set working directory
WORKDIR /app

# Learning: Copy package files for dependency installation
COPY package*.json pnpm-lock.yaml* ./

# Learning: Install dependencies using pnpm
RUN pnpm install

# Learning: Copy source code
COPY . .

# Learning: Expose port
EXPOSE 3000

# Learning: Command for development with hot reload
CMD ["pnpm", "run", "dev"]