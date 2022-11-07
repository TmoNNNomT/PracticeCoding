import random
import openpyxl

ques_file_path = "C:/Users/arksh/Documents/QuestionsCP.xlsx"
wb = openpyxl.load_workbook(ques_file_path)
ws = wb['Sheet1']

links = []
ques_link_col = 2

for i in range(2, 127):
    links.append(ws.cell(row=i, column=ques_link_col).hyperlink.target)

n = random.randint(0, len(links) - 1)
print(links[n])

