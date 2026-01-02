# Sales Forecasting System

A complete production-ready sales forecasting system combining machine learning, generative AI, and modern DevOps practices.

## 🎯 Overview

This project demonstrates an integrated data science and engineering stack:
- **Database**: SQLite for persistent storage
- **Analysis**: Jupyter Notebook for interactive exploration
- **ML**: Linear Regression for trend prediction
- **AI**: OpenAI GPT-4 for intelligent forecasting
- **Visualization**: Plotly for interactive dashboards
- **API**: FastAPI for programmatic access
- **Deployment**: Docker & Kubernetes for scalability
- **CI/CD**: Jenkins for automated pipeline

## 📁 Project Structure

```
.
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── explanation.tex              # LaTeX documentation
├── Dockerfile                   # Container image definition
├── Jenkinsfile                  # CI/CD pipeline configuration
├── deployment.yaml              # Kubernetes deployment config
├── service.yaml                 # Kubernetes service config
├── sales.ipynb                  # Main Jupyter notebook (10 cells)
├── sales.db                     # SQLite database
├── sales.csv                    # Exported sales data
├── sales.sql                    # Database schema
├── sales.xlsx                   # Excel version of data
├── api.py                       # FastAPI application
├── sales_api.py                 # Standalone API server
├── app.py                       # Main application
├── newplot.png                  # Actual sales chart
├── newplot-predicted.png        # Predicted sales chart
└── dashboard.pbix              # Power BI dashboard
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Docker (optional, for containerization)
- Kubernetes kubectl (optional, for orchestration)
- OpenAI API key (optional, for AI predictions)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sales-forecasting.git
   cd sales-forecasting
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create database**
   ```bash
   sqlite3 sales.db < sales.sql
   ```

5. **Set OpenAI API key** (optional)
   ```bash
   # Windows (PowerShell)
   $env:OPENAI_API_KEY = "your-key-here"
   
   # Linux/Mac
   export OPENAI_API_KEY="your-key-here"
   ```

### Running the Jupyter Notebook

```bash
jupyter notebook sales.ipynb
```

The notebook contains 10 cells:
1. **Cell 1**: Load data from database
2. **Cells 2-3**: Install libraries
3. **Cell 4**: Call OpenAI API
4. **Cell 5**: Parse AI predictions
5. **Cell 6**: Display actual sales
6. **Cell 7**: Display forecasts
7. **Cell 8**: Define FastAPI endpoints
8. **Cell 9**: Test API
9. **Cell 10**: Start server

### Running the API Server

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

Access API documentation at: `http://localhost:8000/docs`

## 📊 Database Schema

### Sales Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| product | TEXT | Product name |
| region | TEXT | Geographic region |
| date | DATE | Transaction date |
| units_sold | INTEGER | Units sold |
| revenue | REAL | Total revenue |

## 🤖 Key Components

### Machine Learning
- **Algorithm**: LinearRegression
- **Framework**: scikit-learn
- **Input**: Historical sales data
- **Output**: 7-day forecast

### Generative AI
- **Provider**: OpenAI
- **Model**: gpt-4o-mini
- **Purpose**: Intelligent predictions
- **Cost**: ~$0.15 per 1M tokens

### Visualization
- **Framework**: Plotly
- **Charts**: Line plots with markers
- **Features**: Interactive, hover data, zoom/pan

### REST API
- **Framework**: FastAPI
- **Endpoints**:
  - `GET /sales` - All sales records
  - `GET /predict?region=North` - Forecast for region
  - `GET /docs` - Interactive documentation

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t sales-app:latest .
```

### Run Container
```bash
docker run -d -p 8000:8000 \
  -e OPENAI_API_KEY="your-key" \
  --name sales-app \
  sales-app:latest
