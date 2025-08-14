from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from db import SessionLocal
from models import Usuario, Incidencia

# ---------- USUARIOS (CRUD) ----------
def crear_usuario(nombre: str, email: str):
    with SessionLocal() as s:
        u = Usuario(nombre=nombre.strip(), email=email.strip().lower())
        s.add(u)
        try:
            s.commit()
        except IntegrityError:
            s.rollback()
            raise ValueError("El email ya existe.")
        s.refresh(u)
        return u

def listar_usuarios():
    with SessionLocal() as s:
        return list(s.scalars(select(Usuario).order_by(Usuario.nombre)))

def obtener_usuario(usuario_id: int):
    with SessionLocal() as s:
        return s.get(Usuario, usuario_id)

def editar_usuario(usuario_id: int, nombre: str, email: str):
    with SessionLocal() as s:
        u = s.get(Usuario, usuario_id)
        if not u:
            return None
        u.nombre = nombre.strip()
        u.email  = email.strip().lower()
        try:
            s.commit()
        except IntegrityError:
            s.rollback()
            raise ValueError("El email ya existe.")
        s.refresh(u)
        return u

def eliminar_usuario(usuario_id: int):
    with SessionLocal() as s:
        u = s.get(Usuario, usuario_id)
        if not u:
            return False
        # Bloquea si tiene incidencias asociadas (opcional)
        cnt = s.scalar(select(func.count(Incidencia.id)).where(Incidencia.usuario_id == usuario_id))
        if cnt and cnt > 0:
            raise ValueError("No se puede eliminar: tiene incidencias asociadas.")
        s.delete(u); s.commit()
        return True

# ---------- INCIDENCIAS (CRUD) ----------
def crear_incidencia(titulo: str, descripcion: str, prioridad: str, usuario_id: int):
    with SessionLocal() as s:
        if not s.get(Usuario, usuario_id):
            raise ValueError("Usuario no existe.")
        inc = Incidencia(
            titulo=titulo.strip(),
            descripcion=descripcion.strip(),
            prioridad=prioridad.strip(),
            usuario_id=usuario_id
        )
        s.add(inc); s.commit(); s.refresh(inc)
        return inc

def listar_incidencias(usuario_id: int | None = None, prioridad: str | None = None):
    # SELECT (búsqueda normal)
    with SessionLocal() as s:
        stmt = select(Incidencia).options(joinedload(Incidencia.usuario)).order_by(Incidencia.id.desc())
        if usuario_id:
            stmt = stmt.where(Incidencia.usuario_id == usuario_id)
        if prioridad:
            stmt = stmt.where(Incidencia.prioridad == prioridad)
        return list(s.scalars(stmt))

def obtener_incidencia(inc_id: int):
    with SessionLocal() as s:
        return s.get(Incidencia, inc_id)

def editar_incidencia(inc_id: int, **campos):
    # UPDATE
    with SessionLocal() as s:
        inc = s.get(Incidencia, inc_id)
        if not inc:
            return None
        if "usuario_id" in campos and not s.get(Usuario, campos["usuario_id"]):
            raise ValueError("Usuario destino no existe.")
        for k, v in campos.items():
            setattr(inc, k, v)
        s.commit(); s.refresh(inc)
        return inc

def eliminar_incidencia(inc_id: int):
    # DELETE
    with SessionLocal() as s:
        inc = s.get(Incidencia, inc_id)
        if not inc:
            return False
        s.delete(inc); s.commit()
        return True

# ---------- CONSULTAS ESPECIALES ----------
def incidencias_join_con_usuario():
    # JOIN: Incidencia + Usuario.nombre
    with SessionLocal() as s:
        stmt = (
            select(Incidencia.id, Incidencia.titulo, Incidencia.prioridad, Usuario.nombre)
            .join(Usuario, Usuario.id == Incidencia.usuario_id)
            .order_by(Incidencia.id.desc())
        )
        return s.execute(stmt).all()

def conteo_incidencias_por_usuario():
    # GROUP BY: cuántas incidencias por usuario
    with SessionLocal() as s:
        stmt = (
            select(Usuario.nombre, func.count(Incidencia.id))
            .join(Incidencia, Incidencia.usuario_id == Usuario.id, isouter=True)
            .group_by(Usuario.nombre)
            .order_by(Usuario.nombre)
        )
        return s.execute(stmt).all()
