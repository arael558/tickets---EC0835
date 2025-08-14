from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Text

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    email  = Column(String(180), unique=True, nullable=False)
    incidencias = relationship("Incidencia", back_populates="usuario")

class Incidencia(Base):
    __tablename__ = "incidencias"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=False)
    prioridad = Column(String(20), nullable=False)   # Baja/Media/Alta
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", back_populates="incidencias")
