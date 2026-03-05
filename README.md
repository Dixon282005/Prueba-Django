# Prueba - Django

 El proyecto incluye la lógica de backend requerida y un dashboard minimalista implementado con Tailwind CSS para la visualización de los datos.

## Ejercicios Implementados

### 1. Modelado de Datos (Integridad)
- Implementación de los modelos `Project` y `Document`.
- Uso de `UniqueConstraint` para garantizar que no existan documentos con el mismo `tag` dentro de un mismo proyecto, asegurando la integridad a nivel de base de datos.

### 2. Consumo de API (GitHub)
- Integración con la API pública de GitHub usando la librería `requests`.
- Filtrado automático de repositorios originales (excluyendo forks) y manejo de excepciones para respuestas HTTP 404 o fallos de conexión.

### 3. Optimización de Consultas (N+1)
- Solución al problema de rendimiento N+1 al consultar la base de datos.
- Implementación de `select_related('project')` para reducir peticiones masivas a 1 sola consulta SQL mediante un INNER JOIN.

## Stack Tecnológico

- **Backend:** Python 3, Django, Requests
- **Base de Datos:** SQLite
- **Frontend:** HTML5, Tailwind CSS (CDN)

## Instalación y Ejecución

1. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv env
   
   # En Windows:
   .\env\Scripts\activate
   
   # En Linux/macOS:
   source env/bin/activate
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Aplicar migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Ejecutar el servidor local:**
   ```bash
   python manage.py runserver
   ```

## Rutas Principales

Una vez iniciado el servidor:

* **Dashboard Principal (Prueba):** [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)
* **Panel de Administración (Django):** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) _(Requiere ejecutar `python manage.py createsuperuser` previamente)_.

## Pruebas (Tests)

Para ejecutar las pruebas unitarias integradas al proyecto:
```bash
python manage.py test
```
