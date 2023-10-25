from bs4 import BeautifulSoup
import requests
import pandas as pd
import pyarrow.feather as feather
import numpy

df = feather.read_table("G:/Il mio Drive/Spoke 0/R/Dati MIUR/Url_personale.feather").to_pandas()

trydf = df.iloc[0:99, :]

# Loop through the URLs in your DataFrame


matrix = numpy.hstack(["Dummy_row"] + [0, 0, 0, 0, 0, 0, 0, 0, 0])
matrix = [matrix[0]] + [int(x) for x in matrix[1:]]

for url in trydf['link']:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the first table (assuming it's the relevant one)
        table = soup.find('table')

        if table:
            # Initialize lists to store data
            row_names = []
            column_names = []
            values = []

            # Extract the data from the table
            for row in table.find_all('tr'):
                cells = row.find_all('td')
                if len(cells) >= 4:  # Ensure there are enough cells
                    row_names.append(cells[0].get_text().strip())
                    column_names.append(cells[1]['data-col-2'].strip())
                    values.append(cells[1].get_text().strip())

                    row_names.append(cells[0].get_text().strip())
                    column_names.append(cells[2]['data-col-3'].strip())
                    values.append(cells[2].get_text().strip())

                    row_names.append(cells[0].get_text().strip())
                    column_names.append(cells[3]['data-col-4'].strip())
                    values.append(cells[3].get_text().strip())

            # Now you have row_names, column_names, and values
      
        if len(column_names) == 9 and len(row_names) == 9 and len(values) == 9 :
            print("Regular dimensions for " + trydf.iloc[(trydf['link'] == url).astype(int).idxmax(), 0] )
        else:
            print("Wrong dimensions")
            print(trydf.iloc[(trydf['link'] == url).astype(int).idxmax(), 0])
            print(str(len(row_names)) + "x" + str(len(column_names)) + " and " + str(len(values)) + " values" )
           
        idnew = trydf.iloc[(trydf['link'] == url).astype(int).idxmax(), 0]
        rownew = numpy.hstack([idnew] + [values])
        rownew = [rownew[0]] + [int(x) for x in rownew[1:]]
         
        matrix = numpy.vstack([matrix, rownew])

         
    else:
        print(f"Failed to fetch {url}")






