Task 2: Data Visualization and Storytelling  

Dataset Used  
Superstore Sales Dataset  
The dataset contains sales transactions including order details, customer information, product categories, region, profit, discount, and shipping details.

 Objective  
The objective of this task was to clean the dataset using Python and create an interactive dashboard in Power BI that communicates meaningful business insights through data storytelling.

Tools & Technologies Used  
- Python (Pandas) – Data Cleaning & Feature Engineering  
- Power BI – Data Visualization & Dashboard Creation  
- VS Code  

Data Cleaning (Python)  
The dataset was cleaned before importing into Power BI to ensure accurate and reliable analysis.

Cleaning Steps Performed:
1. Converted `order_date` and `ship_date` into proper datetime format  
2. Removed duplicate records  
3. Removed null values  
4. Standardized text columns (lowercase and trimmed spaces)  
5. Created new feature `delivery_days` (shipping time analysis)  
6. Created `profit_status` column (profit vs loss classification)  
7. Extracted `year` and `month` from order date  

The cleaned dataset was saved as: cleaned_superstore.csv

Dashboard Overview (Power BI)
The dashboard was designed in two pages to tell a structured business story.

 Page 1 – Executive Overview  

- Total Sales (KPI Card)  
- Total Profit (KPI Card)  
- Total Orders (KPI Card)  
- Profit Margin  
- Sales by Region  
- Profit by Category  
- Monthly Sales Trend  

This page provides a high-level overview of overall business performance.
Page 2 – Performance Deep Dive  

- Profit by Sub-Category  
- Discount vs Profit (Scatter Analysis)  
- Sales by Segment  
- Average Delivery Days by Region  

This page focuses on identifying loss-making areas and operational insights.

Key Business Insights  

- Certain regions contribute significantly more revenue than others.  
- Technology category generates strong profitability.  
- High discount levels negatively impact profit margins.  
- Some sub-categories consistently generate losses.  
- Delivery time varies across regions and impacts operational efficiency.  

 Storytelling Approach  

The dashboard moves from overall business performance to deeper profitability and operational insights, helping stakeholders identify growth opportunities and areas that require strategic improvement.

Outcome  

Successfully combined Python-based data cleaning with Power BI visualization to create a professional, insight-driven business dashboard focused on data storytelling.


> This task strengthened my understanding of transforming raw data into actionable business insights using both technical and visualization tools.
