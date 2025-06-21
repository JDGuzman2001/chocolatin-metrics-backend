from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from datetime import datetime
import uvicorn
from repository import repository
from models import ChocolatinVariableHistory

# Create FastAPI app instance
app = FastAPI(
    title="Chocolatin Metrics API",
    description="API para métricas de Chocolatin",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://localhost:8080"],  # Add your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/variables", response_model=List[ChocolatinVariableHistory])
async def get_variables(
    limit: Optional[int] = Query(None, description="Número máximo de registros a retornar"),
    offset: Optional[int] = Query(None, description="Número de registros a omitir")
):
    """Obtiene todos los registros de la tabla chocolatin_variables_history"""
    try:
        variables = repository.get_all_variables(limit=limit, offset=offset)
        return variables
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener variables: {str(e)}")

@app.get("/variables/module/{module}", response_model=List[ChocolatinVariableHistory])
async def get_variables_by_module(
    module: str,
    limit: Optional[int] = Query(None, description="Número máximo de registros a retornar")
):
    """Obtiene registros filtrados por módulo"""
    try:
        variables = repository.get_variables_by_module(module=module, limit=limit)
        return variables
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener variables por módulo: {str(e)}")

@app.get("/variables/date-range", response_model=List[ChocolatinVariableHistory])
async def get_variables_by_date_range(
    start_date: datetime = Query(..., description="Fecha de inicio (YYYY-MM-DD HH:MM:SS)"),
    end_date: datetime = Query(..., description="Fecha de fin (YYYY-MM-DD HH:MM:SS)"),
    limit: Optional[int] = Query(None, description="Número máximo de registros a retornar")
):
    """Obtiene registros filtrados por rango de fechas"""
    try:
        variables = repository.get_variables_by_date_range(
            start_date=start_date, 
            end_date=end_date, 
            limit=limit
        )
        return variables
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener variables por rango de fechas: {str(e)}")

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
