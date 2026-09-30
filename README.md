# 💻 Amazon Product Web Scraper in Python 📊🛒

The **Amazon Product Web Scraper** is a Python project that extracts detailed product information, specifications, and customer reviews from Amazon product pages.  
It organizes the scraped data into multiple **Excel sheets** for easy analysis, making it a powerful tool for e-commerce research, competitor tracking, and portfolio projects.

---

## 🔹 Features
- Scrapes **product title, price, rating, details, and reviews**  
- Extracts **technical specifications** from product tables  
- Collects **customer names, ratings, and comments**  
- Saves all extracted data into a **single Excel file** with multiple sheets  
- Uses **BeautifulSoup + Requests** for HTML parsing  
- Handles **structured tabular data** for clean DataFrame output  

---


## 🔹 Tools & Technologies Used
- **Python 3.x** – Core programming language  
- **requests** – For fetching HTML content  
- **BeautifulSoup (bs4)** – For parsing and extracting data  
- **lxml** – Fast HTML parser  
- **pandas** – For DataFrame manipulation and Excel export
  

---

## 🔹 Results
1. Extracted **product info** (title, price, rating, details, reviews).  
2. Parsed **technical specification tables** into structured DataFrames.  
3. Collected **customer reviews** with names, ratings, and comments.  
4. Exported all data into **project_output.xlsx** with multiple sheets:  
   - `Product_Info`  
   - `Additional_Details`  
   - `Product_Reviews`  
   - `Laptop_Details1`  
   - `Laptop_Details2`  

---

## 🔹 Example Usage
```bash
# Clone the repository
git clone https://github.com/msriv6-prog/web_scraping_project.git
cd web_scraping_project

# Run the script
python main2.py
```
---

## ✅ Output Example
After running the script, you’ll get an Excel file `project_output.xlsx` with multiple sheets:

### Sheet: Product_Info
| Product_title      | Product_price | Product_rating       |
|--------------------|---------------|----------------------|
| Dell Gaming Laptop | 89,990        | 4.3 out of 5 stars   |

### Sheet: Product_Reviews
| Customer Name | Rating | Comment                        | Additional        |
|---------------|--------|--------------------------------|-------------------|
| Rahul         | ⭐⭐⭐⭐   | "Great performance!"           | Verified Purchase |
| Sneha         | ⭐⭐⭐    | "Battery life could be better."| Verified Purchase |

---

## 🔹 Future Improvements
- Add **multi-URL scraping** for batch product analysis  
- Integrate **Tkinter GUI** for user-friendly scraping  
- Include **progress bar and status messages** during scraping  
- Enhance **Excel formatting** (colors, bold headers, conditional formatting)  
- Support **CSV/JSON export options**  

---

## 🔹 Author
👨‍💻 Developed by **Mohit**  
📌 Connect with me on [LinkedIn](https://www.linkedin.com/in/mohit-srivastava-343399349)









