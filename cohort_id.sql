create view dbt_onco.cohort_id as (

    select distinct
        patient.patient_id,
        patient.first_name,
        patient_id.last_name,

    from input_layer.patient

    left join input_layer.condtion using (person_id)
    where input_layer.condtion.source_code ~* '^(C[0-9]{2}(\.[0-9A-Z]{1,4})?|D0[0-9](\.[0-9A-Z]{1,4})?|D10-D36(\.[0-9A-Z]{1,4})?|D37-D48(\.[0-9A-Z]{1,4})?|C81-C96(\.[0-9A-Z]{1,4})?|C97(\.[0-9A-Z]{1,4})?|C7A-C7B|C7C-C7E|C7F|C7G|C7H|C7J|C7K|C7L|C7M|C7N|C7P|C7Q|C7R|C7S|C7T|C7U|C7V|C7W|C7X|C7Y|C7Z)$'
)