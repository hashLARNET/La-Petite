# LaPetit-J.A.R.V.I.S
AI Chatbot project for LaPetite hotel chain, this is the backend for it, based on Django Framework for the use as an API REST.

## Cómo iniciar el proyecto Django con entorno virtual y ambiente de desarrollo

1. **Clona el repositorio y entra a la carpeta del backend:**

   ```bash
   git clone https://github.com/tu-usuario/LaPetit-J.A.R.V.I.S.git
   cd LaPetit-J.A.R.V.I.S/backend-django/JARVIS

2. **Crea y activa el repositorio**

    ```bash
    python -m venv venv
    venv\Scripts\activate

3. **Instala las dependencias**

    ```bash
    pip install -r requirements.txt

4. **Configura las variables de entorno**

Crea un archivo .env en la carpeta de settings y agrega tus variables necesarias (por ejemplo, DJANGO_SECRET_KEY).

5. **Aplica las migraciones**

    ```bash
    python manage.py migrate --settings=JARVIS.settings.dev_settings

6. **Inicia el servidor en modo desarrollo**

    ```bash
    python manage.py runserver --settings=JARVIS.settings.dev_settings