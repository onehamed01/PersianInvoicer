import csv

# Read CSV file and parse data
def read_customers_from_csv(filename='database.csv'):
    customers = []
    try:
        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Skip empty rows
                if any(row.values()):
                    customers.append((
                        row.get('نام و نام خانوادگی', '').strip(),
                        row.get('شماره تماس', '').strip(),
                        row.get('آدرس محل سکونت', '').strip(),
                        row.get('کد پستی', '').strip()
                    ))
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
    return customers

# Function to generate HTML with 5 invoices per "page" (using CSS page breaks)
def generate_invoices(customers, output_file='customer_labels.html'):
    # HTML template with CSS for RTL, borders, and print layout
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
            
            .invoice-box {
                width: 90%;
                margin: 20px auto;
                border: 1px solid #000;
                padding: 10px;
                box-sizing: border-box;
                page-break-inside: avoid;
            }
            
            .invoice-header {
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 10px;
            }
            
            .invoice-field {
                font-size: 14px;
                margin-bottom: 5px;
            }
            
            @media print {
                .invoice-box {
                    margin: 10mm;
                }
                
                .page-break {
                    page-break-before: always;
                }
            }
            
            /* Group every 5 invoices per print page */
            .invoice-group:nth-child(5n+1) {
                page-break-before: always;
            }
        </style>
    </head>
    <body>
    '''
    
    # Process customers in groups
    for idx, (name, phone, address, postal) in enumerate(customers):
        # Add page break class every 5 invoices
        group_class = 'invoice-group' if idx % 5 == 0 else ''
        
        html_content += f'''
        <div class="invoice-box {group_class}">
            <div class="invoice-header">فاکتور مشتری</div>
            <div class="invoice-field">نام و نام خانوادگی: {name}</div>
            <div class="invoice-field">شماره تماس: {phone}</div>
            <div class="invoice-field">آدرس محل سکونت: {address}</div>
            <div class="invoice-field">کد پستی: {postal}</div>
        </div>
        '''
    
    html_content += '''
    </body>
    </html>
    '''
    
    # Write to file
    try:
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
        print(f"HTML generated: {output_file} with {len(customers)} invoices")
    except Exception as e:
        print(f"Error writing HTML: {e}")

# Read customers from CSV and generate HTML
customers = read_customers_from_csv('database.csv')
if customers:
    generate_invoices(customers)
else:
    print("No customers found in database.csv")
