from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def product_category_pairs(products, categories, product_category):
    # Join products with product_category mapping
    prod_cat = products.join(product_category, on="product_id", how="left")
    
    # Join with categories to get names
    result = prod_cat.join(categories, on="category_id", how="left") \
                     .select("product_name", "category_name")
    
    return result

if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryJoin").getOrCreate()

    # Sample data
    products = spark.createDataFrame([
        (1, "Apple"),
        (2, "Banana"),
        (3, "Carrot"),
        (4, "Donut")
    ], ["product_id", "product_name"])

    categories = spark.createDataFrame([
        (10, "Fruit"),
        (20, "Vegetable")
    ], ["category_id", "category_name"])

    product_category = spark.createDataFrame([
        (1, 10),
        (2, 10),
        (3, 20)
    ], ["product_id", "category_id"])

    # Run the logic
    result = product_category_pairs(products, categories, product_category)
    result.show(truncate=False)

    # Optionally: filter and show products without categories
    print("Products without categories:")
    result.filter(col("category_name").isNull()).select("product_name").show()

    spark.stop()
