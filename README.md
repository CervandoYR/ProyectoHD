Sistema de Gestión de Recursos Educativos
Sistema web desarrollado con Django para la gestión de recursos educativos, cursos, inscripciones y estudiantes, con un sistema de autenticación basado en roles (Administrador, Profesor, Estudiante) para el Colegio "Naciones Unidas".

Características principales
Autenticación y roles: Soporte para usuarios con roles de Administrador, Profesor y Estudiante, con permisos diferenciados.
Gestión de recursos: Subida, edición, eliminación y vista previa de recursos educativos (PDFs, imágenes, videos) asociados a cursos.
Gestión de estudiantes: Visualización, creación, edición y eliminación de estudiantes (basado en el modelo Usuario con rol 'Estudiante').
Gestión de cursos e inscripciones: Creación de cursos y asignación de estudiantes a los mismos.
Interfaz responsiva: Usa Bootstrap y DataTables para una experiencia de usuario moderna y adaptable.
Chatbot integrado: Implementación de un chatbot con LandBot para responder preguntas frecuentes.
Despliegue en Azure: Configurado para funcionar en Azure App Service con PostgreSQL.
Tecnologías utilizadas
Backend: Django 5.0, Python 3.12
Base de datos: PostgreSQL (producción), SQLite (desarrollo local)
Frontend: Bootstrap 5, DataTables, JavaScript, HTML/CSS
Despliegue: Azure App Service, Azure Database for PostgreSQL
Herramientas de gestión: GitHub, ClickUp, Slack, Zoom, Notion, Figma, Trello, Canva, LandBot
Dependencias: psycopg2-binary, python-dotenv
