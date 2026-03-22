# SegmenAI – Customer Segmentation Dashboard

SegmenAI is a **data-driven Customer Segmentation and Insights application** built to help businesses understand their customer base, identify high-value clients, and optimize marketing, retention, and pricing strategies. The app leverages **RFM (Recency, Frequency, Monetary) analysis** and **KMeans clustering** to segment customers and generate actionable insights through interactive dashboards.  

**SegmenAI** is a complete end-to-end **customer analytics solution**, combining Python, ML, and interactive BI dashboards to help businesses make smarter, revenue-focused decisions.

---

## 1. Problem Statement

Many businesses struggle to understand the behavior of their customers and identify patterns that can help improve:

* **Customer retention**
* **Marketing targeting**
* **Revenue optimization**

Without segmentation, companies often treat all customers the same, leading to **inefficient campaigns** and **missed revenue opportunities**.

---

## 2. Solution Overview

SegmenAI solves this problem by:

1. **Analyzing customer transactional data** using RFM metrics:

   * **Recency:** Days since last purchase  
   * **Frequency:** Number of purchases  
   * **Monetary:** Total spending  

2. **Segmenting customers** using **KMeans clustering** to identify patterns and groups.

3. **Providing actionable insights** through a **highly interactive Streamlit dashboard**, allowing businesses to:

* Visualize customer segments
* Compare monetary contributions
* Identify loyal, recent, or inactive customers
* Receive **personalized recommendations** per segment

---

## 3. Key Features

* **RFM-based Customer Segmentation**  
  Identify high-value, occasional, recent, and inactive customers.

* **Interactive Visualizations**  

  * Customer count per segment  
  * Monetary contribution per segment  
  * Average recency and frequency per segment  

* **Customer Table with Recommendations**  
  Explore customer details per segment interactively and see tailored business actions for each segment, such as:

  | Segment             | Recommendation |
  |--------------------|----------------|
  | High-Value Loyal    | Reward with VIP offers, loyalty perks, early access to products. |
  | Inactive Low-Value  | Send re-engagement campaigns with discounts or reminders. |
  | Recent Moderate     | Upsell or cross-sell complementary products. |
  | Occasional Buyer    | Encourage engagement through seasonal campaigns or bundles. |

* **Pre-trained Models**  
  Efficient clustering with pre-trained KMeans model and feature scaler for faster predictions.

---

## 4. Tools & Technologies

* **Python** – Core language for data processing and model training  
* **Streamlit** – For building the interactive dashboard  
* **Plotly** – For highly interactive and aesthetic visualizations  
* **Pandas & NumPy** – Data wrangling and numerical computations  
* **Scikit-learn** – Feature scaling and KMeans clustering  
* **Cloudflare R2** – S3-compatible cloud storage for dataset hosting  
* **Docker & Docker Compose** – Containerization for reproducible deployment  

---

## 5. Data Source

* The dataset consists of **customer transactions**, including:

  * `CustomerID`  
  * `InvoiceNo`  
  * `InvoiceDate`  
  * `Quantity`  
  * `UnitPrice`  

* Data is **stored in Cloudflare R2** for scalability and accessed directly by the Streamlit app.

---

## 6. Architecture & Workflow
1. **Data Upload** – Customer transactions CSV is uploaded to Cloudflare R2.  
2. **RFM Feature Engineering** – Recency, Frequency, Monetary metrics are calculated.  
3. **Clustering** – Customers are segmented using KMeans.  
4. **Personalized Recommendations** – Assign actionable recommendations to each segment.  
5. **Visualization** – Interactive dashboards show segment metrics and customer insights.  

---

## 7. Visualizations & Dashboard

* **Customer Count per Segment** – Quickly identify segment size.  
* **Monetary Contribution per Segment** – Understand which customers drive revenue.  
* **Average Recency & Frequency** – Identify engagement patterns.  
* **Interactive Customer Table with Recommendations** – Filter and explore customers by segment and receive actionable insights.  

*All plots are interactive using Plotly for zooming, filtering, and tooltip insights.*

---

## 8. Business Value

SegmenAI provides **direct business impact**:

* **Increase Revenue** – Identify high-value customers for targeted campaigns.  
* **Optimize Marketing Spend** – Focus on segments most likely to convert.  
* **Customer Retention** – Identify inactive customers and take corrective action.  
* **Strategic Insights** – Make data-driven business decisions.  
* **Actionable Recommendations** – Personalized business actions per customer segment for marketing, upselling, or retention campaigns.  

---

## 9. Future Improvements
* **Add predictive models** for churn and lifetime value.  
* **Real-time updates** when new transactions are uploaded.  
* **Multi-segment comparisons** with interactive dashboards.  
* **Integration with CRM or Marketing tools** for automated actions.  

---
