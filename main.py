from handlers.datahandlers import PandasHandler

pdh = PandasHandler()

# test_a = dt.get_dataset('/home/adam/Documentos/teste.docx')
# test_b = pdh.get_dataset('/home/adam/nerdstore.pdf')
test_c = pdh.get_dataset('/home/adam/Documentos/data_science/thrid_party_datasets/ubs_construcaonone.csv')
deputies_presences_df = pdh.get_dataset('/home/adam/Documentos/data_science/thrid_party_datasets/chamber_of_deputies_presences.csv')
# print(test_a)
# print(test_b)
print(test_c.keys())