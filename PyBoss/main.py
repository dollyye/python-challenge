import os
import csv
from datetime import datetime

fileNum = ['1', '2']

employeeID = []
firstname = []
lastname = []
birthdate = []
ssn = []
state = []

stateDict = {'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY'}

for n in fileNum:
    employeeCSV = os.path.join('employee_data' + n + '.csv')
    newEmployeeCSV = os.path.join('employee_formatted' + n + '.csv')
    
    with open(employeeCSV,'r') as f_in, open(newEmployeeCSV, 'w', newline="") as f_out:
        d_reader = csv.reader(f_in, delimiter=',')
        
        next(d_reader, None)
        
        for row in d_reader:
            employeeID.append(row[0])

            full_name = row[1].split()
            firstname.append(full_name[0])
            lastname.append(full_name[1])
            
            birthdate_input = datetime.strptime(str(row[2]),'%Y-%m-%d')
            birthdate_formatted = datetime.strftime(birthdate_input,'%m/%d/%Y')
            birthdate.append(birthdate_formatted)

            ssn_split = row[3].split('-')
            ssn_formatted = ('***-**-'+ssn_split[2])
            ssn.append(ssn_formatted)
            
            state.append(stateDict[row[4]])
        
        new_data = zip(employeeID,firstname,lastname,birthdate,ssn,state)
        
        d_writer = csv.writer(f_out, delimiter=',')

        d_writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
        
        d_writer.writerows(new_data)
