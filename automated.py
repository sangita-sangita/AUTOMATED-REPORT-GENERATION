# Import necessary libraries

import pandas as pd  # For data manipulation and analysis

import matplotlib.pyplot as plt  # For creating charts and visualizations

from fpdf import FPDF  # For creating PDF documents

import os  # For interacting with the operating system (e.g., deleting files)



class PDF(FPDF):

    """

    Custom PDF class that inherits from FPDF.

    This allows us to define a custom header and footer that will appear on every page.

    """

    def header(self):

        # This method is called automatically to create the page header.

        # Set the font for the header (Arial, Bold, size 12)

        self.set_font('Arial', 'B', 12)

        # Create a cell for the header text.

        # 0: width (0 means full width)

        # 10: height

        # 'Corporate Report': text

        # 0: border (0 means no border)

        # 1: ln (1 means move to the next line after this cell)

        # 'C': align (Center)

        self.cell(0, 10, 'Corporate Report', 0, 1, 'C')

        # Add a line break for spacing after the header

        self.ln(10)



    def footer(self):

        # This method is called automatically to create the page footer.

        # Position the cursor at 1.5 cm from the bottom of the page

        self.set_y(-15)

        # Set the font for the footer (Arial, Italic, size 8)

        self.set_font('Arial', 'I', 8)

        # Create a cell for the page number.

        # f'Page {self.page_no()}' gets the current page number.

        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')



def analyze_data(file_path):

    """

    Reads data from a specified CSV file and performs a basic analysis.



    Args:

        file_path (str): The path to the input CSV file.



    Returns:

        tuple: A tuple containing the full DataFrame, a summary dictionary, 

               and a Series with revenue grouped by category.

    """

    # Step 1: Read the data from the CSV file into a pandas DataFrame

    df = pd.read_csv(file_path)



    # Step 2: Perform analysis

    # Calculate the sum of the 'Revenue' column

    total_revenue = df['Revenue'].sum()

    # Calculate the sum of the 'Units Sold' column

    total_units_sold = df['Units Sold'].sum()

    # Group data by 'Category' and sum the 'Revenue' for each category

    revenue_by_category = df.groupby('Category')['Revenue'].sum()

    # Find the row with the maximum 'Units Sold' to identify the best-selling product

    best_selling_product = df.loc[df['Units Sold'].idxmax()]



    # Step 3: Compile the analysis results into a dictionary for easy access

    analysis_summary = {

        "Total Revenue": f"${total_revenue:,.2f}", # Format as currency

        "Total Units Sold": f"{total_units_sold:,}", # Format with commas

        "Best Selling Product (Units)": f"{best_selling_product['Product']} ({best_selling_product['Units Sold']} units)",

    }



    # Step 4: Return the processed data and summaries

    return df, analysis_summary, revenue_by_category



def create_chart(data, output_path):

    """

    Creates a bar chart from the provided data and saves it as a PNG image.



    Args:

        data (pd.Series): The data to be plotted (e.g., revenue by category).

        output_path (str): The file path to save the output chart image.

    """

    # Step 1: Create a new figure and set its size

    plt.figure(figsize=(10, 6))

    # Step 2: Create a bar plot from the data with specified colors

    data.plot(kind='bar', color=['#4c72b0', '#55a868', '#c44e52'])

    # Step 3: Set the title and labels for the chart

    plt.title('Total Revenue by Category', fontsize=16)

    plt.ylabel('Revenue ($)', fontsize=12)

    plt.xlabel('Category', fontsize=12)

    # Step 4: Rotate the x-axis labels for better readability

    plt.xticks(rotation=45, ha='right')

    # Step 5: Adjust plot to ensure everything fits without overlapping

    plt.tight_layout()

    # Step 6: Save the generated chart to the specified file path

    plt.savefig(output_path)

    # Step 7: Close the plot to free up memory

    plt.close()



