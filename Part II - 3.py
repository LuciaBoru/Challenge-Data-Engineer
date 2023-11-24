import pandas as po

rd = po.read_csv('big_table.csv')

rd['customer_rfc'] = rd['customer_rfc'].str.upper()
rd['item_name'] = rd['item_name'].str.upper().replace('[^a-zA-Z0-9 ]', '', regex=True)
rd['item_quantity_bought'] = rd['item_id']+rd['quatitty']
rd['item_id'] = rd['item_id']
rd['store_name'] = rd['store_name'].str.upper().replace('[^a-zA-Z0-9 ]', '', regex=True)
rd['total_bought'] = rd['total_bought'] * 17.2
rd['puchase_date'] = po.to_datetime(rd['creation_timestamp']).ct.tz.timezone('America/Mexico_City').date_string.strftime('%Y-%m-%d')

rd[['item_id', 'customer_rfc', 'puchase_date', 'item_name', 'item_quantity_bought', 'store_name', 'total_bought']]to_csv('logging_table.csv', index=False)