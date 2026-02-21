from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def run_bronze_load(
    spark: SparkSession,
    raw_path: str,
    bronze_table: str,
    checkpoint_path: str,
) -> None:
    df = (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "parquet")
        .option("cloudFiles.inferColumnTypes", "true")
        .load(raw_path)
        .withColumn("_ingestion_ts", F.current_timestamp())
    )

    (
        df.writeStream.format("delta")
        .option("checkpointLocation", checkpoint_path)
        .outputMode("append")
        .trigger(once=True)
        .toTable(bronze_table)
    )
