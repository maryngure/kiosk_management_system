# Kiosk Management System

A simple command-line **Kiosk Management System** built with Python. The project manages product inventory, records sales, generates sales reports, searches products, and saves data between sessions using text files.

## Features

* 🔐 **PIN Authentication**

  * Requires a PIN before accessing the main menu.
  * Uses string comparison to validate the PIN.

* 📦 **View Stock**

  * Displays available products, prices, and quantities.
  * Uses a nested dictionary to store inventory information.

* ➕ **Add/Restock Products**

  * Restocks existing products.
  * Allows new products to be added to the inventory.

* 🛒 **Sell Products**

  * Checks whether a product exists.
  * Validates the quantity entered.
  * Checks available stock before completing a sale.
  * Automatically updates inventory after a successful sale.

* 📊 **Sales Report**

  * Displays recorded sales.
  * Calculates total revenue.
  * Shows the number of unique products sold.
  * Identifies the best-selling product based on quantity sold.

* 🔎 **Product Search**

  * Allows users to search using part of a product name.
  * Search is case-insensitive.

* 💾 **Data Persistence**

  * Saves the current inventory to `inventory.txt`.
  * Loads previously saved inventory when the program starts.
  * Appends session sales to `sales.txt` so previous sales are preserved.

## Technologies Used

* Python
* Python Standard Library
* Text file handling
* Git & GitHub

## Python Concepts Practiced

This project was built to practice:

* Variables and data types
* Strings and string methods
* Dictionaries and nested dictionaries
* Lists
* Tuples
* Sets
* `if`, `elif`, and `else`
* `while` and `for` loops
* Functions
* Input validation
* `.isdigit()`
* `.lower()` and `.title()`
* File handling with `open()`
* Reading and writing text files
* `os.path.exists()`
* Formatted output using f-strings

## Project Structure

```text
kiosk-management-system/
│
├── kiosk_management.py
├── inventory.txt
├── sales.txt
└── README.md
```

> `inventory.txt` and `sales.txt` are created automatically when the program saves data.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/kiosk-management-system.git
```

### 2. Open the project folder

```bash
cd kiosk-management-system
```

### 3. Run the program

```bash
python kiosk_management.py
```

The program will ask for the kiosk owner name, kiosk name, and PIN before displaying the main menu.

## Main Menu

```text
===== MAIN MENU =====
1. View Stock
2. Add/Restock a product
3. Sell a product
4. View Sales Report
5. Search Products
6. Exit
```

## Data Storage

The project uses plain text files rather than a database.

### Inventory

The current inventory is stored in `inventory.txt` using a simple comma-separated format:

```text
Milk,70,20
Bread,65,15
Sugar,150,25
```

### Sales

Sales are stored in `sales.txt`:

```text
Milk,2,140
Bread,1,65
```

Sales are appended to the file so previous session records are not overwritten.


