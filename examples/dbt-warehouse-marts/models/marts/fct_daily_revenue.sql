select
  order_date,
  sum(amount) as daily_revenue
from {{ ref('stg_orders') }}
group by 1
