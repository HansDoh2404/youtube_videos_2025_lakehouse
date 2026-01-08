from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df_csv = spark.read.csv(
    "/home/data/youtube_video.csv",
    header=True,
    inferSchema=True
)

table_name = "youtubes.video2025"

if not spark.catalog.tableExists(table_name):
    df_csv.writeTo(table_name).create()

df_csv.write.mode("overwrite").insertInto(table_name)

spark.stop()
