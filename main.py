import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'SITEID': int(row['SITEID']),
                'COUNTRYID': row['COUNTRYID'],
                'SCRNNUM': int(row['SCRNNUM']),
                'ENROLNUM': int(row['ENROLNUM'])
            })
    return data

def main():
    file_path = 'data/site_data.csv'
    data = read_csv_file(file_path)

    total_screened = sum(row['SCRNNUM'] for row in data)
    total_enrolled = sum(row['ENROLNUM'] for row in data)

    print(f"Total Subjects Screened: {total_screened}")
    print(f"Total Subjects Enrolled: {total_enrolled}")

if __name__ == "__main__":
    main()