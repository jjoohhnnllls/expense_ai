import sqlite3
import pandas as pd
####################################################
#READ DATABASE
#CONVERT TO PANDAS DATAFRAME
#TO ANALYSE DATA
def load_expenses():
    conn = sqlite3.connect("database.db")
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df

####################################################
#CATEGORY SPENDING ANALYSIS
####################################################
def spending_by_category():
    df = load_expenses()

    if df.empty:
        return {}

    result = df.groupby("category")["amount"].sum()
    return result.to_dict()
####################################################
#USED GROUPEDBY AND AGGREGRATION FOR DATA ANALYSIS FOR CATEGORY SPENDING
####################################################

####################################################
#BASIC STATISTICS
def basic_stats():
    df = load_expenses()

    if df.empty:
        return {
            "total": 0,
            "average": 0,
            "max_category": "None"
        }

    total = df["amount"].sum()
    average = df["amount"].mean()

    max_category = (
        df.groupby("category")["amount"]
        .sum()
        .idxmax()
    )

    return {
        "total": round(total, 2),
        "average": round(average, 2),
        "max_category": max_category
    }

####################################################