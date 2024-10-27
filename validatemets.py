from lxml import etree

mets_file = 'microcenterdata_mets.xml'
#mets_file = 'books_mets.xml'
with open(mets_file, 'rb') as file:
    mets_doc = etree.parse(file)

schema_file = '../mets.xsd'
with open(schema_file, 'rb') as schema:
    mets_schema = etree.XMLSchema(etree.parse(schema))

if mets_schema.validate(mets_doc):
    print("The METS XML file is compliant with the METS schema.")
else:
    print("The METS XML file is NOT compliant with the METS schema.")
    for error in mets_schema.error_log:
        print(error)