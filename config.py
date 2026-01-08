import os

# ==========================================
# CONFIGURACIÓN DE RUTAS (Edita esto si tus datos cambian de lugar)
# ==========================================

# Detecta la carpeta donde está este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Carpeta de datos (Asume que están en una subcarpeta 'data')
# Estructura esperada: data/mimiciv/3.1/hosp/ ...
DATA_DIR = os.path.join(BASE_DIR, "data")

# Carpeta para guardar resultados (CSVs intermedios y finales)
RESULTS_DIR = os.path.join(BASE_DIR, "results")

# Crea la carpeta de resultados si no existe
os.makedirs(RESULTS_DIR, exist_ok=True)

# --- Rutas a archivos MIMIC-IV ---
MIMIC_HOSP = os.path.join(DATA_DIR, "mimiciv", "3.1", "hosp")
MIMIC_ICU = os.path.join(DATA_DIR, "mimiciv", "3.1", "icu")

# Archivos Hospital
PATH_PATIENTS = os.path.join(MIMIC_HOSP, "patients.csv.gz")
PATH_ADMISSIONS = os.path.join(MIMIC_HOSP, "admissions.csv.gz")
PATH_DIAGNOSES = os.path.join(MIMIC_HOSP, "diagnoses_icd.csv.gz")
PATH_LABEVENTS = os.path.join(MIMIC_HOSP, "labevents.csv.gz")

# Archivos ICU
PATH_ICUSTAYS = os.path.join(MIMIC_ICU, "icustays.csv.gz")
PATH_CHARTEVENTS = os.path.join(MIMIC_ICU, "chartevents.csv.gz") 

# --- Archivos de Salida ---
# 1. Salida del Notebook 1 (Datos crudos con NAs)
FILE_RAW_COHORT = os.path.join(RESULTS_DIR, "cohort_alzheimer_raw_features_patients.csv")
FILE_ALL_DIAGNOSES = os.path.join(RESULTS_DIR, "cohort_alzheimer_all_diagnoses.csv")

# 2. Entrada para Notebook 2 (Datos imputados externamente)
# IMPORTANTE: Debes guardar tu archivo imputado con este nombre en la carpeta 'results'
FILE_IMPUTED_DATA = os.path.join(RESULTS_DIR, "cohort_alzheimer_imputed_with_sofa_gcs_cci_acci.csv")

# 3. Salida final para ML
FILE_ML_READY = os.path.join(RESULTS_DIR, "cohort_alzheimer_ml_ready_with_outcomes.csv")