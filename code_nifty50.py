import csv
with open("Nifty 50 Historical Data.csv","r",newline="") as file1:
    with open("output_signals.csv","w",newline="") as file2:
        writer=csv.writer(file2)
        reader=csv.reader(file1)
        rows=list(reader)
        ans=False
        writer.writerow(["Date","Signal"])
        req_rows=[]
        for row in reversed(rows):
            if row[6]=='Change %':
                continue
            s=float(row[6].replace('%','').strip())
            if s>=0:
                if not ans:
                    req_rows.append([row[0],1])
                    ans=True
                else:
                    req_rows.append([row[0],0])
            else:
                if not ans:
                    req_rows.append([row[0],0])
                    ans=False
                else:
                    req_rows.append([row[0],-1])
                    ans=False
        for row in reversed(req_rows):
            writer.writerow(row)
            
            
