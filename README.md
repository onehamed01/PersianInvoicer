# Persian Invoice Generator

A professional Python application for generating print-ready Persian invoice labels from CSV data. This project demonstrates modern software development practices, including modular architecture, RTL (Right-to-Left) text support, and print-optimized HTML generation.

## 🚀 Features

- **CSV Data Processing**: Reads customer information from CSV files with Persian column headers
- **RTL Support**: Full right-to-left text direction support for Persian/Farsi content
- **Print-Optimized Layout**: Generates HTML with 2-column layout, 8 invoices per page (4 per column)
- **Persian Font Integration**: Uses Google Fonts (Noto Sans Arabic) for proper Persian text rendering
- **Modular Architecture**: Clean, object-oriented design with a reusable `PersianInvoicerClass`
- **Customizable**: Configurable shop name, invoices per page, and output file name
- **Error Handling**: Robust error handling for file operations and data validation

## 📋 Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/PersianInvoicer.git
cd PersianInvoicer
```

2. Ensure you have Python 3.6 or higher installed:
```bash
python --version
```

## 📖 Usage

### Basic Usage

1. Prepare your CSV file with the following column headers (in Persian):
   - `نام و نام خانوادگی` (Full Name)
   - `شماره تماس` (Phone Number)
   - `آدرس محل سکونت` (Address)
   - `کد پستی` (Postal Code)

2. Run the application:
```bash
python main.py
```

3. The generated HTML file (`customer_labels.html`) will be created in the same directory.

### Customization

Edit `main.py` to customize the shop name and CSV file:

```python
from PersianInvoicer import PersianInvoicerClass

if __name__ == "__main__":
    invoicer = PersianInvoicerClass(
        file_name='database.csv',  # Your CSV file path
        shop_name='Your Shop Name'  # Your shop name
    )
    
    invoicer.generate_html(
        output_file='customer_labels.html',  # Output file name
        invoices_per_page=8,  # Total invoices per page
        invoices_per_column=4  # Invoices per column
    )
```

### Programmatic Usage

```python
from PersianInvoicer import PersianInvoicerClass

# Initialize the invoicer
invoicer = PersianInvoicerClass(
    file_name='database.csv',
    shop_name='Bella Shop'
)

# Read CSV data
customers = invoicer.read_csv()

# Generate HTML invoices
invoicer.generate_html(
    output_file='output.html',
    invoices_per_page=8,
    invoices_per_column=4
)

# Access customer data
customer_count = invoicer.get_customer_count()
all_customers = invoicer.get_customers()
```

## 📁 Project Structure

```
PersianInvoicer/
├── main.py                 # Entry point
├── PersianInvoicer.py      # Main class implementation
├── database.csv            # Sample CSV data
├── customer_labels.html    # Generated output
└── README.md              # This file
```

## 🎨 Output Format

The generated HTML file includes:
- **Print-optimized CSS**: Proper page breaks and margins for printing
- **2-column grid layout**: Efficient use of page space
- **Responsive design**: Adapts to different screen sizes
- **Professional styling**: Clean borders and typography

## 🔧 Technical Details

### CSV Format

The CSV file must include these columns (in Persian):
- `نام و نام خانوادگی`: Customer full name
- `شماره تماس`: Contact phone number
- `آدرس محل سکونت`: Residential address
- `کد پستی`: Postal code

### HTML Output

- UTF-8 encoding for proper Persian character support
- RTL (right-to-left) text direction
- Print media queries for optimal printing
- Page break controls to prevent invoice splitting

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 💡 Development Notes

This project was developed using AI-assisted programming, demonstrating:
- **Effective AI Collaboration**: Leveraging AI tools for rapid development while maintaining code quality
- **Iterative Refinement**: Customizing AI-generated code to meet specific requirements
- **Professional Standards**: Following best practices in code structure, documentation, and error handling
- **Problem-Solving**: Addressing complex requirements like RTL text support and print optimization

## 📞 Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

---

**Built with Python** | **Optimized for Persian/Farsi text** | **Print-ready output**

