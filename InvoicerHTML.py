import csv

def read_customers_from_csv(filename='database.csv'):
    customers = []
    try:
        with open(filename, 'r', encoding='utf-8') as csv_file:
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
        print(f"Error: {filename} not found!")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
    return customers


    
