import streamlit as st
import mysql.connector

st.title("Hello from Streamlit + MySQL!")

try:
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        # host="localhost",
        user="testuser",
        password="testpass",
        database="testdb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db = cursor.fetchone()
    st.success(f"Connected to database: {db[0]}")
    cursor.close()
    conn.close()
except Exception as e:
    st.error(f"Failed to connect: {e}")
