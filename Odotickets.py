import mysql.connector
import pandas as pd

user = input('Enter MySQL username: ')
password = input('Enter MySQL password: ')
host = input('Enter MySQL host: ')
start_date = input('Enter start date (YYYY-MM-DD): ')
end_date = input('Enter end date (YYYY-MM-DD): ')
brand_id = input('Enter brand id: ')


# Connect to the MySQL server
cnx = mysql.connector.connect(user=user, password=password,
                              host=host, database='Odo')
print("MySQL Database Connection established")

# Create a cursor object
cursor = cnx.cursor()

# Query to select all records from the 'SupportTicket' table
query = f"""SELECT TicketID, 
                   TRIM(SUBSTRING_INDEX(TicketDescription, ' - ', 1)) AS TicketSubject, #split the TicketDescription column to subject and email
                   TRIM(SUBSTRING_INDEX(TicketDescription, ' - ', -1)) AS EmailAddress, 
                   TicketStatus, 
                   TurnAroundTime/216000 AS TurnAroundTimeHours, 
                   CreatedByEmployeeID, 
                   CreationDateTimeID, 
                   ClosedDateTimeID, 
                   TicketPriority, 
                   GlobalRegion, 
                   LastModifiedDateTimeID, 
                   ClientCountry, 
                   SpecialtyName 
            FROM Odo.SupportTicket 
            WHERE CreationDateTimeID BETWEEN '{start_date}' AND '{end_date}' 
                  AND BrandID = '{brand_id}' 
            ORDER BY CreationDateTimeID ASC"""

# Execute the query
cursor.execute(query)

# Fetch all records and store them in a list of tuples
result = cursor.fetchall()

# Convert the list of tuples to a Pandas DataFrame
df = pd.DataFrame(result, columns=cursor.column_names)

# Save the DataFrame to a CSV file
df.to_csv('Ticketdata.csv', index=False)

# Close the cursor and connection
cursor.close()
cnx.close()
