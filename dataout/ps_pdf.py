import subprocess
import os
from glob import glob

path_in = os.getcwd()

files = glob(f"{path_in}/mode_teste_*A.ps")

for file in files:
    file_out = file.split("/")[-1].replace(".ps", "")
    # Convert PS to PNG using Ghostscript
    #cmd = [
    #    "gs",
    #    "-dSAFER",
    #    "-dBATCH",
    #    "-dNOPAUSE",
    #    "-dFirstPage=1",
    #    "-dLastPage=5",
    #    "-sDEVICE=pngalpha",
    #    "-r300",
    #    f"-sOutputFile={file_out}.png",
    #    f"{file}"
    #]

    cmd = [
        "gs",
        "-dSAFER",
        "-dBATCH",
        "-dNOPAUSE",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-sOutputFile={file_out}.pdf",
        file
    ]

    subprocess.run(cmd, check=True)
