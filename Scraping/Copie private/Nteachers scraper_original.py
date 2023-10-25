from bs4 import BeautifulSoup
import requests
import pandas as pd
import pyarrow.feather as feather
import numpy
import time

df = feather.read_table("G:/Il mio Drive/Spoke 0/R/Dati MIUR/Url_personale.feather").to_pandas()

trydf = df.iloc[0:199, :]

# Loop through the URLs in your DataFrame


matrix = numpy.hstack(["CODICE_SCUOLA"] + ["M_Docenti", "F_Docenti", "Tot_Docenti", "M_Supplenti", "F_Supplenti", "Tot_Supplenti", "M_ATA", "F_ATA", "Tot_ATA"])
print("start")
starttime = time.time()

for url in df['link']:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table')

        if table:
            row_names = []
            column_names = []
            values = []

            for row in table.find_all('tr'):
                cells = row.find_all('td')
                if len(cells) >= 4:  
                    row_names.append(cells[0].get_text().strip())
                    column_names.append(cells[1]['data-col-2'].strip())
                    values.append(cells[1].get_text().strip())

                    row_names.append(cells[0].get_text().strip())
                    column_names.append(cells[2]['data-col-3'].strip())
                    values.append(cells[2].get_text().strip())

                    row_names.append(cells[0].get_text().strip())
                    column_names.append(cells[3]['data-col-4'].strip())
                    values.append(cells[3].get_text().strip())
      
        if len(column_names) != 9 or len(row_names) != 9 or len(values) != 9 :
            print("Wrong dimensions")
            print(df.iloc[(df['link'] == url).astype(int).idxmax(), 0])
            print(str(len(row_names)) + "x" + str(len(column_names)) + " and " + str(len(values)) + " values" )
           
        idnew = df.iloc[(df['link'] == url).astype(int).idxmax(), 0]
        values = [int(x) if x != 'n.d.' else 0 for x in values]
        rownew = numpy.hstack([idnew] + [values])
        rownew = [rownew[0]] + [int(x) for x in rownew[1:]]
         
        matrix = numpy.vstack([matrix, rownew])

         
    else:
        print(f"Failed to fetch {url}")
    
    if (df['link'] == url).astype(int).idxmax()%20 == 0:
        print("reached  " + str((df['link'] == url).astype(int).idxmax() ) )
        
        endtime = time.time()
        difftime = endtime - starttime
        print(f"Elapsed time: needed {difftime} seconds")
        starttime = time.time()
   


pddf = pd.DataFrame(matrix)
pddf.to_csv('G:/Il mio Drive/Spoke 0/R/Dati MIUR/Analisi/excel/nTeachers.csv', index=False, header=False)

