# 🐾 Centro de Adopción

Una solución web robusta desarrollada con Python (Flask) y MySQL para la gestión eficiente de mascotas y procesos de adopción. Este proyecto está diseñado para ser ligero, eficiente y optimizado para entornos GNU/Linux.

## 🚀 Sobre el Proyecto

Este sistema permite gestionar el flujo completo de adopción de mascotas, desde la visualización de un catálogo hasta el registro de adoptantes. La aplicación utiliza una arquitectura modular que separa la lógica de negocio, las rutas del servidor y la persistencia de datos, aprovechando la potencia de la terminal de Linux para el control del entorno.

## 🛠️ Tecnologías utilizadas
Framework Web: Flask (Python).

Base de Datos: MySQL (Almacenamiento relacional y persistente).

Frontend: HTML5 y CSS3 (Diseño personalizado y maquetación visual).

Entorno: GNU/Linux (Desarrollo y ejecución mediante CLI).

Editor: VS Code.

## ✨ Características Principales
Arquitectura Modular: Separación clara entre rutas (routes.py), modelos de datos (models.py) y configuración (config.py).

Gestión CRUD: Registro, consulta y eliminación de adopciones directamente en la base de datos.

Motor de Plantillas: Uso de Jinja2 para renderizar vistas dinámicas (catalogo, historial, confirmación).

Registro Transaccional: Validación de datos del adoptante antes de procesar la adopción.

Optimización Linux: Configurado para ejecutarse de forma aislada mediante entornos virtuales (venv).

## 📂 Estructura del Proyecto
Bash
CENTRO_ADOPCION/
├── static/              # Archivos estáticos
│   ├── img/             # Imágenes de las mascotas (Husky, Pastor, etc.)
│   └── style.css        # Hoja de estilos personalizada
├── templates/           # Vistas HTML (Jinja2)
│   ├── catalogo.html    # Galería de mascotas disponibles
│   ├── confirmacion.html# Formulario de adopción
│   └── historial.html   # Registro de adopciones realizadas
├── venv/                # Entorno virtual de Python
├── config.py            # Credenciales y configuración de la DB
├── database.py          # Lógica de conexión y consultas SQL
├── main.py              # Punto de entrada de la aplicación
├── models.py            # Definición de la clase Dog y objetos
├── routes.py            # Controladores y lógica de navegación
└── setup_db.py          # Script de inicialización de la base de datos


## 📦 Configuración e Instalación
Requisitos previos
Sistema Operativo: GNU/Linux.

Python 3.x y MySQL Server instalados y en ejecución.

Pasos para el despliegue
Clonar el repositorio:

Bash
git clone https://github.com/tu-usuario/centro-adopcion.git
cd centro-adopcion
Configurar el entorno virtual:

Bash
python3 -m venv venv
source venv/bin/activate
Instalar dependencias:

Bash
pip install flask mysql-connector-python
Inicializar la Base de Datos:
Asegúrate de configurar tus credenciales en config.py y luego ejecuta:

Bash
python3 setup_db.py
Lanzar la aplicación:

Bash
python3 main.py
Luego, abre tu navegador en: http://127.0.0.1:5000


## 📸 Vista Previa
<img width="1920" height="1080" alt="Captura desde 2026-03-26 22-39-35" src="https://github.com/user-attachments/assets/fb15d52c-35ee-4a8b-b261-8c67d3d35d79" />
<img width="1920" height="1080" alt="Captura desde 2026-03-27 08-13-27" src="https://github.com/user-attachments/assets/21b6f0f7-b83f-470a-83cc-1681a751d80c" />
<img width="1920" height="1080" alt="Captura desde 2026-03-27 10-34-40" src="https://github.com/user-attachments/assets/1741a141-fb01-4c9c-8c66-083133bfe371" />
<img width="1920" height="1080" alt="Captura desde 2026-03-27 10-34-27" src="https://github.com/user-attachments/assets/259e33f2-df92-4e22-97ff-7c7c2d1aa246" />
<img width="1920" height="1080" alt="Captura desde 2026-03-27 11-11-09" src="https://github.com/user-attachments/assets/fb82d6b9-4787-43a3-b3e9-cb0686920fee" />
<img width="1920" height="1080" alt="Captura desde 2026-03-27 11-14-29" src="https://github.com/user-attachments/assets/adc7b28c-e560-4cff-a99c-69bdb23b5ccc" />
<img width="1920" height="1080" alt="Captura desde 2026-03-27 15-28-27" src="https://github.com/user-attachments/assets/9662a6a3-4d0e-443e-b9b3-f410f1f840ef" />
<img width="1920" height="1080" alt="Captura desde 2026-03-27 15-28-58" src="https://github.com/user-attachments/assets/a0c7d1fa-af46-4576-9fae-77d9884ab151" />



