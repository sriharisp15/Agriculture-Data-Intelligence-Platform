import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Srihari1557",
    database="agriculture_db"
)

cursor = connection.cursor()

queries = {

    "1. Total Records":
    """
    SELECT COUNT(*) AS Total_Records
    FROM agriculture;
    """,

    "2. Total States":
    """
    SELECT COUNT(DISTINCT State) AS Total_States
    FROM agriculture;
    """,

    "3. Total Crops":
    """
    SELECT COUNT(DISTINCT Crop) AS Total_Crops
    FROM agriculture;
    """,

    "4. Total Production":
    """
    SELECT SUM(Production) AS Total_Production
    FROM agriculture;
    """,

    "5. Total Area":
    """
    SELECT SUM(Area) AS Total_Area
    FROM agriculture;
    """,

    "6. Average Yield":
    """
    SELECT AVG(Yield) AS Average_Yield
    FROM agriculture;
    """,

    "7. Top 10 States by Production":
    """
    SELECT State,
           SUM(Production) AS Total_Production
    FROM agriculture
    GROUP BY State
    ORDER BY Total_Production DESC
    LIMIT 10;
    """,

    "8. Top 10 Crops by Production":
    """
    SELECT Crop,
           SUM(Production) AS Total_Production
    FROM agriculture
    GROUP BY Crop
    ORDER BY Total_Production DESC
    LIMIT 10;
    """,

    "9. Production by Year":
    """
    SELECT Crop_Year,
           SUM(Production) AS Total_Production
    FROM agriculture
    GROUP BY Crop_Year
    ORDER BY Crop_Year;
    """,

    "10. Production by Season":
    """
    SELECT Season,
           SUM(Production) AS Total_Production
    FROM agriculture
    GROUP BY Season
    ORDER BY Total_Production DESC;
    """,

    "11. Average Yield by State":
    """
    SELECT State,
           AVG(Yield) AS Average_Yield
    FROM agriculture
    GROUP BY State
    ORDER BY Average_Yield DESC
    LIMIT 10;
    """,

    "12. Average Yield by Crop":
    """
    SELECT Crop,
           AVG(Yield) AS Average_Yield
    FROM agriculture
    GROUP BY Crop
    ORDER BY Average_Yield DESC
    LIMIT 10;
    """,

    "13. Top 10 States by Area":
    """
    SELECT State,
           SUM(Area) AS Total_Area
    FROM agriculture
    GROUP BY State
    ORDER BY Total_Area DESC
    LIMIT 10;
    """,

    "14. Top 10 Crops by Area":
    """
    SELECT Crop,
           SUM(Area) AS Total_Area
    FROM agriculture
    GROUP BY Crop
    ORDER BY Total_Area DESC
    LIMIT 10;
    """,

    "15. State Wise Crop Count":
    """
    SELECT State,
           COUNT(DISTINCT Crop) AS Crop_Count
    FROM agriculture
    GROUP BY State
    ORDER BY Crop_Count DESC;
    """,

    "16. Highest Production Year":
    """
    SELECT Crop_Year,
           SUM(Production) AS Total_Production
    FROM agriculture
    GROUP BY Crop_Year
    ORDER BY Total_Production DESC
    LIMIT 1;
    """,

    "17. Top 5 Crops in Tamil Nadu":
    """
    SELECT Crop,
           SUM(Production) AS Total_Production
    FROM agriculture
    WHERE State='Tamil Nadu'
    GROUP BY Crop
    ORDER BY Total_Production DESC
    LIMIT 5;
    """,

    "18. Top 5 Crops in Kerala":
    """
    SELECT Crop,
           SUM(Production) AS Total_Production
    FROM agriculture
    WHERE State='Kerala'
    GROUP BY Crop
    ORDER BY Total_Production DESC
    LIMIT 5;
    """,

    "19. Rice Production Trend":
    """
    SELECT Crop_Year,
           SUM(Production) AS Rice_Production
    FROM agriculture
    WHERE Crop='Rice'
    GROUP BY Crop_Year
    ORDER BY Crop_Year;
    """,

    "20. Wheat Production Trend":
    """
    SELECT Crop_Year,
           SUM(Production) AS Wheat_Production
    FROM agriculture
    WHERE Crop='Wheat'
    GROUP BY Crop_Year
    ORDER BY Crop_Year;
    """
}

for title, query in queries.items():
    print("\n" + "="*70)
    print(title)
    print("="*70)

    df = pd.read_sql(query, connection)
    print(df)

connection.close()
print("\nDatabase Connection Closed.")