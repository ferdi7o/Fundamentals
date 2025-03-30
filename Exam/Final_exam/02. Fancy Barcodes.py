import re

barcodes = int(input())

pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for _ in range(barcodes):
    barcod = input()
    match = re.findall(pattern, barcod)
    if match:
        for find in match:
            product_group = re.sub(r"\D", "", find)
            if product_group:
                print(f"Product group: {product_group}")
            else:
                print(f"Product group: 00")
    else:
        print("Invalid barcode")