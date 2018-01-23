import csv

def main():
    with open('MyGrade.csv', encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        first_row = next(readCSV)
        credit_sum = 0
        score_sum = 0

        for row in readCSV:
            if(row[0] == ""):
                continue
            credit_sum += int(row[1])
            score_sum += tranform_grade_to_number(row[2]) * int(row[1])

        print("all credit : ",credit_sum)
        print("all score : ",score_sum)
        print("GPAX : ", (int(score_sum*100/credit_sum)/100))

def tranform_grade_to_number(grade):
    return {
        "A": 4,
        "B+": 3.5,
        "B": 3,
        "C+": 2.5,
        "C": 2,
        "D+": 1.5,
        "D": 1,
        "F": 0,
    }.get(grade, 0)

main()
