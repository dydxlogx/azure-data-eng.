# Databricks notebook source
from pyspark.sql import SparkSession
from src.dq import not_null_check, non_negative_check, split_valid_invalid
from src.silver_merge import run_silver_merge

spark = SparkSession.builder.getOrCreate()

source_table = dbutils.widgets.get("source_table")
target_table = dbutils.widgets.get("target_table")
quarantine_table = dbutils.widgets.get("quarantine_table")
primary_keys = dbutils.widgets.get("primary_keys").split(",")

raw_df = spark.table(source_table)
check_df = not_null_check(raw_df, primary_keys)
check_df = non_negative_check(check_df, ["amount"])

valid_df, invalid_df = split_valid_invalid(check_df)
valid_df.createOrReplaceTempView("valid_stage")

run_silver_merge(
    spark=spark,
    source_table="valid_stage",
    target_table=target_table,
    primary_keys=primary_keys,
    scd_type="SCD1",
)

invalid_df.write.mode("append").saveAsTable(quarantine_table)
