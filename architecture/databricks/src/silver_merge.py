from pyspark.sql import SparkSession


def run_silver_merge(
    spark: SparkSession,
    source_table: str,
    target_table: str,
    primary_keys: list[str],
    scd_type: str = "SCD1",
) -> None:
    pk_join = " AND ".join([f"t.{pk}=s.{pk}" for pk in primary_keys])

    if scd_type == "SCD1":
        spark.sql(
            f"""
            MERGE INTO {target_table} t
            USING {source_table} s
            ON {pk_join}
            WHEN MATCHED THEN UPDATE SET *
            WHEN NOT MATCHED THEN INSERT *
            """
        )
    elif scd_type == "SCD2":
        spark.sql(
            f"""
            MERGE INTO {target_table} t
            USING {source_table} s
            ON {pk_join} AND t.is_current = true
            WHEN MATCHED AND t.hashdiff <> s.hashdiff THEN
              UPDATE SET t.valid_to = current_timestamp(), t.is_current = false
            WHEN NOT MATCHED THEN
              INSERT *
            """
        )
    else:
        raise ValueError(f"Unsupported SCD type: {scd_type}")
