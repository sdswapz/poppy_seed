# Docker Setup for Poppy Seed

This guide provides instructions for running Poppy Seed using Docker and Docker Compose.

## Prerequisites

### Install Docker

#### macOS
```bash
# Install Docker Desktop for Mac
# Download from: https://www.docker.com/products/docker-desktop/

# Or install via Homebrew
brew install --cask docker
```

#### Linux (Ubuntu/Debian)
```bash
# Update package index
sudo apt-get update

# Install Docker
sudo apt-get install docker.io docker-compose

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group (optional)
sudo usermod -aG docker $USER
```

#### Windows
- Download Docker Desktop for Windows from: https://www.docker.com/products/docker-desktop/
- Install and restart your computer

### Verify Installation
```bash
docker --version
docker-compose --version
```

## Quick Start

### Development Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sdswapz/poppy_seed.git
   cd poppy_seed
   ```

2. **Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. **Access the application**:
   - Main Interface: http://localhost:8000/
   - Upload Page: http://localhost:8000/
   - About Page: http://localhost:8000/about/
   - Repository: http://localhost:8000/repo/

### Production Environment

1. **Set up environment variables**:
   ```bash
   cp env.example .env
   # Edit .env file with your production settings
   ```

2. **Run production setup**:
   ```bash
   docker-compose -f docker-compose.prod.yml up --build -d
   ```

3. **Access via Nginx**:
   - Main Interface: http://localhost/
   - All traffic is proxied through Nginx

## Docker Commands

### Basic Commands

```bash
# Build and start containers
docker-compose up --build

# Start in background (detached mode)
docker-compose up -d

# Stop containers
docker-compose down

# View logs
docker-compose logs -f

# Rebuild specific service
docker-compose build poppy-seed

# Execute commands in container
docker-compose exec poppy-seed python manage.py shell
docker-compose exec poppy-seed python manage.py createsuperuser
```

### Database Commands

```bash
# Run migrations
docker-compose exec poppy-seed python manage.py migrate

# Create superuser
docker-compose exec poppy-seed python manage.py createsuperuser

# Collect static files
docker-compose exec poppy-seed python manage.py collectstatic --noinput
```

### Maintenance Commands

```bash
# View container status
docker-compose ps

# View resource usage
docker stats

# Clean up unused containers and images
docker system prune -a

# Backup database
docker-compose exec poppy-seed cp db.sqlite3 /app/backup_$(date +%Y%m%d).sqlite3
```

## Configuration

### Environment Variables

Copy `env.example` to `.env` and configure:

```bash
# Django Settings
SECRET_KEY=your-secret-key-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database
DATABASE_URL=sqlite:///db.sqlite3

# File Upload Settings
MAX_UPLOAD_SIZE=104857600  # 100MB
```

### Volume Mounts

The Docker setup includes volume mounts for:
- **Database**: Persistent SQLite database
- **Media Files**: Uploaded APK files and analysis results
- **Static Files**: CSS, JavaScript, and other static assets

### Port Configuration

- **Development**: Port 8000 (Django development server)
- **Production**: Port 80/443 (Nginx reverse proxy)

## Troubleshooting

### Common Issues

1. **Port Already in Use**:
   ```bash
   # Change port in docker-compose.yml
   ports:
     - "8001:8000"  # Use port 8001 instead
   ```

2. **Permission Issues**:
   ```bash
   # Fix file permissions
   sudo chown -R $USER:$USER .
   ```

3. **Container Won't Start**:
   ```bash
   # Check logs
   docker-compose logs poppy-seed
   
   # Rebuild without cache
   docker-compose build --no-cache
   ```

4. **Database Issues**:
   ```bash
   # Reset database
   docker-compose down -v
   docker-compose up --build
   ```

### Health Checks

The containers include health checks:
```bash
# Check container health
docker-compose ps

# Manual health check
docker-compose exec poppy-seed python manage.py check --deploy
```

## Security Considerations

### Production Deployment

1. **Change Default Secrets**:
   - Update `SECRET_KEY` in `.env`
   - Use strong passwords for database
   - Enable HTTPS with SSL certificates

2. **Network Security**:
   - Use Docker networks for service isolation
   - Configure firewall rules
   - Enable rate limiting in Nginx

3. **File Upload Security**:
   - Validate file types and sizes
   - Scan uploaded files for malware
   - Store files in isolated volumes

### Container Security

```bash
# Run as non-root user (add to Dockerfile)
USER 1000:1000

# Use specific image tags
FROM python:3.9-slim@sha256:...

# Regular security updates
docker-compose pull
docker-compose up --build
```

## Monitoring and Logging

### Log Management

```bash
# View application logs
docker-compose logs -f poppy-seed

# View Nginx logs
docker-compose logs -f nginx

# Log rotation (add to crontab)
0 0 * * * docker-compose exec poppy-seed find /app/logs -name "*.log" -mtime +7 -delete
```

### Performance Monitoring

```bash
# Monitor resource usage
docker stats

# Check container health
docker-compose ps
```

## Backup and Recovery

### Database Backup

```bash
# Create backup
docker-compose exec poppy-seed python manage.py dumpdata > backup.json

# Restore backup
docker-compose exec poppy-seed python manage.py loaddata backup.json
```

### Volume Backup

```bash
# Backup volumes
docker run --rm -v poppy_seed_media_data:/data -v $(pwd):/backup alpine tar czf /backup/media_backup.tar.gz -C /data .
docker run --rm -v poppy_seed_db_data:/data -v $(pwd):/backup alpine tar czf /backup/db_backup.tar.gz -C /data .
```

## Scaling

### Horizontal Scaling

```bash
# Scale the application
docker-compose up --scale poppy-seed=3

# Use load balancer
# Configure Nginx upstream with multiple instances
```

### Resource Limits

```yaml
# Add to docker-compose.yml
services:
  poppy-seed:
    deploy:
      resources:
        limits:
          memory: 1G
          cpus: '0.5'
        reservations:
          memory: 512M
          cpus: '0.25'
```

## Support

For Docker-related issues:
- Check container logs: `docker-compose logs`
- Verify Docker installation: `docker --version`
- Review configuration files
- Check port availability: `netstat -tulpn | grep :8000`
