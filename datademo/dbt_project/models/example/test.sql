-- Use the `ref` function to select from other models

select *
from {{ source('data_source', 'core_user') }}
