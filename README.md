FCC ULS Callsign search
=======================
Python scripts to download a local copy of the [FCC Universal Licensing System](https://www.fcc.gov/wireless/systems-utilities/universal-licensing-system) and run searches against the local copy.  fcc_uls_callsign_search.py will download a copy of the [ULS](https://www.fcc.gov/wireless/systems-utilities/universal-licensing-system) and overwrite it if the zip is more than a week old.

I wrote this script to monitor vanity callsigns I am interested in.


Assumptions
----------------------
* You have an internet connection.
* You have python installed.



Quick Start
----------------------

``` 
    python .\fcc_uls_callsign_search.py

    ULS Zip file not found.
    Downloading Zip
    Download complete
    Unzipping file
    Unzipping complete
    Ingesting dat files
    Ingesting dat files complete
    FCC ULS Callsign Search
     0: Exit
     1: Search for Callsign
     2: Process callsign_input.txt

    Option:

```
Example Output
----------------------
```
Callsign: W4NTS
==================
Group: C, Available To: Technician, Tech Plus. & General Class

Amateur:
------------------
Operator Class: E,Previous Callsign: , Entity:Tate, Harold L
Operator Class: T,Previous Callsign: KO4IBG, Entity:Henson, Jacob B

History:
------------------
Date: 10/24/2020, FRN: 0030015242, Entity: Henson, Jacob B, License Issued(LIISS )
Date: 10/24/2020, FRN: 0030015242, Entity: Henson, Jacob B, None(VANGRT)
Date: 05/25/2016, FRN: 0004436366, Entity: Tate, Harold L, License Status Set to Expired(LIEXP )


Callsign: K1SSY
==================
Group: C, Available To: Technician, Tech Plus. & General Class

History: None, K1SSY Probably Available

```

Use Option 2 to run a search for each callsign in [callsign_input.txt](callsign_input.txt)

License
----------------------
MIT License

Author
----------------------
Jacob Henson (W4NTS)