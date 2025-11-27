from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any

import os
import ibm_db
import ibm_db_dbi as dbi
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

# =====================
# DB2 CONFIG
# =====================

# You can keep hardcoded values or read from env
DB2_HOST = os.getenv("DB2_HOST")
DB2_PORT = os.getenv("DB2_PORT")
DB2_USERNAME = os.getenv("DB2_USERNAME")
DB2_PASSWORD = os.getenv("DB2_PASSWORD")

DB2_DSN = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
            'BLUDB',
            DB2_HOST,   
            DB2_PORT,         
            uid=DB2_USERNAME,     
            pwd=DB2_PASSWORD     
        )


def db2_init(query: str):
    """
    Run a SELECT query on DB2 and return rows as list of dicts.
    Same DSN as your working script.
    """
    try:
        conn = dbi.connect(DB2_DSN)
        df = pd.read_sql_query(query, con=conn)
        conn.close()
        # Return Python objects; FastAPI will JSON-encode them
        return df.to_dict(orient="records")
    except Exception as e:
        # Let caller handle/log
        raise e


# =====================
# FASTAPI APP
# =====================

app = FastAPI(title="DB2 Customer API")


# (optional) enable CORS if you call this from browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


# =====================
# Customer
# =====================

@app.get("/customer")
def run_query():
    """
    Hit: GET /query
    Returns all rows from TSF84071.CUSTOMERDATA (like your example).
    """
    try:
        data = db2_init("SELECT * FROM TSF84071.CUSTOMERDATA FETCH FIRST 1 ROW ONLY;")
        return {
            "count": len(data),
            "data": data,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB2 query failed: {e}")


@app.get("/customerkind")
def run_query():
    """
    Hit: GET /query
    Returns all rows from TSF84071.CUSTOMERDATA (like your example).
    """
    try:
        data = db2_init("SELECT DISTINCT CUSTOMER_NAME, CUSTOMER_MARRIAGE_STATUS, TRANSACTION_TYPE, HAS_EXISTING_LOAN, LOAN_PRODUCT_INTEREST_LEVEL, CUSTOMER_SEGMENT AS KIND FROM TSF84071.CUSTOMERDATA;")
        return {
            "count": len(data),
            "data": data,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB2 query failed: {e}")


# =====================
# Fundsheet
# =====================
@app.get("/fundsheet")
def run_query():
    """
    Hit: GET /query
    Returns all rows from TSF84071.FUNDSHEET (like your example).
    """
    try:
        data = db2_init("SELECT * FROM TSF84071.FUNDSHEET FETCH FIRST 1 ROW ONLY;")
        return {
            "count": len(data),
            "data": data,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB2 query failed: {e}")

@app.get("/fundsheetkind")
def run_query():
    """
    Hit: GET /query
    Returns all rows from TSF84071.FUNDSHEET (like your example).
    """
    try:
        data = db2_init("SELECT DISTINCT REKSADANA, JENIS_DANA, KLASIFIKASI_RISIKO AS KIND FROM TSF84071.FUNDSHEET;")
        return {
            "count": len(data),
            "data": data,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB2 query failed: {e}")


# =====================
# query
# =====================
@app.post("/query")
def run_query(body: QueryRequest):
    """
    Generic endpoint if you want to run a custom SELECT query.
    Use carefully (don't expose to public without restrictions).
    """
    try:
        data = db2_init(body.query)
        return {
            "count": len(data),
            "data": data,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB2 query failed: {e}")