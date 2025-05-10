from pyspark.sql import SparkSession
# Initialize Spark session
spark = SparkSession.builder \
    .appName("SparkSessionTest") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()

# Print Spark version to confirm it's running
print(f"Spark version: {spark.version}")

# Create a simple DataFrame
df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

# Show the DataFrame
df.show()
 
# Stop the session
spark.stop()