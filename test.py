Write a Python program that acts as a Data Sovereignty Guardian. The program should:

- Use pandas to read an Excel file named "data_sovereignty.xlsx". Assume the file has merged cells in various places, so handle merged cells appropriately by filling forward or using appropriate pandas options like pd.read_excel with merge handling.

- The Excel structure is:
  - Column B: "Source Country"
  - Column C: "Destination Country"
  - Column D: "Data Category" with possible values: "Personal Data", "Sensitive Personal Data", "Corporate Client Data", "Corporate Third Party Data", "Bank Derived Data", "Transaction Data", "Country Specific Data". Each source-destination pair has 7 rows, one for each category.
  - Column K: Risk Driver "Can the country data be hosted externally?" with values 1 (Yes), 2 (Yes with condition), 3 (No)
  - Column L: "Can the data be accessed by cross border users (non-country based users)?" with values 1 (Yes), 2 (Yes with condition), 3 (No)
  - Column M: "Can the data be processed externally at a location outside the country?" with values 1 (Yes), 2 (Yes with condition), 3 (No)
  - Columns P to AC: Conditions for cross-border data, with values "Y" or blank.
  - Column AD: "Caveats for the conditions" in natural language English.
  - Column AF: "Risk Tier" with values blank, 1, 2, 3, 4, or 5.

- Prompt the user for input: Source Country, Destination Country, and Data Category (must match one of the 7 categories exactly).

- Filter the DataFrame to find the matching row based on the user inputs (case-insensitive matching recommended).

- If no match found, output an error message and exit gracefully.

- For the matching row, extract:
  - Risk drivers from K, L, M (map 1/2/3 to "Yes"/"Yes with condition"/"No").
  - List of conditions from P to AC where value is "Y".
  - Caveat from AD – summarize it concisely in the output to guide the user on next steps (e.g., rephrase into bullet points or actionable steps if possible; keep it simple without external NLP libraries).
  - Risk Tier from AF.

- Output a formatted summary including:
  - Data sovereignty guidance based on the risk drivers.
  - List of required conditions.
  - Summarized caveats with actionable next steps.
  - Risk Tier.

- Follow Python best practices: Use type hints, docstrings, error handling, modular functions (e.g., one for loading data, one for querying, one for summarizing), and clean code structure. Use argparse or input() for user inputs. Make it runnable from command line.