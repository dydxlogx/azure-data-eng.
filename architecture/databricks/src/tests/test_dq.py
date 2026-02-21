from pyspark.sql import SparkSession
from src.dq import not_null_check


def test_not_null_check():
    spark = SparkSession.builder.master("local[1]").appName("test").getOrCreate()
    df = spark.createDataFrame([(1, "A"), (None, "B")], ["id", "name"])
    result = not_null_check(df, ["id"])
    rows = [r["_dq_not_null"] for r in result.select("_dq_not_null").collect()]
    assert rows == [True, False]
