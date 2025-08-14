# Tickets EC0835 (Python + Tkinter + SQLite)

Mini sistema de **Tickets** (Usuarios e Incidencias) para la evaluación **EC0835**. Incluye CRUD, consultas con **JOIN** y reportes con **GROUP BY**.

## Requisitos
- **Python** 3.10+ (Tkinter incluido en Windows)
- **pip** actualizado
- Dependencias en `requirements.txt`:
  ```txt
  sqlalchemy>=2.0
  alembic>=1.13
  ```

## Instalación rápida

### 1) Clonar
```bash
git clone <URL_DE_TU_REPO>.git
cd <carpeta_del_repo>
```

### 2) Crear y activar entorno virtual
**Windows (PowerShell):**
```powershell
python -m venv venv
.env\Scripts\Activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4) Base de datos (SQLite con Alembic)
Si el repo **ya trae** `alembic/` y `alembic.ini`:
```bash
alembic upgrade head
```

> Si es la **primera vez** y no existe `alembic/`:
> ```bash
> alembic init alembic
> # en alembic.ini: sqlalchemy.url = sqlite:///app.db
> # en alembic/env.py: from models import Base ; target_metadata = Base.metadata
> alembic revision --autogenerate -m "init"
> alembic upgrade head
> ```

### 5) Ejecutar
```bash
python main.py
```

## Estructura (referencia)
```
main.py        # UI Tkinter
models.py      # Modelos SQLAlchemy (Usuario, Incidencia)
db.py          # Engine/Session SQLite
crud.py        # Funciones CRUD + consultas
requirements.txt
alembic.ini
alembic/
  env.py
  versions/
```

##  Generar .exe (Windows)
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
# Ejecutable en dist/main.exe
```

## Problemas comunes
- **no such table: usuarios/incidencias** → ejecuta `alembic upgrade head`.
- **ModuleNotFoundError: models** en Alembic → revisa el `sys.path` en `alembic/env.py` y corre los comandos desde la raíz del proyecto.
