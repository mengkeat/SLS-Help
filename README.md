# SLS-Help
Simple utilities for MOE SLS for my own use

I currently have no intention to support this for others or making this generic as this is my own 
quick and dirty approach to automate some of the work to upload my kid's homework to MOE's website 
over SLS. I probably have to do this everyday for my kid during the circuit breaker ("Soft lockdown") 
in Singapore. Hence at least automate some of the pain points away.

Phone Camera Shot Aggregation
-----------------------------
SLS currently is not allowing upload of multiple phone camera shots. Python images2PDF.py
packages all these images to a single pdf.

- Tkinter interface to choose which set of jpegs or which zip files (which contains the jpegs)
- My workflow consists of my wife taking the snapshot and then sending it by phone over to me in 
    a ZIP file. 
