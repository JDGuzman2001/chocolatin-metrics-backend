﻿# Chocolatin Metrics Backend

A FastAPI-based REST API for managing and querying Chocolatin variable history data from Google Cloud SQL.

## 🚀 Features

- **RESTful API**: Built with FastAPI for high performance and automatic API documentation
- **Google Cloud SQL Integration**: Secure connection to PostgreSQL database hosted on Google Cloud
- **Flexible Querying**: Multiple endpoints for retrieving data with filtering options
- **CORS Support**: Configured for cross-origin requests from frontend applications
- **Environment-based Configuration**: Secure credential management using environment variables

## 📋 Prerequisites

- Python 3.8+
- Google Cloud Platform account with Cloud SQL instance
- PostgreSQL database with `chocolatin_variables_history` table
- OpenAI API key (for future AI features)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JDGuzman2001/chocolatin-metrics-backend.git
   cd chocolatin-metrics-backend
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory with the following variables:
   ```env
   # Google Cloud credentials
   GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json
   PROJECT_ID=your-gcp-project-id
   
   # Google Cloud SQL configuration
   SQL_DATABASE_NAME=your-database-name
   SQL_DATABASE_USERNAME=your-database-username
   SQL_DATABASE_PASSWORD=your-database-password
   SQL_DATABASE_REGION=your-database-region
   SQL_DATABASE_INSTANCE=your-database-instance-name
   
   # OpenAI API key
   OPENAI_API_KEY=your-openai-api-key
   ```

## 🏃‍♂️ Running the Application

### Development Mode
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Production Mode
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📚 API Documentation

Once the application is running, you can access:
- **Interactive API docs**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`

## 🔌 API Endpoints

### 1. Get All Variables
```http
GET /variables
```

**Query Parameters:**
- `limit` (optional): Maximum number of records to return
- `offset` (optional): Number of records to skip

**Example:**
```bash
curl "http://localhost:8000/variables?limit=10&offset=0"
```

### 2. Get Variables by Module
```http
GET /variables/module/{module}
```

**Path Parameters:**
- `module`: Module name to filter by

**Query Parameters:**
- `limit` (optional): Maximum number of records to return

**Example:**
```bash
curl "http://localhost:8000/variables/module/production?limit=5"
```

### 3. Get Variables by Date Range
```http
GET /variables/date-range
```

**Query Parameters:**
- `start_date`: Start date in format `YYYY-MM-DD HH:MM:SS`
- `end_date`: End date in format `YYYY-MM-DD HH:MM:SS`
- `limit` (optional): Maximum number of records to return

**Example:**
```bash
curl "http://localhost:8000/variables/date-range?start_date=2024-01-01%2000:00:00&end_date=2024-01-31%2023:59:59&limit=20"
```

## 📊 Data Model

The API works with `ChocolatinVariableHistory` objects with the following structure:

```json
{
  "id": 1,
  "module": "production",
  "address": "DB1.DBW0",
  "symbol": "TEMP_SENSOR_1",
  "data_type": "REAL",
  "comment": "Temperature sensor reading",
  "value": "25.5",
  "timestamp": "2024-01-15T10:30:00",
  "created_at": "2024-01-15T10:30:00"
}
```

## 🏗️ Project Structure

```
chocolatin-metrics-backend/
├── main.py              # FastAPI application and route definitions
├── models.py            # Pydantic data models
├── database.py          # Google Cloud SQL connection management
├── repository.py        # Data access layer and business logic
├── config.py            # Configuration management
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔧 Configuration

The application uses the following configuration classes:

- **APIConfig**: Manages all environment variables and validates required credentials
- **CloudSQLConnection**: Handles Google Cloud SQL connection pooling
- **ChocolatinVariablesRepository**: Provides data access methods

## 🚨 Error Handling

The API includes comprehensive error handling:
- **500 Internal Server Error**: For database connection issues or unexpected errors
- **422 Validation Error**: For invalid request parameters (handled automatically by FastAPI)
- **404 Not Found**: For invalid endpoints (handled automatically by FastAPI)

## 🔒 Security

- Environment variables for sensitive configuration
- Google Cloud SQL secure connection
- CORS configuration for frontend integration
- Input validation using Pydantic models

## 🧪 Testing

To test the API endpoints, you can use:
- The interactive Swagger UI at `/docs`
- curl commands
- Postman or similar API testing tools

## 📝 Database Schema

The application expects a PostgreSQL table with the following structure:

```sql
CREATE TABLE chocolatin_variables_history (
    id SERIAL PRIMARY KEY,
    module VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    symbol VARCHAR(255),
    data_type VARCHAR(50),
    comment TEXT,
    value TEXT,
    timestamp TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
