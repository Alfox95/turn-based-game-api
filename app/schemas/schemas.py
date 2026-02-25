from pydantic import BaseModel, field_validator

class UsuarioCreate(BaseModel):
    username: str
    mail: str
    password: str
    nombre: str
    edad: int
    es_admin: bool = False


    @field_validator("password")
    def validar_password(cls, value):
        if len(value.encode("utf-8")) > 72:
            raise ValueError("La contraseña es demasiado larga")
        if len(value) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        return value

class UsuarioOut(BaseModel):
    id: int
    username: str
    mail: str
    nombre: str
    edad: int
    es_admin: bool

    class Config: 
        from_attributes = True

class UsuarioUpdate(BaseModel):
    nombre: str
    edad: int
    es_admin: bool
