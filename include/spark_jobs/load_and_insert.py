from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df_csv = spark.read.csv(
    "/home/data/youtube_video.csv",
    header=True,
    inferSchema=True
)
df_csv.writeTo("youtubes.video2025").create()
df_csv.writeTo("youtubes.video2025").append()

spark.stop()
