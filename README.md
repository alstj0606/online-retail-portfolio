# 🛒 Online Retail Data Analysis Portfolio

<p align="right">
  <a href="#-english-version">🇺🇸 English</a> | 
  <a href="#-한국어-버전">🇰🇷 한국어</a>
</p>

---

## 🇺🇸 English Version

This repository contains a comprehensive data analysis project using UK online retail transaction data to evaluate sales structures, customer retention, and marketing channel performance.

---

## 1. Project Overview
This project analyzes the **Online Retail II** dataset to derive actionable business insights across three core domains:
1.  **Revenue Analysis:** Identifying growth drivers and sales trends.
2.  **Customer Retention:** Analyzing repurchase patterns and identifying dormant segments.
3.  **Channel Attribution:** Evaluating marketing efficiency through hypothesis-based modeling.

## 2. Project Titles
* **Project 1:** E-commerce Revenue Structure Analysis & Growth Point Identification
* **Project 2:** Customer Repurchase Pattern Analysis & Dormant Group Segmentation
* **Project 3:** Marketing Efficiency Strategy via Hypothesis-based Channel Performance

## 3. Dataset & Tech Stack
### Dataset: Online Retail II
* **Format:** CSV
* **Key Features:** `Invoice`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `Price`, `Customer ID`, `Country`

### Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, Matplotlib, Seaborn
* **IDE:** VS Code

---

## 4. Data Preprocessing
To ensure data integrity, the following steps were performed:
* **Cleaning:** Removed whitespace from column names and handled missing `Customer ID` values.
* **Transformation:** Converted `InvoiceDate` to datetime and generated `YearMonth` for time-series analysis.
* **Filtering:** Included only valid transactions ($Quantity > 0$ and $Price > 0$).
* **Feature Engineering:** Calculated `Sales` ($Quantity \times Price$).

---

## 5. Analysis Details

### 5-1. Sales Analysis
* Monthly revenue trends and seasonality.
* Top 10 countries and products by revenue contribution.
* **Outputs:** `monthly_sales.png`, `country_sales.png`, `product_sales.png`

### 5-2. Repurchase & Dormant Customer Analysis
* **Recency/Frequency:** Aggregated order counts and intervals per customer.
* **Dormancy:** Defined "Dormant Customers" as those with no purchases within the last 90 days.
* **Outputs:** `purchase_frequency.png`, `repurchase_distribution.png`, `dormant_distribution.png`

### 5-3. Channel Performance Analysis
*Since the dataset lacks original source tags, synthetic variables were assigned for framework implementation:*
* **Acquisition (First Order):** Paid Search, Social, Direct.
* **Retention (Repeat Order):** Email, Direct, Social.
* **Outputs:** `channel_orders.png`, `channel_sales.png`, `channel_aov.png`

---

## 6. Key Metrics
* **Sales:** $Quantity \times Price$
* **Recency:** Reference Date - Last Purchase Date
* **Frequency:** Total order count per customer
* **Monetary:** Total spending per customer
* **AOV (Average Order Value):** Total Revenue / Total Orders

---

## 7. Limitations & Future Work
* **Channel Data:** Performance metrics are based on assumed variables due to lack of raw attribution data.
* **Categorization:** Analysis relied on product descriptions as explicit category metadata was unavailable.
* **Dormancy Threshold:** Used a fixed 90-day window which may vary by business industry.


<img width="599" height="376" alt="image" src="https://github.com/user-attachments/assets/7b5e1edf-1fe7-4a02-a751-4726a7dab69d" />


## 🇰🇷 한국어 버전

# Online Retail Portfolio Project

## 1. Project Overview
영국 온라인 리테일 거래 데이터를 활용해 매출 구조, 고객 재구매 패턴, 그리고 가정 기반 유입 채널 성과를 분석한 데이터 분석 포트폴리오 프로젝트입니다.

하나의 이커머스 거래 데이터를 기반으로 아래 3가지 관점에서 분석을 진행했습니다.

1. 매출 분석
2. 재구매 및 휴면 고객 분석
3. 가정 기반 채널 성과 분석

## 2. Project Titles

### Project 1
이커머스 주문 데이터 기반 매출 구조 분석 및 매출 개선 포인트 도출

### Project 2
고객 구매 이력 기반 재구매 패턴 분석 및 휴면 고객군 식별

### Project 3
가정 기반 유입 채널별 성과 분석을 통한 마케팅 효율 개선 전략 제안

## 3. Dataset
- Dataset: Online Retail II
- Format: CSV
- Main Columns:
  - Invoice
  - StockCode
  - Description
  - Quantity
  - InvoiceDate
  - Price
  - Customer ID
  - Country

## 4. Tools
- Python
- Pandas
- Matplotlib
- VSCode

## 5. Data Preprocessing
- 컬럼명 공백 제거
- InvoiceDate를 datetime 형식으로 변환
- Customer ID가 없는 행 제거
- Quantity > 0, Price > 0 조건으로 정상 주문만 필터링
- Sales = Quantity * Price 컬럼 생성
- YearMonth 컬럼 생성

## 6. Analysis Details

### 6-1. Sales Analysis
- 월별 매출 추이 분석
- 국가별 매출 상위 10개 분석
- 상품별 매출 상위 10개 분석

결과물:
- outputs/monthly_sales.png
- outputs/country_sales.png
- outputs/product_sales.png

### 6-2. Repurchase / Dormant Customer Analysis
- 고객별 주문 횟수 집계
- 재구매 고객 여부 분석
- 최근 90일 미구매 고객을 휴면 고객으로 정의하여 분석

결과물:
- outputs/purchase_frequency.png
- outputs/repurchase_distribution.png
- outputs/dormant_distribution.png

### 6-3. Channel Performance Analysis
원본 데이터에는 마케팅 유입 채널 정보가 존재하지 않기 때문에, 분석 프레임워크 구현을 위해 가정 기반 채널 변수를 생성했습니다.

- 첫 구매 주문: Paid Search / Social / Direct 중 하나 배정
- 재구매 주문: Email / Direct / Social 중 하나 배정

결과물:
- outputs/channel_orders.png
- outputs/channel_sales.png
- outputs/channel_aov.png

## 7. Key Metrics
- Sales = Quantity × Price
- Recency = 기준일 - 마지막 구매일
- Frequency = 고객별 주문 횟수
- Monetary = 고객별 총 구매 금액
- AOV = 채널별 총매출 / 채널별 주문 수

## 8. Limitations
- 원본 데이터에는 실제 유입 채널 정보가 없어 채널 분석은 가정 기반 파생 변수로 진행했습니다.
- 상품 카테고리 정보가 별도로 존재하지 않아 상품 설명 중심으로 분석했습니다.
- 휴면 고객은 최근 90일 미구매로 정의했습니다.

<img width="599" height="376" alt="image" src="https://github.com/user-attachments/assets/7b5e1edf-1fe7-4a02-a751-4726a7dab69d" />



