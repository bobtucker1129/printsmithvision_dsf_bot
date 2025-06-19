import psycopg2
import os
from dotenv import load_dotenv
import streamlit as st  # ✅ ADD THIS

load_dotenv()


def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT", "5432")
        )
        return conn
    except Exception as e:
        st.error(f"Connection failed: {e}")  # ✅ Now works
        return None
