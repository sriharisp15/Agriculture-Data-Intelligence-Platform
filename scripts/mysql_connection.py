import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Srihari1557",
        database="agriculture_db"
    )

    if connection.is_connected():
        print("✅ Connected to MySQL Successfully!")

except mysql.connector.Error as e:
    print("❌ Error:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔒 Connection Closed.")