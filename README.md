# Modelador de minas 3D Minero Pro

## Prerequisitos

- Puerto 8000 disponible. Debido a que se usa fastAPI en una capa inferior.
- Python 3.11, puedes verificar tu versión ejecutando el
  comando `python --version`. Si no lo posee puedes obtenerlo desde:
  1. [Página-Oficial](https://www.python.org/downloads/release/python-3119/) Ideal para Linux y Unix
  2. [Microsoft-Store](https://apps.microsoft.com/detail/9nrwmjp3717k?hl=en-mt&gl=MT) Ideal para Windows (no requiere configuración para usar python en CLI, a diferencia de la otra opción)

## Instalación

1. crear un ambiente virtual, usando el comando:
    ```bash
    python3.11 -m venv venv # Asegurar usar 3.11
    ```

2. activar el ambiente virtual utilizando:
    ```bash
    venv\Scripts\activate # En Windows
    source venv/bin/activate # En Linux o MacOS
    ```

3. instalar las dependencias del proyecto con:
    ```
    pip install -r requirements.txt
    ```

4. levantar el servidor:
    ```
    python main.py
    ```

5. La aplicación deberá desplegar una GUI.

## Construcción de la aplicación

Para construir la aplicación, se debe ejecutar el siguiente comando:

```bash
nicegui-pack  --add-data "assets;assets" --add-data "data;data"  --name "minero-pro" --windowed main.py
```

Generará un archivo ejecutable en la carpeta `dist` con el nombre `minero-pro`. Al ejecutarlo, se desplegará la GUI de
la aplicación.
