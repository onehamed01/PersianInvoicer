from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pathlib
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

# Function to generate PDF with 5 invoices per page
def generate_invoices(customers, font_path='NotoNaskhArabic-Regular.ttf', output_file='customer_labels.pdf'):
    pdf = FPDF()
    pdf.set_auto_page_break(False)  # Disable auto page break
    
    # Add Persian font
    pdf.add_font(family='NotoNaskhArabic', fname=pathlib.Path(font_path))
    
    # Page dimensions
    page_width = 210  # A4 width in mm
    page_height = 297  # A4 height in mm
    margin = 10  # margin in mm
    usable_width = page_width - 2 * margin
    usable_height = page_height - 2 * margin
    
    # Invoice box dimensions (5 boxes per page)
    box_width = usable_width  # Full width
    box_height = usable_height / 5  # Each box is 1/5 of page height
    box_spacing = 2  # Small spacing between boxes
    
    # Font size
    font_size = 10
    line_height = 6
    
    # Enable text shaping for Persian RTL
    pdf.set_text_shaping(use_shaping_engine=True, direction='rtl', script='arab', language='fas')
    pdf.set_font('NotoNaskhArabic', size=font_size)
    
    # Process customers in groups of 5
    for idx, (name, phone, address, postal) in enumerate(customers):
        # Calculate which position on page (0-4)
        position_on_page = idx % 5
        
        # Add new page for every 5 invoices
        if position_on_page == 0:
            pdf.add_page()
        
        # Calculate position for current invoice box
        box_y = margin + position_on_page * box_height
        
        # Draw border/framework around invoice
        pdf.rect(margin, box_y, box_width, box_height - box_spacing, style='D')
        
        # Set position inside the box with padding
        x = margin + 5  # Small padding inside box
        y = box_y + 5   # Small padding inside box
        
        pdf.set_xy(x, y)
        
        # Header (slightly larger font)
        pdf.set_font('NotoNaskhArabic', size=font_size + 1)
        pdf.cell(box_width - 10, line_height, text='فاکتور مشتری', align='C', new_x=XPos.LEFT, new_y=YPos.NEXT)
        
        # Fields with Persian labels (smaller font)
        pdf.set_font('NotoNaskhArabic', size=font_size)
        pdf.set_x(x)
        
        pdf.cell(box_width - 10, line_height, text=f'نام و نام خانوادگی: {name}', new_x=XPos.LEFT, new_y=YPos.NEXT)
        pdf.set_x(x)
        
        pdf.cell(box_width - 10, line_height, text=f'شماره تماس: {phone}', new_x=XPos.LEFT, new_y=YPos.NEXT)
        pdf.set_x(x)
        
        pdf.cell(box_width - 10, line_height, text=f'آدرس محل سکونت: {address}', new_x=XPos.LEFT, new_y=YPos.NEXT)
        pdf.set_x(x)
        
        pdf.cell(box_width - 10, line_height, text=f'کد پستی: {postal}', new_x=XPos.LEFT, new_y=YPos.NEXT)

    # Save the PDF
    pdf.output(output_file)
    print(f"PDF generated: {output_file} with {len(customers)} invoices")

# Read customers from CSV and generate PDF
customers = read_customers_from_csv('database.csv')
if customers:
    generate_invoices(customers)
else:
    print("No customers found in database.csv")