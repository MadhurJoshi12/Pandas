#### **1️⃣ Reading \& Writing Data**



Load a CSV file students.csv containing columns Name, Age, Score. Print the first 5 rows.



Save the first 10 rows of this DataFrame to a new CSV file called top\_students.csv.



Load an Excel file data.xlsx and print all sheet names.



#### **2️⃣ Selection \& Indexing**



From the DataFrame df, select the Name and Score columns only.



Select rows where Age > 25.



Using .loc\[], select the Score of the student whose Name is "Raj".



Using .iloc\[], select the last 3 rows of the DataFrame.



#### **3️⃣ Filtering \& Conditional Selection**



Filter all rows where Score is between 80 and 90.



Find all students whose names start with "A" using regex.



Replace all scores less than 50 with 50 using replace().



#### **4️⃣ Missing Data Handling**



Count how many missing values (NaN) are present in each column.



Drop all rows that have at least one NaN.



Fill missing Age values with the median age.



Forward-fill missing values in the Score column.



Interpolate missing Score values using linear interpolation.



#### **5️⃣ Aggregation \& Statistics**



Find the mean, median, and standard deviation of the Score column.



Find the maximum and minimum age.



Group the data by Age and find the average score for each age.



#### **6️⃣ String \& Regex Operations**



In the Name column, replace all occurrences of "Raj" with "Rahul".



Remove all non-alphabet characters from the Name column using regex.



Extract the first 3 letters of each name into a new column called ShortName.



#### **7️⃣ Advanced / Optional**



Using polynomial interpolation, fill missing Score values (ensure SciPy is installed).



For a column of messy phone numbers, remove all non-digit characters using regex.



Split a column "Address" with format "City | State" into two separate columns.

