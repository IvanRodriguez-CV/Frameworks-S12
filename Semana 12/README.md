# Semana 12 - Django y MariaDB

Proyecto de práctica basado en las dos guías: proyecto `comercial`, aplicación
`catalogo`, consultas ORM y mantenimiento CRUD de categorías con plantillas
heredadas y formularios.

## Preparar el entorno

Use Python 3.12, MariaDB 10.4 y las versiones compatibles del proyecto
(Django 4.2.30). Cree el entorno virtual e instale los paquetes:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Inicie MariaDB Server en el puerto `3306` y cree la base de datos `comercial`.
La configuración del proyecto usa la base de datos `comercial`, el
usuario `root`, el host `localhost` y el puerto `3306`. Si configuró una
contraseña para `root`, escríbala en `PASSWORD` en `comercial/settings.py`.

## Migraciones y servidor

Genere las migraciones, cree las tablas y ejecute el servidor:

```powershell
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py runserver
```

Abra <http://127.0.0.1:8000/categoria/> para listar, agregar, actualizar y
eliminar categorías.

Para inspeccionar las tablas con la consola de MariaDB:

```powershell
python .\manage.py dbshell
```

En la consola SQL:

```sql
SHOW TABLES;
DESCRIBE catalogo_categoria;
```

## Probar el modelo desde Django Shell

```powershell
python .\manage.py shell
```

En la consola interactiva:

```python
from django.utils import timezone
from catalogo.models.categoria import Categoria

mi_categoria = Categoria(
    nombre="Electrónicos",
    descripcion="Productos electrónicos",
    created_at=timezone.now(),
    updated_at=timezone.now(),
)
print(mi_categoria)
mi_categoria.save()
mi_categoria.nombre = "tv"
mi_categoria.save()
mi_categoria.delete()
```

La guía también propone crear los modelos `TipoPago`, `Cliente` y `Rol`.
