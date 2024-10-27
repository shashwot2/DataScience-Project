import pandas as pd
import json
from lxml import etree

file_path = 'books_raw.csv'
df = pd.read_csv(file_path)

df['parsed_data'] = df['raw_data'].apply(json.loads)

def extract_metadata(record):
    metadata = {
        'title': record.get('volumeInfo', {}).get('title', 'N/A'),
        'authors': ', '.join(record.get('volumeInfo', {}).get('authors', [])),
        'publishedDate': record.get('volumeInfo', {}).get('publishedDate', 'N/A'),
        'identifier': record.get('id', 'N/A'),
        'category': ', '.join(record.get('volumeInfo', {}).get('categories', [])),
    }
    return metadata

extracted_metadata = pd.DataFrame(df['parsed_data'].apply(extract_metadata).tolist())

mets = etree.Element("mets", nsmap={
    None: "http://www.loc.gov/METS/",
    "xlink": "http://www.w3.org/1999/xlink",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dnx": "http://www.exlibrisgroup.com/dps/dnx"
})
mets.attrib['ID'] = 'BooksDataPackage'
mets.attrib['OBJID'] = 'BooksData'
mets.attrib['TYPE'] = 'Archival Information Package (AIP)'

metsHdr = etree.SubElement(mets, "metsHdr", CREATEDATE="2024-10-27T12:00:00", RECORDSTATUS="Complete")
agent = etree.SubElement(metsHdr, "agent", ROLE="CREATOR", TYPE="INDIVIDUAL")
etree.SubElement(agent, "name").text = "Shashwot K C"

dmdSec = etree.SubElement(mets, "dmdSec", ID="DMD1")
mdWrap = etree.SubElement(dmdSec, "mdWrap", MDTYPE="DC")
xmlData = etree.SubElement(mdWrap, "xmlData")

for index, row in extracted_metadata.iterrows():
    dc_record = etree.SubElement(xmlData, "{http://purl.org/dc/elements/1.1/}record")
    etree.SubElement(dc_record, "{http://purl.org/dc/elements/1.1/}title").text = row['title']
    etree.SubElement(dc_record, "{http://purl.org/dc/elements/1.1/}creator").text = row['authors']
    etree.SubElement(dc_record, "{http://purl.org/dc/elements/1.1/}date").text = row['publishedDate']
    etree.SubElement(dc_record, "{http://purl.org/dc/elements/1.1/}identifier").text = row['identifier']
    etree.SubElement(dc_record, "{http://purl.org/dc/elements/1.1/}subject").text = row['category']

output_file = 'books_mets.xml'
tree = etree.ElementTree(mets)
tree.write(output_file, pretty_print=True, xml_declaration=True, encoding="UTF-8")

print(f"METS XML file saved to {output_file}")
