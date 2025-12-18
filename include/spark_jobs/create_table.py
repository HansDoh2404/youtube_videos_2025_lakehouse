from pyspark.sql import SparkSession
from pyspark.sql.types import DateType, StringType, StructType, IntegerType, StructField

schema = StructType([
  StructField("video_id", StringType(), True),
  StructField("title", StringType(), True),
  StructField("channel_id", StringType(), True),
  StructField("channel_name", StringType(), True),
  StructField("view_count", IntegerType(), True),
  StructField("like_count", IntegerType(), True),
  StructField("comment_count", IntegerType(), True),
  StructField("published_date", DateType(), True),
  StructField("thumbnail", StringType(), True)
])

spark = SparkSession.builder.getOrCreate()
df_csv = spark.createDataFrame([], schema)