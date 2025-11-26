chai_type = 'Ginger Type'
customer_name = 'Cust1'

chai_description = 'Aromatic and Bold'
print(f'Frist Word: {chai_description[0:8]}')
print(f'Last Word: {chai_description[12:]}')
print(f'Reverse String: {chai_description[::-1]}')

label_text = 'Chai Special'
encoded_label = label_text.encode('utf-8')
print(f'Non Encoded Label: {label_text}')
print(f'Encoded Label: {encoded_label}')
decoded_label = encoded_label.decode('utf-8')
print(f'Decoded Label: {decoded_label}')