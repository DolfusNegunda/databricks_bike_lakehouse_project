# Databricks notebook source
# MAGIC %md
# MAGIC # Import libraries

# COMMAND ----------

# DBTITLE 1,Cell 1
from raw_ingestion_config import INGESTION_CONFIG

# COMMAND ----------

# MAGIC %md
# MAGIC #Ingest 

# COMMAND ----------

for table in INGESTION_CONFIG:
    print(f'Ingesting {table['source']} table into bike_lakehouse.bronze.{table['table']}')

    df = (
        spark.read
            .option('header', 'true')
            .option('inferSchema', 'true')
            .csv(table['path'])
    )

    (
        df.write
            .format('delta')
            .mode('overwrite')
            .saveAsTable(f'bike_lakehouse.bronze.{table['table']}')
    )
