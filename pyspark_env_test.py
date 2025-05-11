from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from pyspark.sql.functions import struct

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SparkSessionTest") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()

# Print Spark version to confirm it's running
print(f"Spark version: {spark.version}")


# Define a DataFrame
data = [("Alice", 30, "Developer"), ("Bob", 25, "Analyst")]

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("role", StringType(), True)
])
df = spark.createDataFrame(data, schema)

df.show()

# Use the struct function to create a new struct column
df_with_struct = df.withColumn("person", struct(df.name, df.age, df.role))

# Show the DataFrame with the new struct column
df_with_struct.show()

 
# Stop the session
spark.stop()
