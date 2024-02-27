import markdown  # This assumes you're using the Python-Markdown package
from io import BytesIO
from datetime import datetime

def save_markdown(output_filename, markdown_string):
    # Convert Markdown to HTML
    html_string = markdown.markdown(markdown_string)

    # Save Markdown File
    with open(f'{output_filename}.md', 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_string)

    # Save HTML File
    with open(f'{output_filename}.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_string)

    # Attempt PDF Generation
    try:
        from weasyprint import HTML

        buffer = BytesIO()
        HTML(string=html_string).write_pdf(buffer)

        with open(f'{output_filename}.pdf', 'wb') as pdf_file:
            pdf_file.write(buffer.getvalue())
    except ImportError:
        print('WeasyPrint module not found. Skipping PDF generation.')
