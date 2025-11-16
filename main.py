from PersianInvoicer import PersianInvoicerClass

if __name__ == "__main__":
    invoicer = PersianInvoicerClass(file_name='database.csv', shop_name='Bella Shop')
    
    invoicer.generate_html()
