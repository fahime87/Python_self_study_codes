import pandas as pd

grad=[[18,16.5,14,17],[12,15,13,15],[19,20,18,17]]
data=pd.DataFrame(grad,index=["Ali","Moh","Reza"],columns=["pisic","shimi","math","adabiat"])
print(data)
excel_file=pd.ExcelWriter("Grade.xlsx",engine="xlsxwriter")
data.to_excel(excel_file)
excel_file._save()
