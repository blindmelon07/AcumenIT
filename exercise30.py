#csv
import csv

with open('voting.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Candidate", "Positions", "Votes"])
    writer.writerow(["CHAIRMAN", "President", "100"] )
    writer.writerow(["CHAIRMAN", "BOD ", "1" * 66])
    writer.writerow(["LEONY", "BOD", "1000" * 10] )
    writer.writerow(["EMERSON", "ELCOM", "80"] * 20)

  