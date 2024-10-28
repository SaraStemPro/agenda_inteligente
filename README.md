# Agenda Inteligente para la Organización Semanal

Esta es una aplicación de **Streamlit** para ayudar a organizar y priorizar tareas semanales. Permite cargar un archivo Excel con información sobre tareas, tiempo estimado, fechas límite y progreso, y genera recomendaciones de planificación semanal para optimizar la productividad.

Este ejercicio forma parte del apartado de casos de uso reales de la asignatura **“Competencias profesionales en la era digital”** impartida por Sara Díaz (SaraStem).

## Características

- **Carga de Tareas**: Sube un archivo Excel con tus tareas y obtén un resumen en pantalla.
- **Prioritización**: Calcula la prioridad de cada tarea en función de los días restantes y el progreso.
- **Planificación Semanal**: Genera un calendario semanal optimizado para completar las tareas en orden de prioridad.
- **Actualización de Progreso**: Permite actualizar el progreso diario de las tareas y ajustar la planificación en tiempo real.

## Ejemplo de Formato del Archivo Excel

Tu archivo Excel debe contener las siguientes columnas:
- **Tarea**: Nombre de la tarea (Texto)
- **Tiempo Estimado (Horas)**: Tiempo total estimado en horas para completar la tarea (Número)
- **Deadline**: Fecha límite de la tarea en formato `YYYY-MM-DD` (Fecha)
- **Progreso (%)**: Porcentaje de avance en la tarea, del 0 al 100% (Número)

A continuación, un ejemplo de archivo:

| Tarea                         | Tiempo Estimado (Horas) | Deadline   | Progreso (%) |
|-------------------------------|--------------------------|------------|--------------|
| Preparar presentación         | 5                        | 2024-10-30 | 20           |
| Revisar y responder correos   | 2                        | 2024-10-31 | 50           |
| Redactar informe mensual      | 8                        | 2024-11-01 | 0            |

## Instalación

### Requisitos

- Python 3.7 o superior
- Streamlit
- Pandas
- Numpy

### Pasos de Instalación

1. Clona el repositorio:
 ```bash
 git clone https://github.com/tu-usuario/agenda-inteligente-semanal.git
 cd agenda-inteligente-semanal
 ```
   
2. Instala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```

3. Ejecuta la aplicación:
  ```bash
  streamlit run app.py
  ```

4. Abre tu navegador y ve a http://localhost:8501 para interactuar con la aplicación.

### Uso de la Aplicación

- **Carga de Tareas**: Sube un archivo Excel con el formato especificado. La aplicación mostrará un resumen inicial de las tareas.

- **Actualizar Progreso**: Selecciona una tarea del menú desplegable y ajusta el progreso usando el control deslizante.

- **Planificación Semanal**: Visualiza la planificación sugerida para completar tus tareas antes de las fechas límite.

### Capturas de Pantalla

**PANTALLA DE INICIO:**

![Captura de pantalla 2024-10-28 a las 13 23 54 p  m](https://github.com/user-attachments/assets/7cef48f6-2877-44e9-8a78-93fae1e714e3)

**PLANIFICACIÓN SEMANAL:**

![Captura de pantalla 2024-10-28 a las 13 24 08 p  m](https://github.com/user-attachments/assets/6f8b4e0a-53a6-46ba-98a0-15b685b598ed)
![Captura de pantalla 2024-10-28 a las 13 25 12 p  m](https://github.com/user-attachments/assets/ca5b901d-6ae2-49f9-a474-dcea8f37b674)


### Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar esta aplicación, puedes hacer un fork del repositorio y enviar un pull request con tus cambios.

### Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

### Contacto

Para consultas o sugerencias, puedes contactarme en hola@sarastem.com.



