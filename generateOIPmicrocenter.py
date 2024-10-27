import pandas as pd
from lxml import etree

file_path = 'microcenterdata.csv'
df = pd.read_csv(file_path)

mets = etree.Element("mets", nsmap={
    None: "http://www.loc.gov/METS/",
    "xlink": "http://www.w3.org/1999/xlink",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dnx": "http://www.exlibrisgroup.com/dps/dnx"
})
mets.attrib['ID'] = 'MicrocenterDataPackage'
mets.attrib['OBJID'] = 'MicrocenterData'
mets.attrib['TYPE'] = 'Archival Information Package (AIP)'

dmdSec = etree.SubElement(mets, "dmdSec", ID="DMD1")
mdWrap = etree.SubElement(dmdSec, "mdWrap", MDTYPE="DC")
xmlData = etree.SubElement(mdWrap, "xmlData")

for _, row in df.iterrows():
    dc_record = etree.SubElement(xmlData, "{http://purl.org/dc/elements/1.1/}record")
    etree.SubElement(dc_record, "{http://purl.org/dc/elements/1.1/}title").text = row['Name']
    etree.SubElement(dc_record, "{http://purl.org/dc/elements/1.1/}identifier").text = row['Part ID'] if pd.notna(row['Part ID']) else "N/A"
    etree.SubElement(dc_record, "{http://purl.org/dc/elements/1.1/}date").text = row['Time']
    etree.SubElement(dc_record, "{http://purl.org/dc/elements/1.1/}description").text = f"Category: {row['Category']}"

amdSec = etree.SubElement(mets, "amdSec", ID="AMD1")
techMD = etree.SubElement(amdSec, "techMD", ID="TMD1")
mdWrap = etree.SubElement(techMD, "mdWrap", MDTYPE="DNX")
xmlData = etree.SubElement(mdWrap, "xmlData")

for index, row in df.iterrows():
    dnx_record = etree.SubElement(xmlData, "{http://www.exlibrisgroup.com/dps/dnx}record")
    etree.SubElement(dnx_record, "{http://www.exlibrisgroup.com/dps/dnx}FileSize").text = "N/A"
    etree.SubElement(dnx_record, "{http://www.exlibrisgroup.com/dps/dnx}FileFormat").text = "N/A"
    etree.SubElement(dnx_record, "{http://www.exlibrisgroup.com/dps/dnx}MIMEType").text = "N/A"
    etree.SubElement(dnx_record, "{http://www.exlibrisgroup.com/dps/dnx}ProducerAgent").text = "Microcenter"

structMap = etree.SubElement(mets, "structMap", TYPE="logical")
div = etree.SubElement(structMap, "div", TYPE="bundle")

for index, row in df.iterrows():
    item = etree.SubElement(div, "div", TYPE="item")
    etree.SubElement(item, "{http://www.loc.gov/METS/}label").text = row['Name']
    etree.SubElement(item, "{http://www.loc.gov/METS/}id").text = row['Part ID'] if pd.notna(row['Part ID']) else "N/A"

fileSec = etree.SubElement(mets, "fileSec")
fileGrp = etree.SubElement(fileSec, "fileGrp", USE="View")

for index, row in df.iterrows():
    file_id = f"FILE{index+1}"
    file_element = etree.SubElement(fileGrp, "file", ID=file_id, MIMETYPE="N/A")
    fLocat = etree.SubElement(file_element, "FLocat", LOCTYPE="URL")
    fLocat.attrib["{http://www.w3.org/1999/xlink}href"] = row['Link']

output_file = 'microcenterdata_mets.xml'
tree = etree.ElementTree(mets)
tree.write(output_file, pretty_print=True, xml_declaration=True, encoding="UTF-8")

print(f"METS XML file saved to {output_file}")
