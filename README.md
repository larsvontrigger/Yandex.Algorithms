# Production Plan Automation with PyQt and Excel Integration

This project is designed to automate the workflow in a quality audit environment for automotive manufacturing. It uses Python and PyQt to extract daily production plans from Excel sheets and enhance productivity by linking relevant part measurement documents. 

## Overview

In the automotive industry, quality auditors frequently deal with repetitive tasks such as locating production plans, selecting shift-specific parts, and manually opening Excel files to record measurements. This tool automates that process by:
- Extracting daily production plans from a structured Excel sheet.
- Filtering parts based on the selected work shift (morning, afternoon, night).
- Consolidating duplicate parts (e.g., left and right components).
- Providing clickable hyperlinks to the relevant Excel files where part-specific measurement data is stored.
- Supporting multiple Excel sheets, with parts linked to specific worksheets when required.


##  Technology Stack

- **Python**: Core logic for handling data extraction and processing.
- **PyQt**: GUI interface for selecting shifts, displaying parts, and interacting with files.
- **Pandas**: Data manipulation library to work with Excel sheets.
- **OpenPyXL**: For Excel file reading and manipulation.
- **Platform support**: MacOS, Windows.
