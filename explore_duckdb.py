import duckdb
import pandas as pd


pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

conn = duckdb.connect(database='local.duckdb')
# result = pd.read_sql("""select table_schema, table_name, column_name from information_schema.columns where table_schema like '%input_layer%' and table_name like '%medical_claim%'""", conn)
# result = pd.read_sql("""select long_description from terminology.icd_10_cm where icd_10_cm ~ '^C[0-9]{2}'""", conn)
result = pd.read_sql("""
select    
person_id,
claim_id,             
paid_amount,
allowed_amount,
charge_amount,
coinsurance_amount,
copayment_amount,
deductible_amount,
total_cost_amount,
diagnosis_code_1,diagnosis_poa_1, diagnosis_code_2, diagnosis_code_3, diagnosis_code_4, diagnosis_code_5,diagnosis_code_6 from input_layer.medical_claim
where
  ((diagnosis_code_1 ~ '^C[0-9]{2}')
   OR (diagnosis_code_2 ~ '^C[0-9]{2}')
   OR (diagnosis_code_3 ~ '^C[0-9]{2}')
   OR (diagnosis_code_4 ~ '^C[0-9]{2}')
   OR (diagnosis_code_5 ~ '^C[0-9]{2}')
   OR (diagnosis_code_6 ~ '^C[0-9]{2}'))
  """, conn)

#result = pd.read_sql("""select  icd_10_cm, long_description from terminology.icd_10_cm where icd_10_cm ~ '^C[0-9]{2}'""", conn)

print(result.head(100))

#print(duckdb.sql("""select * from information_schema.columns"""))