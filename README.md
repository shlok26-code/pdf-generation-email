# Automatically Generate a PDF and Send It by Email

## Introduction

This project automates the process of generating a sales summary report for second-hand cars and sending it via email. The script processes sales data, identifies key insights (such as top-selling models and most popular manufacturing years), and generates a PDF report with a pie chart visualization. The report is then automatically emailed to the intended recipient.

## Features

- Loads car sales data from a JSON file.
- Processes the data to extract meaningful statistics.
- Generates a summary report as a PDF.
- Includes a pie chart for better visualization.
- Sends the generated report via email.

## File Structure

```
|-- scripts/
    |-- cars.py         # Main script for processing car sales data
    |-- emails.py       # Handles email generation and sending
    |-- reports.py      # Generates reports for fruit inventory
    |-- reports1.py     # Generates reports for car sales
    |-- example_old.py  # Example script for sending a fruit inventory report
    |-- example_new.py  # Example script with a modified sender and an additional entry
    |-- car_sales.json  # Sample sales data file (not included here)
```

## Dependencies

Ensure you have the following Python packages installed before running the scripts:

```sh
pip install reportlab matplotlib
```

## Setup and Execution

### 1. Clone the repository

```sh
git clone https://github.com/your-repo/your-project.git
cd your-project
```

### 2. Run the Car Sales Report Script

```sh
python3 scripts/cars.py
```

This script will:

- Read sales data from `car_sales.json`
- Analyze the data
- Generate `cars.pdf` containing the summary and pie chart
- Send the report via email

### 3. Run the Fruit Inventory Report Scripts (Optional)

To generate and send a fruit inventory report, execute:

```sh
python3 scripts/example_old.py
```

Or

```sh
python3 scripts/example_new.py
```

The second script includes an additional entry (`kiwi`) and uses `automation@example.com` as the sender.

## Code Explanation

### `cars.py`

This script processes the car sales data from `car_sales.json`, calculates key metrics (highest revenue, most sales, most popular year), generates a PDF report, and emails it.

### `emails.py`

Handles email generation and sending. It formats the email content and attaches the generated PDF.

### `reports.py`

Generates PDF reports for fruit inventory.

### `reports1.py`

Generates PDF reports for car sales, formatting data into tables and including a pie chart for visualization.

### `example_old.py`

Example script that generates a fruit inventory report and sends it via email.

### `example_new.py`

Modified version of `example_old.py`, using a different sender (`automation@example.com`) and adding an extra fruit (`kiwi`).

## Expected Output

Upon execution, the `cars.py` script will generate a PDF report (`cars.pdf`) containing:

- A summary of the most sold car model, highest revenue car, and most popular manufacturing year.
- A table of all car sales data formatted as `Car Make Model (Year) | Price | Total Sales`.
- A pie chart visualization of car sales distribution.
- The generated PDF will be emailed to the recipient.

For fruit inventory reports, the scripts will generate a PDF titled **"A Complete Inventory of My Fruit"**, listing all fruit items and their quantities and send it via email.

## Screenshots

### 1. Sample Email with Attached Report



### 2. PDF Report Preview



### 3. Pie Chart Visualization


![Automating_PDF_report_generation_1](https://github.com/user-attachments/assets/9fc29e25-89ab-4472-9c3b-4ddf5fbb5355)
![Automating_PDF_report_generation_2](https://github.com/user-attachments/assets/300f10a0-997a-4160-9d10-bdef1e56735d)
![Automating_PDF_report_generation_3](https://github.com/user-attachments/assets/40f7eb61-4409-40fa-8d44-29078ff3e3d8)
![Automating_PDF_report_generation_4](https://github.com/user-attachments/assets/8b944d73-8f83-453e-8cae-dab538f2be6e)
![Automating_PDF_report_generation_5](https://github.com/user-attachments/assets/a33b7888-7015-46be-8085-0ca67267b7a7)
![Automating_PDF_report_generation_6](https://github.com/user-attachments/assets/3669e83f-4e98-4965-92e4-be498095f6f7)
![Automating_PDF_report_generation_7](https://github.com/user-attachments/assets/d64a9770-2627-45f0-bf5e-57157fd4590e)
![Automating_PDF_report_generation_8](https://github.com/user-attachments/assets/390389ec-6251-46b0-81ee-41e290e7260f)
![Automating_PDF_report_generation_9](https://github.com/user-attachments/assets/0df706b6-e1e4-4a37-bc18-f088c1782bf4)
![Automating_PDF_report_generation_10](https://github.com/user-attachments/assets/5fc8c52f-9a03-4d1f-9b47-819805cef371)




## Troubleshooting

### SMTP Error: `Recipient address rejected`

If you receive an error like:

```sh
smtplib.SMTPRecipientsRefused: {'user': (550, b'5.1.1 <user>: Recipient address rejected: User unknown in local recipient table')}
```

Ensure that the recipient email address is valid and configured correctly in `cars.py` or `example_old.py/example_new.py`.

### Permissions Issue

If you encounter permission errors while executing the scripts, run:

```sh
chmod +x scripts/cars.py
```

Then try running the script again.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


💡 Contributions are welcome! If you have any improvements or suggestions, feel free to fork the repository and submit a pull request. 🚀

## Author

Shlok Sharma

