select
  order_id,
  customer_id,
  cast(order_date as date) as order_date,
  cast(amount as numeric) as amount
from {{ ref('orders') }}
