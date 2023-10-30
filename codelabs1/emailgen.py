import pandas as pd
import re  # Import the regular expressions library

# Specify the absolute path to your Excel file
file_path = r'C:\Users\admin\Desktop\Python-Projects\CS\codelabs1\Test_Files.xlsx'

# Specify the sheet names you want to read (in this case, "3B" and "3C")
sheet_names = ['3B', '3C']

# Define the email domain
email_domain = "gmail.com"

generated_emails  = set()

# Iterate through each sheet name
for sheet_name in sheet_names:
    # Read the Excel sheet into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Define a function to generate email addresses
    def generate_unique_email(student_name, email_domain):
        # Remove special characters and spaces from the student_name
        cleaned_name = re.sub(r'[^a-zA-Z0-9 ]', '', student_name)

        # Split the cleaned name by spaces
        name_parts = cleaned_name.split()
        
        # Initialize variables for last name, first name, middle name, and forth name
        last_name = ""
        first_name = ""
        middle_name = ""
        forth_name = ""
        
        # Check the number of name parts and assign them accordingly
        if len(name_parts) >= 1:
            last_name = name_parts[0]
        if len(name_parts) >= 2:
            middle_name = name_parts[1]
        if len(name_parts) >= 3:
            middle_name = name_parts[2]
        if len(name_parts) >= 4:
            forth_name = name_parts[3]

        # Take the first letter of the first name and concatenate it with the last name
        email = f"{last_name.lower()[0]}{middle_name.lower()}@{email_domain}"
        # Make the email address unique if it already exists
        suffix = 1
        while email in generated_emails:
            email = f"{last_name.lower()[0]}{middle_name.lower()}{suffix}@{email_domain}"
            suffix += 1
        
        # Add the generated email to the set
        generated_emails.add(email)
        
        return email

    # Apply the generate_email function to create email addresses
    df['Email Address'] = df['Student Name'].apply(lambda x: generate_unique_email(x, email_domain))

    # Save as TSV (Tab-Separated Values)
    tsv_file_path = rf'C:\Users\admin\Desktop\Python-Projects\CS\codelabs1\emailgenerated\Testfilestsv_{sheet_name}.tsv'
    df.to_csv(tsv_file_path, sep='\t', index=False)

    # Save as CSV (Comma-Separated Values)
    csv_file_path = rf'C:\Users\admin\Desktop\Python-Projects\CS\codelabs1\emailgenerated\Testfilescsv_{sheet_name}.csv'
    df.to_csv(csv_file_path, index=False)

    print(f"DataFrame for sheet '{sheet_name}' saved as TSV: {tsv_file_path}")
    print(f"DataFrame for sheet '{sheet_name}' saved as CSV: {csv_file_path}")
