import csv

f1 = file('domainsToAdd.csv', 'rU')
f2 = file('masterDomainList.csv', 'rU')
f3 = file('results.csv', 'w')

domainsToAdd = csv.reader(f1)
masterDomainList = csv.reader(f2)
c3 = csv.writer(f3)

masterlist = list(masterDomainList)

for domainsToAdd_row in domainsToAdd:
    row = 1
    found = False
    for masterDomain_row in masterlist:
        results_row = domainsToAdd_row
        if domainsToAdd_row[3].lower() == masterDomain_row[1].lower():
            results_row.append('[*] FOUND in master list (row ' + str(row) + ')')
            found = True
            break
        row = row + 1
    if not found:
        results_row.append('[!] NOT FOUND in master list')
    c3.writerow(results_row)

f1.close()
f2.close()
f3.close()