import xlrd

wb = xlrd.open_workbook('sample.xlsx') #foo.xls

'''sh = wb.sheet_by_index(0)
for i in range(5):
    cell_value_class = sh.cell(i,2).value
    cell_value_id = sh.cell(i,0).value
'''
#print xlrd.dump(wb)
worksheet = wb.sheet_by_index(0)

# Change this depending on how many header rows are present
# Set to 0 if you want to include the header data.
offset = 0

rows = []
for i, row in enumerate(range(worksheet.nrows)):
    if i <= offset:  # (Optionally) skip headers
        continue
    r = []
    for j, col in enumerate(range(worksheet.ncols)):
        r.append(worksheet.cell_value(i, j))
    rows.append(r)

#print 'Got %d rows' % len(rows) - offset
print rows[0]  # Print column headings
print rows[offset]  # Print first data row sample
print rows[offset+1]  # Print first data row sample
