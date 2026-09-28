import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml


url = "https://www.amazon.in/Dell-Anti-Glare-Graphics-Keyboard-Dedicated/dp/B0GWHPGLGM/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.rMqYfF-Vzn4jNyEvKXg9lZgz65ruk6mwVDcSIe3fAoF9lOBpe2lnR0TlCGz03-yHUSf_yp0GBAjxpTDBICIIiNmyWkpLrDWU2HmKNkX0bJ8.NvjDA2ALHGn3p1SJWMQXc6YVXFIg33EusyYWluU-Cq8&dib_tag=se&keywords=dell+g6+gaming+laptop&qid=1789821763&sr=8-1-spons&aref=DYDJLTCQN9&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    html_content = response.text
    # print(response.status_code)
else:
    print(f"fetching error- {response.status_code}")


soup = BeautifulSoup(html_content, "lxml")
product_title = soup.find("span", id="productTitle").text.strip()
product_price = soup.find("span", class_="a-price-whole").text.strip()
span_tag = soup.find("span", id="acrPopover")
product_rating = span_tag.get("title")
product_details = soup.find("ul", class_="a-unordered-list a-vertical a-spacing-mini").text.strip()
product_reviews = soup.find("ul", id="localTopReviewsList").text.strip()

product_info1 = [{
    "Product_title": product_title,
    "Product_price": product_price,
    "Product_rating": product_rating,
    "Product_details": product_details,
    "Product_reviews": product_reviews
}]
# Convert to DataFrame for column-wise output
df12 = pd.DataFrame(product_info1)

table = soup.find("table", class_="a-normal a-spacing-micro")
data = {}
if table:
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 2:
            key = cells[0].text.strip()
            value = cells[1].text.strip()
            data[key] = value

df9 = pd.DataFrame(list(data.items()), columns=["Attribute", "Value"])


review_content = soup.find("ul", id="localTopReviewsList")

customer_names = [name.text.strip() for name in review_content.find_all("span", class_="a-profile-name")]
customer_ratings = [rating.text.strip() for rating in review_content.find_all("span", class_="a-icon-alt")]
customer_comments = [comment.text.strip() for comment in review_content.find_all("h5", class_="_Y3Itd_single-review-title_2aKRE")]
customer_additionals = [additional.text.strip() for additional in review_content.find_all("div", class_="_Y3Itd_contain-rich-content_2IORW")]

# Combine all into rows
reviews = []
for name, rating, comment, additional in zip(customer_names, customer_ratings, customer_comments, customer_additionals):
    reviews.append({
        "Customer Name": name,
        "Rating": rating,
        "Comment": comment,
        "Additional": additional
    })

# Convert to DataFrame for column-wise output
df = pd.DataFrame(reviews)


table_list = soup.find_all("table", class_="a-keyvalue prodDetTable")
data1 = {}
for idx, table1 in enumerate(table_list):
    if idx >= 5:
        break
    rows1 = table1.find_all("tr")
    for row1 in rows1:
            cells1 = row1.find_all(["th", "td"])
            if len(cells1) == 2:
                key1 = cells1[0].text.strip()
                value1 = cells1[1].text.strip()
                data1[key1] = value1
    

df4 = pd.DataFrame(list(data1.items()), columns=["Attribute", "Value"])


data2 = {}

for idx2 in range(6, 10):   # 7th to 10th table
    table2 = table_list[idx2]
    rows2 = table2.find_all("tr")
    for row2 in rows2:
        cells2 = row2.find_all(["th", "td"])
        if len(cells2) == 2:
            key2 = cells2[0].text.strip()
            value2 = cells2[1].text.strip()
            data2[key2] = value2

df5 = pd.DataFrame(list(data2.items()), columns=["Attribute", "Value"])




with pd.ExcelWriter("project_output.xlsx") as writer:
    df12.to_excel(writer, sheet_name="Product_Info", index=False)
    df9.to_excel(writer, sheet_name="Additional_Details", index=False)
    df.to_excel(writer, sheet_name="Product_Reviews", index=False)
    df4.to_excel(writer, sheet_name="Laptop_Details1", index=False)
    df5.to_excel(writer, sheet_name="Laptop_Details2", index=False)

print("✅ Sabhi DataFrames ek hi Excel file me alag, alag sheets ke saath save ho gaye: project_output.xlsx")














