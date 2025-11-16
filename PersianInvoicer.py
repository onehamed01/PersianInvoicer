import csv
import datetime
from typing import List, Tuple, Optional


class PersianInvoicerClass:
    """
    A modular class for generating Persian invoices from CSV data.
    Supports HTML output with customizable layouts.
    """
    
    def __init__(self, file_name: str, shop_name: str = "", eng_numbers: bool = True):
        """
        Initialize the Persian Invoicer.
        
        Args:
            file_name: Path to the CSV file containing customer data
            shop_name: Name of the shop (optional, for future use)
            eng_numbers: Whether to use English numbers (optional, for future use)
        """
        self.file_name = file_name
        self.shop_name = shop_name
        self.eng_numbers = eng_numbers
        self.customers: List[Tuple[str, str, str, str]] = []
    
    def read_csv(self) -> List[Tuple[str, str, str, str]]:
        """
        Read customer data from CSV file.
        
        Returns:
            List of tuples containing (name, phone, address, postal_code)
        """
        customers = []
        try:
            with open(self.file_name, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if any(row.values()):
                        customers.append((
                            row.get('نام و نام خانوادگی', '').strip(),
                            row.get('شماره تماس', '').strip(),
                            row.get('آدرس محل سکونت', '').strip(),
                            row.get('کد پستی', '').strip()
                        ))
        except FileNotFoundError:
            print(f"Error: {self.file_name} not found!")
            return []
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []
        
        self.customers = customers
        return customers
    
    def generate_html(self, 
                     output_file: str = 'customer_labels.html',
                     invoices_per_page: int = 8,
                     invoices_per_column: int = 4) -> bool:
        """
        Generate HTML file with invoice labels in a 2-column layout.
        
        Args:
            output_file: Name of the output HTML file
            invoices_per_page: Total number of invoices per page (default: 8)
            invoices_per_column: Number of invoices per column (default: 4)
        
        Returns:
            True if successful, False otherwise
        """
        if not self.customers:
            self.customers = self.read_csv()
        
        if not self.customers:
            print("No customers found to generate invoices")
            return False
        
        html_content = f'''
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>{self.shop_name}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@100..900&display=swap');
            
            body {{
                font-family: "Noto Sans Arabic", sans-serif;
                direction: rtl;
                text-align: right;
                margin: 0;
                padding: 0;
            }}
            
            .page-container {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 10px;
                padding: 10mm;
                min-height: 100vh;
                box-sizing: border-box;
            }}
            
            .column {{
                display: flex;
                flex-direction: column;
                gap: 5px;
            }}
            
            .invoice-box {{
                border: 1px solid #000;
                padding: 8px;
                box-sizing: border-box;
                page-break-inside: avoid;
                break-inside: avoid;
                flex: 1;
                min-height: 0;
            }}
            
            .invoice-header {{
                font-size: 14px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 8px;
            }}
            
            .invoice-field {{
                font-size: 11px;
                margin-bottom: 4px;
                line-height: 1.4;
            }}
            
            @media print {{
                .page-container {{
                    page-break-after: always;
                    padding: 5mm;
                }}
                
                .page-container:last-child {{
                    page-break-after: auto;
                }}
                
                .column {{
                    page-break-inside: avoid;
                }}
                
                .invoice-box {{
                    break-inside: avoid;
                    page-break-inside: avoid;
                }}
            }}
        </style>
    </head>
    <body>
    '''
        
        # Group customers into pages
        for page_idx in range(0, len(self.customers), invoices_per_page):
            html_content += '<div class="page-container">'
            
            # Create two columns
            for col_idx in range(2):
                html_content += '<div class="column">'
                
                # Add invoices to this column
                for box_idx in range(invoices_per_column):
                    customer_idx = page_idx + (col_idx * invoices_per_column) + box_idx
                    
                    if customer_idx < len(self.customers):
                        name, phone, address, postal = self.customers[customer_idx]
                        html_content += f'''
                    <div class="invoice-box">
                        <div class="invoice-header">{self.shop_name}</div>
                        <div class="invoice-field"><strong>نام و نام خانوادگی:</strong> {name}</div>
                        <div class="invoice-field"><strong>شماره تماس:</strong> {phone}</div>
                        <div class="invoice-field"><strong>آدرس محل سکونت:</strong> {address}</div>
                        <div class="invoice-field"><strong>کد پستی:</strong> {postal}</div>
                    </div>
                    '''
                
                html_content += '</div>'  # Close column
            
            html_content += '</div>'  # Close page-container
        
        html_content += '''
    </body>
    </html>
    '''
        
        try:
            with open(output_file, 'w', encoding='utf-8') as html_file:
                html_file.write(html_content)
            print(f"HTML generated: {output_file} with {len(self.customers)} invoices")
            return True
        except Exception as e:
            print(f"Error writing HTML: {e}")
            return False
    
    def get_customers(self) -> List[Tuple[str, str, str, str]]:
        """
        Get the list of customers.
        If not loaded yet, reads from CSV first.
        
        Returns:
            List of customer tuples
        """
        if not self.customers:
            self.read_csv()
        return self.customers
    
    def get_customer_count(self) -> int:
        """
        Get the number of customers.
        
        Returns:
            Number of customers
        """
        if not self.customers:
            self.read_csv()
        return len(self.customers)

