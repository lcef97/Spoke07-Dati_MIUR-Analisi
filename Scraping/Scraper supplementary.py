from selenium import webdriver


# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Replace 'Your Search Key' with the actual search key
search_key = "CEEE85404L"

# Construct the search results URL
search_url = f"https://cercalatuascuola.istruzione.it/cercalatuascuola/ricerca/risultati?rapida={search_key}&tipoRicerca=RAPIDA&gidf=1"

# Navigate to the search results page
driver.get(search_url)

# Optionally, interact with the search results or perform further actions
# ...

# Close the browser
#driver.quit()

# Replace 'search_keys' with your array of search keys
#search_keys = ["AGIS01700D", "AGTF02601R", "ANEE80501A", "APRI02000Q", "AVIC81800B", "BATD21000D", "BATD21050V", "BGRH020009", "BIPS00401B", "BNCT72300G ", "BSPS03000P",
#"CARA004014 ", "CBAA84602E ", "CBEE84602Q ", "CBIS002003 ", "CEAA86606Q ", "CLCT70300L ", "CLIC807003 ", "CNMM826047 ", "CRAA80603L ", "CRAA81203X ", "CRIC80200A",
#"CRIS00200E ", "CRTA00201A ", "CSIC85300P ", "CTIS001009 ", "CTIS00400R ", "CTIS01200Q ", "CTIS016003 ", "CTIS024002 ", "CTIS04200G ", "CTIS044007 ", "CTRH010007",
#"CTRH05000N ", "CTSL01000A ", "CZTA021035 ", "ENIC81800T ", "ENMM82801D ", "FGAA81805A ", "FGPM00701E ", "FICT70100D ", "FICT704001 ", "FRIC81200B ", "GEEE820055",
#"GEIC866008 ", "GEIS017007 ", "GOIC81100L ", "GOMM04000N ", "IMAA800012 ", "IMMM800016 ", "ISEE81508D ", "LECT708002 ", "LERH05101Q ", "LETD048023 ", "LETF01601R",
#"MBPM08000Q ", "MIAA84001P ", "MNIC80000X ", "MNTD008011 ", "MOIS011007 ", "NAAA8AS028 ", "NAIS04600E ", "NAIS06200C ", "NAMM8GL01Q ", "NAPC22000A ", "NAPS02000Q",
#"NARH07000E ", "NOEE80701R ", "NOEE80703V ", "NOEE80704X ", "PAIC817007 ", "PDPM001015 ", "POSD003019 ", "PVEE823065 ", "PZIC822004 ", "RCIC82100T ", "RGTD03002X",
#"RMEE8AJ035 ", "RMMM8AF01E ", "RMPC29000G ", "RMTD19000N ", "SAIC8BM00X ", "SRIS00700C ", "SRIS011004 ", "SRMM07100L ", "SSTD01701R ", "TOIC8AP00R ", "TOMM32500B",
#"TRMM816026 ", "TVIS00800E ", "TVIS01100A ", "TVRH01000N ", "UDEE85407R ", "VARC030007 ", "VBTN006017 ", "VEMM87101V ", "VIIC834006 ", "VRRI01000R"]





# Loop through the search keys and automate the search
#for key in search_keys:
#    search_input = driver.find_element_by_id("rapida")  # Change the selector as needed
#    search_input.clear()  # Clear the input field
#    search_input.send_keys(key)  # Enter the search key
#    search_input.send_keys(Keys.RETURN)  # Submit the form by pressing Enter

    # You can add additional code to interact with the results as needed

# Close the browser when done
#driver.quit()
