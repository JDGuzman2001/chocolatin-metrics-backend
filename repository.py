from database import sql_connection
from models import ChocolatinVariableHistory
from typing import List, Optional
from datetime import datetime

class ChocolatinVariablesRepository:
    
    def get_all_variables(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[ChocolatinVariableHistory]:
        """Obtiene todos los registros de la tabla chocolatin_variables_history"""
        try:
            cursor = sql_connection.connection.cursor()
            
            query = "SELECT id, module, address, symbol, data_type, comment, value, timestamp, created_at FROM chocolatin_variables_history ORDER BY timestamp DESC"
            
            if limit:
                query += f" LIMIT {limit}"
            if offset:
                query += f" OFFSET {offset}"
            
            cursor.execute(query)
            rows = cursor.fetchall()
            
            variables = []
            for row in rows:
                variable = ChocolatinVariableHistory(
                    id=row[0],
                    module=row[1],
                    address=row[2],
                    symbol=row[3],
                    data_type=row[4],
                    comment=row[5],
                    value=row[6],
                    timestamp=row[7],
                    created_at=row[8]
                )
                variables.append(variable)
            
            cursor.close()
            return variables
            
        except Exception as e:
            print(f"Error getting variables: {e}")
            raise
    
    def get_variables_by_module(self, module: str, limit: Optional[int] = None) -> List[ChocolatinVariableHistory]:
        """Obtiene registros filtrados por módulo"""
        try:
            cursor = sql_connection.connection.cursor()
            
            query = "SELECT id, module, address, symbol, data_type, comment, value, timestamp, created_at FROM chocolatin_variables_history WHERE module = %s ORDER BY timestamp DESC"
            
            if limit:
                query += f" LIMIT {limit}"
            
            cursor.execute(query, (module,))
            rows = cursor.fetchall()
            
            variables = []
            for row in rows:
                variable = ChocolatinVariableHistory(
                    id=row[0],
                    module=row[1],
                    address=row[2],
                    symbol=row[3],
                    data_type=row[4],
                    comment=row[5],
                    value=row[6],
                    timestamp=row[7],
                    created_at=row[8]
                )
                variables.append(variable)
            
            cursor.close()
            return variables
            
        except Exception as e:
            print(f"Error getting variables by module: {e}")
            raise
    
    def get_variables_by_date_range(self, start_date: datetime, end_date: datetime, limit: Optional[int] = None) -> List[ChocolatinVariableHistory]:
        """Obtiene registros filtrados por rango de fechas"""
        try:
            cursor = sql_connection.connection.cursor()
            
            query = "SELECT id, module, address, symbol, data_type, comment, value, timestamp, created_at FROM chocolatin_variables_history WHERE timestamp BETWEEN %s AND %s ORDER BY timestamp DESC"
            
            if limit:
                query += f" LIMIT {limit}"
            
            cursor.execute(query, (start_date, end_date))
            rows = cursor.fetchall()
            
            variables = []
            for row in rows:
                variable = ChocolatinVariableHistory(
                    id=row[0],
                    module=row[1],
                    address=row[2],
                    symbol=row[3],
                    data_type=row[4],
                    comment=row[5],
                    value=row[6],
                    timestamp=row[7],
                    created_at=row[8]
                )
                variables.append(variable)
            
            cursor.close()
            return variables
            
        except Exception as e:
            print(f"Error getting variables by date range: {e}")
            raise

# Crear instancia global del repositorio
repository = ChocolatinVariablesRepository() 