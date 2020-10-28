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

```python 
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

Entity:
------------------
FRN: 0004436366, Name:Tate, Harold L, Southern Pines,NC
FRN: 0030015242, Name:Henson, Jacob B, Owens Crossroads,AL

History:
------------------
10/24/2020 LIISS , Henson, Jacob B
10/24/2020 VANGRT, Henson, Jacob B
05/25/2016 LIEXP , Tate, Harold L
```

Use Option 2 to run a search for each callsign in [callsign_input.txt](callsign_input.txt)

License
----------------------
MIT License

Author
----------------------
Jacob Henson (W4NTS)