def generate_report(data_df, summary, chart_path, output_path):

    """

    Generates a formatted PDF report containing the analysis, chart, and raw data.



    Args:

        data_df (pd.DataFrame): The raw data to be included in the report table.

        summary (dict): A dictionary containing the key analysis findings.

        chart_path (str): The file path to the chart image.

        output_path (str): The file path to save the final PDF report.

    """

    # Step 1: Initialize the PDF object using our custom PDF class

    pdf = PDF()

    pdf.add_page()



    # --- Section: Report Title ---

    # Set font for the main title

    pdf.set_font('Arial', 'B', 24)

    # Add the title cell

    pdf.cell(0, 15, 'Quarterly Sales Analysis Report', 0, 1, 'C')

    # Add some vertical space

    pdf.ln(5)



    # --- Section: Analysis Summary ---

    # Set font for the section heading

    pdf.set_font('Arial', 'B', 16)

    pdf.cell(0, 10, '1. Executive Summary', 0, 1, 'L')

    # Set font for the body text

    pdf.set_font('Arial', '', 11)

    # Loop through the summary dictionary and add each item as a line in the PDF

    for key, value in summary.items():

        pdf.cell(0, 8, f'  - {key}: {value}', 0, 1, 'L')

    pdf.ln(10)



    # --- Section: Chart ---

    # Set font for the section heading

    pdf.set_font('Arial', 'B', 16)

    pdf.cell(0, 10, '2. Revenue by Category Visualization', 0, 1, 'L')

    # Calculate x-coordinate to center the image

    page_width = pdf.w - 2 * pdf.l_margin

    image_x = pdf.get_x() + (page_width - 160) / 2 # Assuming image width is 160

    # Embed the chart image into the PDF

    pdf.image(chart_path, x=image_x, w=160)

    pdf.ln(10)



    # --- Section: Data Table ---

    # Set font for the section heading

    pdf.set_font('Arial', 'B', 16)

    pdf.cell(0, 10, '3. Detailed Sales Data', 0, 1, 'L')

    

    # Set font for the table header

    pdf.set_font('Arial', 'B', 10)

    # Calculate an appropriate column width

    col_width = pdf.w / (len(data_df.columns) + 1)

    

    # Create the table header row

    for col in data_df.columns:

        pdf.cell(col_width, 10, col, 1, 0, 'C')

    pdf.ln()



    # Create the table body rows

    pdf.set_font('Arial', '', 9)

    # Iterate over each row in the DataFrame

    for index, row in data_df.iterrows():

        # Iterate over each item in the row

        for item in row:

            # Add a cell for each data point

            pdf.cell(col_width, 10, str(item), 1, 0, 'C')

        # Move to the next line after completing a row

        pdf.ln()



    # --- Final Step: Save the PDF ---

    # Write the PDF content to the specified output file

    pdf.output(output_path)

    print(f"Report successfully generated at: {output_path}")



def main():

    """

    Main function to orchestrate the entire report generation process.

    """

    # Define the file paths for input data, intermediate chart, and final report

    input_csv = 'sales_data.csv'

    chart_image = 'revenue_chart.png'

    output_pdf = 'Sample_Report.pdf'

    

    # Check if the input data file exists to avoid errors.

    if not os.path.exists(input_csv):

        print(f"Error: Data file not found at '{input_csv}'")

        # For demonstration, create a small sample file if it's missing.

        sample_data = """Date,Product,Category,Units Sold,Revenue

2023-01-15,Laptop,Electronics,50,45000

2023-01-17,Smartphone,Electronics,120,60000"""

        with open(input_csv, 'w') as f:

            f.write(sample_data)

        print("A sample 'sales_data.csv' has been created. Please run the script again.")

        return



    # --- Execute the workflow ---

    # 1. Analyze the data from the CSV file

    df, summary, revenue_by_category = analyze_data(input_csv)



    # 2. Create the visualization chart

    create_chart(revenue_by_category, chart_image)



    # 3. Generate the final PDF report with all the components

    generate_report(df, summary, chart_image, output_pdf)

    

    # 4. Clean up by deleting the temporary chart image file

    os.remove(chart_image)



# This is a standard Python construct.

# The code inside this block will only run when the script is executed directly.

if __name__ == '__main__':

    # A reminder for the user to install necessary libraries before running.

    # pip install pandas matplotlib fpdf2

    main()

