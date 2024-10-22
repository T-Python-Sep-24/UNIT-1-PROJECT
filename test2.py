# import pandas as pd
# from Products import Products

# def extractedProducts(row):
#     return Products(row['Name'], row['price'], row['quantity'])

# productsData = pd.read_excel('Products.xlsx')

# extractedRows = productsData.apply(extractedProducts, axis=1).tolist()

# print(f'{"Id":<5} {"Name":<25} {"Product Id":<12} {"Price":<10} {"Stock Qty":<12}')
# for i, product in enumerate(extractedRows, start=1):
#     print(f'{i:<5}', end='')
#     product.display()
