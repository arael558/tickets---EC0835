
# Requerimientos solicitados por la empresa

### 1. **Registro de usuarios** mediante formulario de escritorio (Tkinter).
  - Crear un formulario para registrar **Usuarios** con campos como **Nombre** y **Email**.
  - Validar que **el email sea único** antes de insertar.

### 2. **Registro de incidencias (tickets)** mediante formulario de escritorio.
  - Crear un formulario para registrar **Incidencias** con campos como **Título**, **Descripción**, **Prioridad** y **Usuario asignado**.
  - Validar los campos antes de guardar.

### 3. **Consultar todas las incidencias registradas.**
  - Mostrar todas las incidencias en una lista o tabla, con botones para editar o eliminar.

### 4. **Consultar incidencias por prioridad** (Baja, Media, Alta).
  - Filtrar incidencias por su nivel de **prioridad**.
  - Mostrar un listado de las incidencias filtradas.

### 5. **Consultar incidencias por usuario asignado.**
  - Filtrar incidencias por **usuario asignado**.
  - Mostrar las incidencias correspondientes a un usuario específico.

### 6. **Edición y actualización de incidencias.**
  - Permitir la **edición** de **título**, **descripción** y **prioridad** de las incidencias registradas.

### 7. **Eliminación de incidencias con confirmación.**
  - Añadir funcionalidad para eliminar incidencias, con una ventana de **confirmación** para evitar borrados accidentales.

### 8. **Gestión de usuarios**: alta, edición y eliminación con **integridad referencial**.
  - **Alta**: Crear nuevos usuarios con validación de email único.
  - **Edición**: Modificar los detalles del usuario.
  - **Eliminación**: No permitir eliminar usuarios que tengan incidencias asociadas (ver integridad referencial).

### 9. **Filtrado combinado por usuario y prioridad en el listado.**
  - Ofrecer filtros para combinar **usuario** y **prioridad** a la hora de ver las incidencias.

### 10. **Reportes / Resumen de consultas:**
  a. **Conteo de incidencias por usuario** (`GROUP BY`).
     - Generar un reporte con el **conteo de incidencias** por cada usuario.
  
  b. **Conteo de incidencias por prioridad** (`GROUP BY`).
     - Generar un reporte con el **conteo de incidencias** por cada prioridad (**Baja**, **Media**, **Alta**).
  
  c. **Listado combinado de incidencias con nombre de usuario** (`JOIN`).
     - Mostrar un **listado combinado** de incidencias junto con el **nombre de usuario** asignado.

### 11. **Consultas combinadas**: unión de tablas (`JOIN` Incidencia–Usuario) y **filtros simultáneos**.
  - Consultas para obtener incidencias asociadas a un usuario con **filtros de prioridad** aplicados al mismo tiempo.

### 12. **Respaldo de base de datos**: copia del archivo `app.db` a dispositivo externo (USB).
  - Implementar una opción en la interfaz para **respaldar** la base de datos **`app.db`** a un **dispositivo externo (USB)** u otra ubicación de almacenamiento.
  - Generar un archivo de respaldo con fecha y hora para su recuperación.
