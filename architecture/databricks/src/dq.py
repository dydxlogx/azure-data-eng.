from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def not_null_check(df: DataFrame, cols: list[str]) -> DataFrame:
    condition = None
    for col_name in cols:
        col_check = F.col(col_name).isNotNull()
        condition = col_check if condition is None else (condition & col_check)
    return df.withColumn("_dq_not_null", condition)


def non_negative_check(df: DataFrame, cols: list[str]) -> DataFrame:
    condition = None
    for col_name in cols:
        col_check = F.col(col_name) >= F.lit(0)
        condition = col_check if condition is None else (condition & col_check)
    return df.withColumn("_dq_non_negative", condition)


def split_valid_invalid(df: DataFrame) -> tuple[DataFrame, DataFrame]:
    valid = df.filter(F.col("_dq_not_null") & F.col("_dq_non_negative"))
    invalid = df.filter(~(F.col("_dq_not_null") & F.col("_dq_non_negative")))
    return valid, invalid
