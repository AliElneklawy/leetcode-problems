select p.product_id, ROUND(SUM(p.price * us.units)/SUM(us.units), 2) as average_price
from Prices p inner join UnitsSold us
on p.product_id = us.product_id
where us.purchase_date between p.start_date and p.end_date   
group by p.product_id
