select query_name, 
       ROUND(SUM(rating / position) / COUNT(*), 2) as quality,
       ROUND((SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*)) * 100, 2) 
                                                            as poor_query_percentage
from Queries
group by query_name
