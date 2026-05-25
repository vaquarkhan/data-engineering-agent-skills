create or replace view analytics.customers_publish as
select
  customer_id,
  customer_name,
  country,
  updated_at
from analytics.customers_refined;