```

### View Logs
```bash
docker logs -f sales-app
```

## ☸️ Kubernetes Deployment

### Prerequisites
- Kubernetes cluster running
- kubectl configured
- Docker image pushed to registry

### Deploy
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Check Status
```bash
kubectl get pods
kubectl get services
kubectl logs -f deployment/sales-app
```

### Scale
```bash
kubectl scale deployment sales-app --replicas=5
```

## 🔄 CI/CD Pipeline (Jenkins)

### Pipeline Stages
1. **Checkout** - Pull code from GitHub
2. **Build** - Create Docker image
3. **Test** - Run unit tests
4. **Deploy** - Update Kubernetes deployment

### Triggering
- Webhook on GitHub push
- Scheduled builds
- Manual trigger via Jenkins UI

## 📈 Results

### Predictions
- ML Model: LinearRegression forecast
- AI Model: OpenAI ChatGPT predictions
- Accuracy: Improves with more historical data

### Charts
- `newplot.png` - Actual sales trends
- `newplot-predicted.png` - 7-day forecast

## 🔑 Configuration

### Environment Variables
```
OPENAI_API_KEY     # OpenAI API key
DATABASE_PATH      # Path to sales.db
API_PORT          # FastAPI port (default: 8000)
```

### requirements.txt
```
pandas              # Data manipulation
plotly              # Visualization
scikit-learn        # Machine learning
openai              # AI integration
fastapi             # Web framework
uvicorn             # ASGI server
jupyter             # Notebook environment
```

## 🧪 Testing

```bash
# Test database connection
sqlite3 sales.db "SELECT COUNT(*) FROM sales;"

# Test API
curl http://localhost:8000/sales
curl http://localhost:8000/predict?region=North

# Run Jupyter notebook
jupyter notebook sales.ipynb
```

## 📚 Documentation

- `explanation.tex` - Detailed technical documentation (LaTeX)
- `explanation.pdf` - PDF version of documentation
- `Jenkinsfile` - CI/CD pipeline configuration
- Code comments throughout

## 🐛 Troubleshooting

### Issue: Database not found
```bash
# Solution: Create database
sqlite3 sales.db < sales.sql
```

### Issue: API key invalid
```bash
# Solution: Get key from https://platform.openai.com/api-keys
export OPENAI_API_KEY="sk-proj-..."
```

### Issue: Port already in use
```bash
# Solution: Use different port
uvicorn api:app --port 8001
```

### Issue: Docker build fails
```bash
# Solution: Clear Docker cache
docker build --no-cache -t sales-app:latest .
```

## 📦 Deployment Options

### Local Development
```bash
jupyter notebook sales.ipynb
```

### Standalone Server
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

### Docker Container
```bash
docker run -d -p 8000:8000 sales-app:latest
```

### Kubernetes Cluster
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Cloud Platforms
- AWS ECS/EKS
- Google Cloud Run/GKE
- Azure Container Instances/AKS
- Digital Ocean App Platform

## 🔐 Security Best Practices

1. **API Key Management**
   - Never commit API keys
   - Use environment variables
   - Rotate keys regularly

2. **Database Security**
   - Use strong credentials
   - Enable encryption
   - Restrict access

3. **API Security**
   - Enable HTTPS/TLS
   - Implement rate limiting
   - Add authentication

4. **Container Security**
   - Use minimal base images
   - Scan for vulnerabilities
   - Run as non-root user

## 📊 Performance Metrics

- ML Model Training: < 1 second
- AI Prediction API: 1-2 seconds (includes OpenAI latency)
- API Response Time: < 500ms
- Database Query: < 100ms

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👤 Author

DevOps, MLOps, GenAI Project Team

## 📞 Support

- GitHub Issues: Report bugs and request features
- Email: your-email@example.com
- Documentation: See explanation.tex

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Scikit-learn Guide](https://scikit-learn.org/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Kubernetes Docs](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)

## 📅 Changelog

### Version 1.0.0 (January 2026)
- Initial release
- ML and AI integration
- Kubernetes deployment
- Jenkins CI/CD pipeline
- Complete documentation

---

**Last Updated**: January 2, 2026

**Status**: Production Ready ✅
