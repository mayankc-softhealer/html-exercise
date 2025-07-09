from jinja2 import Environment, FileSystemLoader #, Template
import pdfkit

#name of the folder where index file is located.
file_loader = FileSystemLoader('templates')

#This object is needed to create a template object.
env = Environment(loader=file_loader)

#path of the HTML file reletive to the folder.
template = env.get_template('./invoice.html')

record_data = [
    ['Mark-1 Spaceship', 60.4, 1, 60.4],
    ['Mark-2 Spaceship', 400.4, 1, 60.4],
    ['Mark-3 Spaceship', 600.4, 1, 60.4],
]

subtotal = 0
shipping = 20
total = 0

for item in record_data:
    subtotal += item[3]

total = subtotal + shipping

#Data dictionary to be supplied to our HTML file.
input_dict = {
    'order_number': '123',
    'billedto': """Mayank Chudasama
1234 Main
Apt. 4B
Springfield, ST 54321""",
    'shippedto': """Will Robinson
1234 Main
Aplpha Century
Lost in Space, ST 54321""",
    'order_date': 'May 20, 2072',
    'payment_method': """Visa Ending **** 0001
mayank@gmail.com""",
    'data_records': record_data, # List of list data -> [[], [],...]
    'subtotal': subtotal,
    'shipping': shipping,
    'total': total
}

# This function renders the data substituted HTML form.
output_html = template.render(input_dict)
print(output_html)


'''
HTML to PDF
'''

pdfkit.from_string(output_html, 'Invoice.pdf')

# from xhtml2pdf import pisa
# from io import BytesIO

# # BytesIO buffer
# output = BytesIO()

# # Convert HTML content to PDF
# pdf_status = pisa.CreatePDF(BytesIO(output_html.encode('utf-8')), dest=output)

# # Check if there was an error
# if pdf_status.err:
#     print("An error occurred.")
# else:
#     # Save the PDF to a file
#     with open("Invoice.pdf", "wb") as pdf_file:
#         pdf_file.write(output.getvalue())
#     print("PDF created successfully.")