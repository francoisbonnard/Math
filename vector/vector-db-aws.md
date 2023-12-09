https://aws.amazon.com/fr/what-is/vector-databases/

https://aws.amazon.com/products/databases/

https://aws.amazon.com/rds/

https://aws.amazon.com/dynamodb/

https://aws.amazon.com/aurora/

https://aws.amazon.com/redshift/

https://aws.amazon.com/documentdb/

https://aws.amazon.com/neptune/

Aurora Serverless PostgreSQL with pgvector would be my go-to.

The recommendation is almost always "don't run databases in containers". If you have access to the cloud, consider managed services first - such as postgres on RDS with pg_vector, or opensearch.

Use Kendra if you have the budget. It literally is a "one-and-done" solution and you never have to even think about the vector part or managing a database part. It does it all for you and even manages the integration with whatever your data source is.

If you don't have a spare $1k/mo, use opensearch serverless.

