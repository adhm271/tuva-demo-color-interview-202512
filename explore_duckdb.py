import duckdb

print(duckdb.sql("""select * from information_schema.schemata"""))

print(duckdb.sql("""select * from information_schema.columns"""))