from pydantic import BaseModel, Field

class UserRequestModel(BaseModel):
    nombre: str
    password: str
    
class UserResponseModel(UserRequestModel):
    
    nombre: str
 
class ClienteDatos(BaseModel):
    nombre: str
    direccion: str
    colonia: str
    cp: int
    estado: str
    pais: str = "México"
    
class ClienteRequestModel(BaseModel):
    id_cliente: int = Field(..., description="ID de la referencia del auto")
    nombre: str
    numero: str
    direccion: str
    colonia: str
    estado: str
    cp: int
    pais: str
    numero_pagos: int
    orden_envio: int
    
    class Config:
        orm_mode = True
        from_attributes = True 

class ClienteResponseModel(BaseModel):
    id_cliente: int 
    nombre: str
    numero: str
    direccion: str
    colonia: str
    estado: str
    cp: int
    pais: str
    numero_pagos: int
    orden_envio: int
    
    class Config:
        orm_mode = True
        from_attributes = True 
    

class AutoRequestModel(BaseModel):
    referencia: int = Field(..., description="ID de la referencia del auto")
    auto: str
    modelo: int
    version: str
    color: str
    precio: float
    transmision: str
    motor: str
    n_motor: int
    n_puertas: int
    tipo: str
    chasis: str
    fecha_aprovacion: int
    certificado: int
    
    class Config:
        orm_mode = True
        from_attributes = True 

class AutoResponseModel(BaseModel):
    referencia: int
    auto: str
    modelo: int
    version: str
    color: str
    precio: float
    transmision: str
    motor: str
    n_motor: int
    n_puertas: int
    tipo: str
    chasis: str
    fecha_aprovacion: int
    certificado: int
    
    class Config:
        orm_mode = True
        from_attributes = True

class FacturaRequestModel(BaseModel):
    id_factura: int = Field(..., description="ID de la referencia del auto")
    referencia_id: int = Field(..., description="ID de la referencia del auto")
    auto: str
    modelo: int
    version: str
    color: str
    precio: float
    transmision: str
    motor: str
    n_motor: int
    n_puertas: int
    tipo: str
    chasis: str
    fecha_aprovacion: int
    certificado: int
    id_cliente_id: int = Field(..., description="ID del cliente")
    nombre: str
    numero: str
    Direccion: str
    Colonia: str
    Estado: str
    CP: int
    Pais: str
    numero_pagos: int
    orden_envio: int
    fecha: str
    hora: str
    
    
    
    class Config:
        orm_mode = True
        from_attributes = True 

class FacturaResponseModel(BaseModel):
    id_factura: int
    referencia_id: int
    auto: str
    modelo: int
    version: str
    color: str
    precio: float
    transmision: str
    motor: str
    n_motor: int
    n_puertas: int
    tipo: str
    chasis: str
    fecha_aprovacion: int
    certificado: int
    id_cliente_id: int
    nombre: str
    numero: str
    Direccion: str
    Colonia: str
    Estado: str
    CP: int
    Pais: str
    numero_pagos: int
    orden_envio: int
    fecha: str
    hora: str
    
    class Config:
        orm_mode = True
        from_attributes = True 


