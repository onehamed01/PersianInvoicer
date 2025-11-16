from HtmlGenerator import generate_invoices
from InvoicerHTML import read_customers_from_csv

customers = read_customers_from_csv('database.csv')
if customers:
    generate_invoices(customers)
else:
    print("No customers found in database.csv")