from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sql("CREATE NAMESPACE IF NOT EXISTS youtubes")

