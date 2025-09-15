#!/bin/bash

# Poppy Seed Docker Run Script
# This script provides easy Docker commands for Poppy Seed

echo "🐳 Poppy Seed Docker Management"
echo "==============================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "   • macOS: Download Docker Desktop from https://www.docker.com/products/docker-desktop/"
    echo "   • Linux: sudo apt-get install docker.io docker-compose"
    echo "   • Windows: Download Docker Desktop from https://www.docker.com/products/docker-desktop/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Function to show usage
show_usage() {
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  start     - Start Poppy Seed in development mode"
    echo "  stop      - Stop all containers"
    echo "  restart   - Restart all containers"
    echo "  build     - Build containers"
    echo "  logs      - Show container logs"
    echo "  shell     - Open shell in Poppy Seed container"
    echo "  prod      - Start in production mode"
    echo "  clean     - Clean up containers and images"
    echo "  status    - Show container status"
    echo ""
}

# Function to start development environment
start_dev() {
    echo "🚀 Starting Poppy Seed in development mode..."
    docker-compose up --build -d
    echo ""
    echo "📱 Access the application at:"
    echo "   • Main Interface: http://localhost:8000/"
    echo "   • Upload Page: http://localhost:8000/"
    echo "   • About Page: http://localhost:8000/about/"
    echo "   • Repository: http://localhost:8000/repo/"
    echo ""
    echo "📊 View logs with: $0 logs"
    echo "🛑 Stop with: $0 stop"
}

# Function to start production environment
start_prod() {
    echo "🏭 Starting Poppy Seed in production mode..."
    docker-compose -f docker-compose.prod.yml up --build -d
    echo ""
    echo "📱 Access the application at:"
    echo "   • Main Interface: http://localhost/"
    echo "   • All traffic proxied through Nginx"
    echo ""
    echo "📊 View logs with: $0 logs"
    echo "🛑 Stop with: $0 stop"
}

# Function to stop containers
stop_containers() {
    echo "🛑 Stopping Poppy Seed containers..."
    docker-compose down
    docker-compose -f docker-compose.prod.yml down 2>/dev/null || true
    echo "✅ Containers stopped"
}

# Function to show logs
show_logs() {
    echo "📊 Showing Poppy Seed logs..."
    docker-compose logs -f
}

# Function to open shell
open_shell() {
    echo "🐚 Opening shell in Poppy Seed container..."
    docker-compose exec poppy-seed /bin/bash
}

# Function to show status
show_status() {
    echo "📊 Container Status:"
    docker-compose ps
}

# Function to clean up
cleanup() {
    echo "🧹 Cleaning up Docker resources..."
    docker-compose down -v
    docker-compose -f docker-compose.prod.yml down -v 2>/dev/null || true
    docker system prune -f
    echo "✅ Cleanup completed"
}

# Main script logic
case "${1:-start}" in
    "start")
        start_dev
        ;;
    "stop")
        stop_containers
        ;;
    "restart")
        stop_containers
        start_dev
        ;;
    "build")
        echo "🔨 Building Poppy Seed containers..."
        docker-compose build
        ;;
    "logs")
        show_logs
        ;;
    "shell")
        open_shell
        ;;
    "prod")
        start_prod
        ;;
    "clean")
        cleanup
        ;;
    "status")
        show_status
        ;;
    "help"|"-h"|"--help")
        show_usage
        ;;
    *)
        echo "❌ Unknown command: $1"
        show_usage
        exit 1
        ;;
esac
