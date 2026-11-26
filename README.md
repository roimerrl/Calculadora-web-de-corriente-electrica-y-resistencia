# Calculadora Web de Corriente Eléctrica y Resistencia

Proyecto Final de **Programación I** — Universidad de Margarita, Decanato de Ingeniería y Afines.

Esta es una aplicación web interactiva desarrollada en **Python y Streamlit** que estima la corriente eléctrica de un circuito sencillo de corriente continua (DC). El usuario debe de introducir la tensión de alimentación, la resistencia de la carga, el material del conductor, la longitud de ida del cable y el área de su sección transversal; el sistema valida los datos, calcula la resistencia del cable, la resistencia total, la corriente, la caída detensión y la potencia disipada, y muestra los resultados con sus unidades.

## Integrantes

- Esteban Cen
- Adrian Torres
- José Castillo
- Roimer Rodríguez
- José Hernández
- Jessena Ibrahim

## Requisitos

- Python 3.10 o superior
- Streamlit (se instala desde `requirements.txt`)

## Creación del entorno virtual e instalación

```bash
# 1. Ubicarse en la carpeta raíz del proyecto (donde está app.py)
cd Calculadora-web-de-corriente-electrica-y-resistencia

# 2. Crear el entorno virtual
python -m venv .venv

# 3. Activar el entorno
#    Windows (PowerShell):
.venv\Scripts\Activate.ps1
#    Windows (CMD):
.venv\Scripts\activate.bat
#    Linux / macOS:
source .venv/bin/activate

# 4. Instalar las dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
# Desde la carpeta raíz del proyecto y con el entorno activado:
streamlit run app.py
```

La aplicación se abre automáticamente en el navegador (por defecto en
`http://localhost:8501`).

## Funcionalidades

- **Calculadora:** valida los cinco parámetros de entrada (rechaza vacíos, texto, cero, negativos, NaN e infinito; admite coma o punto decimal y secciones como `2.5`, `2,5`, `2.5 mm2` o `2,5 mm²` mediante expresiones regulares) y muestra Rc, Rt, I, Vc y Pc con sus unidades.
- **Historial:** guarda cada cálculo exitoso en `data/historial.json` (id, fecha/hora, entradas y resultados) y permite consultarlo con filtros por fecha o material.
- **Logs técnicos:** registra los eventos del programa en `logs/app.log` con el
  formato `fecha | nivel | módulo.función | mensaje` y niveles INFO / WARNING / ERROR. La página de consulta muestra los últimos 50 eventos con sus contadores.
- **Reportes:** exporta el historial a CSV con encabezados y unidades, listo para Excel.
- **Fundamentos / Ayuda:** explica parámetros, fórmulas, ejemplo de comprobación, supuestos y limitaciones del simulador.

>Diferencia importante: el **historial** conserva qué cálculos realizó el usuario; los **logs** documentan qué eventos técnicos ocurrieron en el programa. Son archivos y finalidades distintas.

## Estructura del proyecto

```
pagina/
├── app.py                     # Punto de entrada e interfaz Streamlit
├── requirements.txt           # Dependencias
├── README.md                  # documentación
├── .gitignore                 # Ignorar archivos puntuales
├── calculadora.png            # Imagen en Bienvenida
├── logo-2.png                 # Logo de la universidad 
├── Calculadora/               # Lógica matemática y validaciones
│   ├── matematica.py          #   Modelo matemático (fórmulas)
│   ├── materiales.py          #   Los 4 materiales con sus resistividades
│   └── validaciones.py        #   Validaciones y regex de la sección transversal
├── imagenes/                  #Fotos del equipo
│   ├── Adrian.png, Esteban.png, Jessena.png, Roimer.png      
│   ├── JoseCastillo.png, JoseHernandez.png  
├── servicios/                 # Persistencia y servicios
│   ├── historial.py           #   Guardar/leer data/historial.json
│   ├── logs.py                #   Configuración de logging + generador de eventos
│   └── reportes.py            #   Exportación CSV
├── secciones/                 # Páginas de la interfaz
│   ├── bienvenida.py, menu_tabs.py, calculadora.py, historial.py,
│   ├── logs.py, reportes.py, fundamentos_ayuda.py, conocenos.py
├── utilidades/
│   ├── rutas.py               # Rutas centralizadas del proyecto
│   ├── generadores.py         # Generador (yield) del historial con filtros
│   └── decoradores.py         # Decorador propio @medir_tiempo
├── data/historial.json        # Historial persistente (se crea solo)
├── logs/app.log               # Registro técnico de eventos
└── reportes/                  # CSV exportados (se crea solo)
```

## Notas 

- La lógica matemática está separada de la interfaz: las funciones de cálculo no dependen de los controles visuales de Streamlit.
- El simulador es didáctico (circuito DC en seria ideal a 20 °C): no calcula ampacidad y no sirve para dimensionar instalaciones eléctricas reales.