import pandas as pd

file_path = "data/online_retail_II.csv"

df = pd.read_csv(file_path, encoding="latin1")

print(df.head())
print(df.info())
print(df.columns)

df.columns = df.columns.str.strip()


df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


print(df.isnull().sum())

df = df.dropna(subset=["Customer ID"])


df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]


df["Sales"] = df["Quantity"] * df["Price"]


df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)


print(df.head())
print(df.shape)
print(df[["InvoiceDate", "Quantity", "Price", "Sales", "YearMonth"]].head())

import matplotlib.pyplot as plt

#월별 매출 집계
monthly_sales = df.groupby("YearMonth")["Sales"].sum().reset_index()
print(monthly_sales.head())

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["YearMonth"], monthly_sales["Sales"])
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("YearMonth")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png")
plt.show()

#국가별 매출 상위 10개
country_sales = df.groupby("Country")["Sales"].sum().sort_values(ascending=False).head(10)
print(country_sales)

plt.figure(figsize=(10, 5))
country_sales.plot(kind="bar")
plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("outputs/country_sales.png")
plt.show()

#상품별 매출 상위 10개
product_sales = df.groupby("Description")["Sales"].sum().sort_values(ascending=False).head(10)
print(product_sales)

plt.figure(figsize=(10, 5))
product_sales.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("outputs/product_sales.png")
plt.show()



# -----------------------------
# 프로젝트 2: 재구매 / 휴면 고객 분석
# -----------------------------

# 기준 날짜 설정 (데이터 마지막 날짜 + 1일)
reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# 고객 기준 테이블 만들기
customer_df = df.groupby("Customer ID").agg({
    "InvoiceDate": [lambda x: (reference_date - x.max()).days, "min", "max"],
    "Invoice": "nunique",
    "Sales": "sum"
}).reset_index()


customer_df.columns = [
    "CustomerID",
    "Recency",
    "FirstPurchaseDate",
    "LastPurchaseDate",
    "Frequency",
    "Monetary"
]


print(customer_df.head())
print(customer_df.shape)

customer_df["IsRepurchase"] = customer_df["Frequency"].apply(lambda x: 1 if x > 1 else 0)

customer_df["IsDormant"] = customer_df["Recency"].apply(lambda x: 1 if x >= 90 else 0)

# 비율 확인
repurchase_rate = customer_df["IsRepurchase"].mean()
dormant_rate = customer_df["IsDormant"].mean()

print("Repurchase Rate:", repurchase_rate)
print("Dormant Rate:", dormant_rate)

# 구매 횟수 분포
freq_counts = customer_df["Frequency"].value_counts().sort_index().head(10)
print(freq_counts)

plt.figure(figsize=(10, 5))
freq_counts.plot(kind="bar")
plt.title("Purchase Frequency Distribution")
plt.xlabel("Number of Purchases")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("outputs/purchase_frequency.png")
plt.show()

# 재구매 고객 분포
repurchase_counts = customer_df["IsRepurchase"].value_counts()
print(repurchase_counts)

plt.figure(figsize=(6, 4))
repurchase_counts.plot(kind="bar")
plt.title("Repurchase Customer Distribution")
plt.xlabel("Is Repurchase")
plt.ylabel("Customer Count")
plt.tight_layout()
plt.savefig("outputs/repurchase_distribution.png")
plt.show()

#휴면 고객 분포
dormant_counts = customer_df["IsDormant"].value_counts()
print(dormant_counts)

plt.figure(figsize=(6, 4))
dormant_counts.plot(kind="bar")
plt.title("Dormant Customer Distribution")
plt.xlabel("Is Dormant")
plt.ylabel("Customer Count")
plt.tight_layout()
plt.savefig("outputs/dormant_distribution.png")
plt.show()


# -----------------------------
# 프로젝트 3: 가정 기반 채널 분석
# -----------------------------

import numpy as np

np.random.seed(42)

df = df.sort_values(["Customer ID", "InvoiceDate"])
df["OrderRank"] = df.groupby("Customer ID")["InvoiceDate"].rank(method="first")

def assign_channel(order_rank):
    if order_rank == 1:
        return np.random.choice(["Paid Search", "Social", "Direct"], p=[0.4, 0.3, 0.3])
    else:
        return np.random.choice(["Email", "Direct", "Social"], p=[0.5, 0.3, 0.2])

df["Channel"] = df["OrderRank"].apply(assign_channel)


print(df[["Customer ID", "InvoiceDate", "OrderRank", "Channel"]].head())

# 채널별 주문 수
channel_orders = df.groupby("Channel")["Invoice"].nunique().sort_values(ascending=False)
print(channel_orders)

plt.figure(figsize=(8, 5))
channel_orders.plot(kind="bar")
plt.title("Orders by Channel")
plt.xlabel("Channel")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("outputs/channel_orders.png")
plt.show()

# 채널별 매출
channel_sales = df.groupby("Channel")["Sales"].sum().sort_values(ascending=False)
print(channel_sales)

plt.figure(figsize=(8, 5))
channel_sales.plot(kind="bar")
plt.title("Sales by Channel")
plt.xlabel("Channel")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("outputs/channel_sales.png")
plt.show()

# 채널별 객단가(AOV)
channel_aov = (df.groupby("Channel")["Sales"].sum() / df.groupby("Channel")["Invoice"].nunique()).sort_values(ascending=False)
print(channel_aov)

plt.figure(figsize=(8, 5))
channel_aov.plot(kind="bar")
plt.title("AOV by Channel")
plt.xlabel("Channel")
plt.ylabel("Average Order Value")
plt.tight_layout()
plt.savefig("outputs/channel_aov.png")
plt.show()