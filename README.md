# AUTOMATED-REPORT-GENERATION

COMPANY NAME:CODTECH IT SOLUTIONS
NAME : SANGITA KUMARI
INTERN ID: CTO6DF1191
DOMAIN:PYTHON PROGRAMMING
DURATION:6 WEEKS
MENTOR:NEELA SANTHOSH




Quarterly Sales Analysis Report Generator

This project is a Python-based automated report generation tool that reads a CSV file containing sales data, analyzes it, creates a revenue visualization, and compiles the results into a professional PDF report. It's ideal for businesses and analysts who want quick insights from sales data without manually formatting reports.

🚀 Features
* Data Analysis: Summarizes total revenue, units sold, and identifies the best-selling product.

* Chart Generation: Visualizes revenue by category using a bar chart.

* PDF Report Creation: Generates a well-structured PDF report with a header, footer, summary, chart, and detailed data table.

* Auto Recovery: If the required CSV file is missing, the script creates a sample one and prompts a re-run.

📂 Project Structure
* sales_data.csv: Input CSV file with sales data.

* revenue_chart.png: Temporarily saved chart image used in the report.

Sample_Report.pdf: Output PDF * file containing the full report.

* main.py: Python script that runs the complete workflow.

🧰 Dependencies
Install the following Python libraries before running the script:

bash
Copy code
pip install pandas matplotlib fpdf
Note: The script uses the FPDF library (not fpdf2) for creating PDFs.

📈 How It Works
The project is organized into modular functions, each responsible for a different part of the report pipeline:

1. analyze_data(file_path)
Reads sales data from a CSV file.

* Computes:

* Total Revenue

* Total Units Sold

* Best-selling product

* Revenue grouped by category

2. create_chart(data, output_path)
* Plots a bar chart of revenue by category using matplotlib.

* Saves the chart as a PNG file for use in the PDF.

3. generate_report(data_df, summary, chart_path, output_path)
*Uses a custom PDF class (inheriting from FPDF) to format the report.

*Includes:

Header and footer on each page

* Executive summary

* Embedded revenue chart

*Full data table of sales

4. main()
* Orchestrates the workflow:

* Checks if sales_data.csv exists

* Analyzes data

* Creates the chart

* Generates the PDF report

* Cleans up temporary files

📌 Sample Data Format
If sales_data.csv is missing, the script creates the following sample data:

csv
Copy code
Date,Product,Category,Units Sold,Revenue
2023-01-15,Laptop,Electronics,50,45000
2023-01-17,Smartphone,Electronics,120,60000
📝 Customization Tips
* Add more rows and categories to sales_data.csv for more comprehensive reporting.

* Modify the create_chart() function to generate different types of visualizations.

* Customize the PDF class to match your organization’s branding.

✅ Usage
Simply run the script:

bash
Copy code
python main.py
If everything runs correctly, you’ll get a Sample_Report.pdf in the same directory.

📬 Output Example
* Sample_Report.pdf contains:

* A bold title page

* An executive summary of key sales metrics

* A clean revenue bar chart

* A full table of raw sales data

🧹 Cleanup
The temporary chart image (revenue_chart.png) is automatically deleted after the PDF is created.

📧 Author
Created as a lightweight yet professional reporting tool using Python's data and visualization stack.
