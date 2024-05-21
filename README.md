# Modelador de minas 3D Minero Pro

## Prerequisitos

- [Python 3.12](https://www.python.org/downloads/release/python-3123/), puedes verificar tu versión ejecutando el
  comando `python --version`.

## Instalación

1. crear un ambiente virtual, usando el comando:
    ```bash
        python -m venv venv
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
