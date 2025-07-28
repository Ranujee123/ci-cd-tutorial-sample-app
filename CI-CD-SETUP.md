# CI/CD Pipeline Setup Guide

This guide explains how to set up the CI/CD pipeline for your Flask application using GitHub Actions.

## 🚀 Pipeline Overview

The pipeline includes:
- **Continuous Integration**: Automated testing and building
- **Security Scanning**: Vulnerability detection with Trivy
- **Multi-Environment Deployment**: Development and Staging environments
- **Docker-based Deployment**: Containerized application deployment

## 📋 Prerequisites

1. **GitHub Repository**: Your code should be in a GitHub repository
2. **Docker Hub Account**: For storing Docker images
3. **GitHub Secrets**: Required secrets for the pipeline

## 🔧 Setup Instructions

### 1. Configure GitHub Secrets

Go to your GitHub repository → Settings → Secrets and variables → Actions, and add:

```
DOCKER_USERNAME=your-dockerhub-username
DOCKER_PASSWORD=your-dockerhub-password-or-token
```

### 2. Environment Configuration

The pipeline uses GitHub Environments for deployment approval:

1. Go to Settings → Environments
2. Create two environments:
   - `development`
   - `staging`
3. Configure protection rules as needed (optional reviewers, wait timer, etc.)

### 3. Branch Strategy

- **`develop`**: Triggers deployment to development environment
- **`main`/`master`**: Triggers deployment to both development and staging environments
- **Pull Requests**: Run tests only

## 🏗️ Pipeline Jobs

### 1. Test Job
- Sets up Python environment
- Installs dependencies
- Runs tests
- Performs health checks

### 2. Build Job
- Builds Docker image
- Pushes to Docker Hub with multiple tags
- Supports multi-platform builds (amd64, arm64)

### 3. Deploy Jobs
- **Development**: Automatic deployment on push to develop/main/master
- **Staging**: Automatic deployment on push to main/master (after dev deployment)

### 4. Security Scan
- Runs Trivy vulnerability scanner
- Uploads results to GitHub Security tab

## 🐳 Docker Compose Files

### Development Environment
```bash
docker-compose -f docker-compose.dev.yml up -d
```

### Staging Environment
```bash
docker-compose -f docker-compose.stage.yml up -d
```

## 🔄 Manual Deployment

You can manually trigger deployments using the "Deploy to Development" workflow:

1. Go to Actions tab in your repository
2. Select "Deploy to Development" workflow
3. Click "Run workflow"
4. Choose the image tag and environment
5. Run the workflow

## 📊 Monitoring

### Health Checks
The pipeline includes health checks to ensure your application is running correctly:
- Container health checks in Docker Compose
- HTTP endpoint checks in the deployment workflow

### Logs
View application logs:
```bash
# Development
docker-compose -f docker-compose.dev.yml logs -f

# Staging
docker-compose -f docker-compose.stage.yml logs -f
```

## 🛠️ Customization

### Adding Tests
Add your test files to the `tests/` directory. The pipeline will automatically run them.

### Deployment Targets
Modify the deployment steps in `.github/workflows/ci-cd.yml` to match your infrastructure:

- **Cloud Platforms**: AWS ECS, Azure Container Instances, Google Cloud Run
- **Kubernetes**: Update kubectl commands
- **Docker Swarm**: Use docker stack deploy
- **Traditional Servers**: SSH and deploy scripts

### Environment Variables
Add environment-specific variables in the Docker Compose files or as GitHub secrets.

## 🔍 Troubleshooting

### Common Issues

1. **Docker Hub Authentication Failed**
   - Verify DOCKER_USERNAME and DOCKER_PASSWORD secrets
   - Use Docker Hub access token instead of password

2. **Health Check Failed**
   - Check application logs
   - Verify the application starts correctly
   - Ensure the health check endpoint is accessible

3. **Deployment Failed**
   - Check deployment logs in GitHub Actions
   - Verify Docker image exists and is accessible
   - Check resource availability on target environment

### Debug Commands

```bash
# Check running containers
docker ps

# View container logs
docker logs sample-app-dev
docker logs sample-app-staging

# Check application health
curl http://localhost:8000/
curl http://localhost:8000/menu
```

## 📈 Next Steps

1. **Add more tests**: Improve test coverage
2. **Database migration**: Add proper database setup for production
3. **Monitoring**: Add application monitoring (Prometheus, New Relic, etc.)
4. **Load balancing**: Add load balancer for production
5. **SSL/TLS**: Configure HTTPS for production environments

## 🤝 Contributing

When contributing to this project:
1. Create a feature branch from `develop`
2. Make your changes
3. Create a pull request to `develop`
4. After review and merge, changes will be automatically deployed to development
5. Create a pull request from `develop` to `main` for staging deployment
