def generate_invoices(customers, output_file='customer_labels.html'):
    html_content = '''
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>فاکتورهای مشتریان</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;700&display=swap');
            
            body {
                font-family: 'Noto Naskh Arabic', sans-serif;
                direction: rtl;
                text-align: right;
                margin: 0;
                padding: 0;
            }
            
            .page-container {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 10px;
                padding: 10mm;
                min-height: 100vh;
                box-sizing: border-box;
            }
            
            .column {
                display: flex;
                flex-direction: column;
                gap: 5px;
            }
            
            .invoice-box {
                border: 1px solid #000;
                padding: 8px;
                box-sizing: border-box;
                page-break-inside: avoid;
                break-inside: avoid;
                flex: 1;
                min-height: 0;
            }
            
            .invoice-header {
                font-size: 14px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 8px;
            }
            
            .invoice-field {
                font-size: 11px;
                margin-bottom: 4px;
                line-height: 1.4;
            }
            
            @media print {
                .page-container {
                    page-break-after: always;
                    padding: 5mm;
                }
                
                .page-container:last-child {
                    page-break-after: auto;
                }
                
                .column {
                    page-break-inside: avoid;
                }
                
                .invoice-box {
                    break-inside: avoid;
                    page-break-inside: avoid;
                }
            }
        </style>
    </head>
    <body>
    '''
    
    invoices_per_page = 8
    invoices_per_column = 4
    
    for page_idx in range(0, len(customers), invoices_per_page):
        html_content += '<div class="page-container">'
        
        for col_idx in range(2):
            html_content += '<div class="column">'
            
            for box_idx in range(invoices_per_column):
                customer_idx = page_idx + (col_idx * invoices_per_column) + box_idx
                
                if customer_idx < len(customers):
                    name, phone, address, postal = customers[customer_idx]
                    html_content += f'''
                    <div class="invoice-box">
                        <div class="invoice-header">فاکتور مشتری</div>
                        <div class="invoice-field"><strong>نام و نام خانوادگی:</strong> {name}</div>
                        <div class="invoice-field"><strong>شماره تماس:</strong> {phone}</div>
                        <div class="invoice-field"><strong>آدرس محل سکونت:</strong> {address}</div>
                        <div class="invoice-field"><strong>کد پستی:</strong> {postal}</div>
                    </div>
                    '''
            
            html_content += '</div>'  
        
        html_content += '</div>' 
    
    html_content += '''
    </body>
    </html>
    '''
    try:
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
        print(f"HTML generated: {output_file} with {len(customers)} invoices")
    except Exception as e:
        print(f"Error writing HTML: {e}")

customers = read_customers_from_csv('database.csv')
if customers:
    generate_invoices(customers)
else:
    print("No customers found in database.csv")
