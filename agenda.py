import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Mostrar un ejemplo del archivo Excel requerido


def mostrar_ejemplo_excel():
    ejemplo_data = {
        "Tarea": ["Tarea 1", "Tarea 2", "Tarea 3"],
        "Tiempo Estimado (Horas)": [5, 3, 8],
        "Deadline": [
            (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
            (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"),
            (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        ],
        "Progreso (%)": [20, 50, 0]
    }
    ejemplo_df = pd.DataFrame(ejemplo_data)
    st.write("### Ejemplo de archivo Excel:")
    st.markdown(ejemplo_df.style.hide(
        axis="index").to_html(), unsafe_allow_html=True)
    st.write("Este archivo debe contener las siguientes columnas:")
    st.write("- **Tarea**: Nombre de la tarea.")
    st.write(
        "- **Tiempo Estimado (Horas)**: Tiempo total estimado en horas para completar la tarea.")
    st.write("- **Deadline**: Fecha límite de la tarea en formato `YYYY-MM-DD`.")
    st.write("- **Progreso (%)**: Porcentaje de avance en la tarea (0-100%).")

# Función para cargar datos desde el archivo Excel y verificar columnas


def cargar_datos(file):
    df = pd.read_excel(file)
    df.columns = df.columns.str.strip().str.title()  # Normalizar nombres de columnas
    columnas_necesarias = {
        "Tarea", "Tiempo Estimado (Horas)", "Deadline", "Progreso (%)"}
    if not columnas_necesarias.issubset(df.columns):
        st.error(
            "El archivo Excel debe contener las columnas: Tarea, Tiempo Estimado (Horas), Deadline, Progreso (%)")
    # Formatear la columna 'Deadline' para mostrar solo la fecha
    df['Deadline'] = pd.to_datetime(df['Deadline']).dt.date
    return df

# Función para calcular prioridades y formatear tiempo restante en horas y minutos


def calcular_prioridades(df):
    df['Deadline'] = pd.to_datetime(df['Deadline'])
    today = pd.to_datetime(datetime.now().date())

    # Calcula el tiempo restante y los días restantes para cada tarea
    df['Tiempo Restante (Horas)'] = df['Tiempo Estimado (Horas)'] * \
        (1 - df['Progreso (%)'] / 100)
    df['Días Restantes'] = (df['Deadline'] - today).dt.days

    # Convertir tiempo restante a formato de horas y minutos
    df['Tiempo Restante'] = df['Tiempo Restante (Horas)'].apply(
        lambda x: f"{int(x)}h {int((x - int(x)) * 60)}m" if pd.notnull(x) else "0h 0m"
    )

    # Crear una columna de urgencia personalizada
    condiciones = [
        (df['Días Restantes'] <= 0),
        (df['Días Restantes'] > 0) & (df['Días Restantes'] <= 3),
        (df['Días Restantes'] > 3)
    ]
    valores_urgencia = [
        "Súper prioritario",
        "Prioriza en cuanto puedas",
        "Organiza con tiempo esta tarea y hazla sin estrés"
    ]
    df['Urgencia'] = np.select(condiciones, valores_urgencia)

    # Ordena las tareas de mayor urgencia en términos de días restantes
    df = df.sort_values(by='Días Restantes',
                        ascending=True).reset_index(drop=True)
    return df

# Función para crear un calendario semanal ideal con formato de tabla


def planificacion_semanal(df_prioridades):
    dia_actual = datetime.now().weekday()  # 0=Lunes, ..., 6=Domingo
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    dias_restantes = dias_semana[dia_actual:]
    fecha_base = datetime.now()

    plan_semanal = []
    dia_idx = 0
    for _, tarea in df_prioridades.iterrows():
        if dia_idx >= len(dias_restantes):
            break  # Si alcanzamos el final de la semana, terminamos de planificar

        dia_nombre = dias_restantes[dia_idx]
        dia_fecha = (fecha_base + timedelta(days=dia_idx)).strftime("%Y-%m-%d")

        horas = int(tarea['Tiempo Restante (Horas)'])
        minutos = int((tarea['Tiempo Restante (Horas)'] - horas) * 60)
        tiempo_formateado = f"{horas}h {minutos}m"

        plan_semanal.append({
            "Día": f"{dia_nombre} ({dia_fecha})",
            "Tarea": tarea['Tarea'],
            "Tiempo sugerido": tiempo_formateado
        })

        if tarea['Días Restantes'] > 0 or tarea['Urgencia'] != "Súper prioritario":
            dia_idx += 1

    plan_df = pd.DataFrame(plan_semanal)
    return plan_df


# Interfaz de la aplicación
st.title('Agenda Inteligente para la Organización Semanal')

# Mostrar el día actual
hoy = datetime.now().strftime("%A, %d %B %Y")
st.write(f"### Hoy es: {hoy}")

# Mostrar un ejemplo de archivo Excel
mostrar_ejemplo_excel()

# Cargar el archivo Excel
uploaded_file = st.file_uploader(
    "Cargar archivo Excel con las tareas", type=["xlsx"])

if uploaded_file:
    # Cargar los datos del archivo y mostrar resumen sin índice
    df = cargar_datos(uploaded_file)
    st.write('### Resumen de Tareas Cargadas:')
    st.markdown(df[['Tarea', 'Tiempo Estimado (Horas)', 'Deadline', 'Progreso (%)']].style.hide(
        axis="index").to_html(), unsafe_allow_html=True)

    # Actualizar el progreso de una tarea
    st.subheader('Actualizar progreso diario')
    tarea_seleccionada = st.selectbox(
        'Selecciona una tarea para actualizar:', df['Tarea'])
    nuevo_progreso = st.slider(
        'Progreso (%)', min_value=0, max_value=100, step=5)

    if st.button('Actualizar progreso'):
        df.loc[df['Tarea'] == tarea_seleccionada,
               'Progreso (%)'] = nuevo_progreso
        st.success(
            f'Progreso de "{tarea_seleccionada}" actualizado a {nuevo_progreso}%.')
        st.write('### Tareas actualizadas:')
        st.markdown(df[['Tarea', 'Tiempo Estimado (Horas)', 'Deadline', 'Progreso (%)']].style.hide(
            axis="index").to_html(), unsafe_allow_html=True)

    # Calcular y mostrar las recomendaciones de prioridad con categorías personalizadas
    st.subheader('Recomendaciones de prioridades')
    df_prioridades = calcular_prioridades(df)
    st.write('Tareas recomendadas para priorizar (con categorías de urgencia):')
    st.markdown(df_prioridades[['Tarea', 'Tiempo Restante', 'Días Restantes', 'Urgencia']].style.hide(
        axis="index").to_html(), unsafe_allow_html=True)

    # Planificación sugerida para el resto de la semana
    st.subheader('Planificación sugerida para la semana')
    planificacion = planificacion_semanal(df_prioridades)
    st.write("Calendario ideal para completar las tareas:")
    st.markdown(planificacion.style.hide(
        axis="index").to_html(), unsafe_allow_html=True)
else:
    st.write("Por favor, sube un archivo Excel con las tareas para ver las recomendaciones de planificación.")
