import pandas as pd
df = pd.read_csv('./../TEST.CSV', header=None)
df.columns = ['School', 'Enr_no', 'Enr_yr', 'Roll_no', 'Stream', 'Name', 'Sub1', 'Th1', 'Pr1', 'Sub2', 'Th2', 'Pr2', 'Sub3', 'Th3', 'Pr3', 'Sub4', 'Th4', 'Pr4', 'Sub5', 'Th5', 'Pr5', 'Sub6', 'Th6', 'Pr6', 'Sub7', 'Th7', 'Pr7']



# Function Optimization Required
df['Sub1'] = df['Sub1'].fillna(0.0).astype(int)
df['Sub2'] = df['Sub2'].fillna(0.0).astype(int)
df['Sub3'] = df['Sub3'].fillna(0.0).astype(int)
df['Sub4'] = df['Sub4'].fillna(0.0).astype(int)
df['Sub5'] = df['Sub5'].fillna(0.0).astype(int)
df['Sub6'] = df['Sub6'].fillna(0.0).astype(int)
df['Sub7'] = df['Sub7'].fillna(0.0).astype(int)

# Function Optimization Required
try:
    df['Th1'] = df['Th1'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Pr1'] = df['Pr1'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Th2'] = df['Th2'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Pr2'] = df['Pr2'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Th3'] = df['Th3'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Pr3'] = df['Pr3'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Th4'] = df['Th4'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Pr4'] = df['Pr4'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Th5'] = df['Th5'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Pr5'] = df['Pr5'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Th6'] = df['Th6'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Pr6'] = df['Pr6'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Th7'] = df['Th7'].fillna(0.0).astype(int)
except ValueError:
    pass

try:
    df['Pr7'] = df['Pr7'].fillna(0.0).astype(int)
except ValueError:
    pass


#Check Full Absents
absent_list = []
for index, row in df.iterrows():
    if row['Sub1']:
        if f"{row['Th1']}" == 'AB' and f"{row['Th2']}" == 'AB' and f"{row['Th3']}" == 'AB' and f"{row['Th4']}" == 'AB' and f"{row['Th5']}" == 'AB':
            absent_list.append(4)
        elif f"{row['Th1']}" == 'AB' or f"{row['Th2']}" == 'AB' or f"{row['Th3']}" == 'AB' or f"{row['Th4']}" == 'AB' or f"{row['Th5']}" == 'AB':
            absent_list.append(5)
        else:
            absent_list.append(0)
            
    else:
        if f"{row['Th6']}" == 'AB' and f"{row['Th2']}" == 'AB' and f"{row['Th3']}" == 'AB' and f"{row['Th4']}" == 'AB' and f"{row['Th5']}" == 'AB':
            absent_list.append(4)
        elif f"{row['Th6']}" == 'AB' or f"{row['Th2']}" == 'AB' or f"{row['Th3']}" == 'AB' or f"{row['Th4']}" == 'AB' or f"{row['Th5']}" == 'AB':
            absent_list.append(5)
        else:
            absent_list.append(0)
            
df['Absent_code'] = absent_list
    
# Generate report of these absentees

# Check Incomplete theory students
incomplete_list = []
import numpy as np
for index, row in df.iterrows():
    if row['Sub1']:
        if pd.isnull(row['Th1'] or row['Th2'] or row['Th3'] or row['Th4'] or row['Th5']):
            incomplete_list.append(1)
            continue
    if row['Sub6'] and not row['Th6']:
        incomplete_list.append(1)
        continue
    if row['Sub7'] and not row['Th7']:
        incomplete_list.append(1)
        continue
    
        
    incomplete_list.append(0)

df['Incomplete_code'] = incomplete_list

# Generate report of incomplete students

PASSING_THEORY_MARKS = {
	"01":"26",
	"02":"26",
	"03":"26",
	"04":"26",
	"05":"26",
	"06":"26",
	"11":"23",
	"12":"23",
	"13":"26",
	"14":"23",
	"15":"26",
	"16":"23",
	"17":"23",
	"18":"23",
	"19":"23",
	"20":"23",
	"21":"26",
	"22":"26",
	"23":"26",
	"24":"26",
	"25":"26",
	"26":"26",
	"27":"23",
	"28":"15",
	"29":"26",
	"30":"26"
}

PASSING_PRACT_MARKS = {
	"01":"7",
	"02":"7",
	"03":"7",
	"04":"7",
	"05":"7",
	"06":"7",
	"11":"10",
	"12":"10",
	"13":"7",
	"14":"10",
	"15":"7",
	"16":"10",
	"17":"10",
	"18":"10",
	"19":"10",
	"20":"10",
	"21":"7",
	"22":"7",
	"23":"7",
	"24":"7",
	"25":"7",
	"26":"7",
	"27":"10",
	"28":"18",
	"29":"7",
	"30":"7"
}

passed_list = []
for index, row in df.iterrows():
    if row['Sub1'] and row['Sub2'] and row['Sub3'] and row['Sub4'] and row['Sub5']:
        if pd.notnull(row['Th1']) and f"{row['Th1']}" != 'AB' and row['Th1'] >=  int(PASSING_THEORY_MARKS[str(row['Sub1']).zfill(2)]):
            if pd.notnull(row['Th2']) and f"{row['Th2']}" != 'AB' and row['Th2'] >=  int(PASSING_THEORY_MARKS[str(row['Sub2']).zfill(2)]):
                if pd.notnull(row['Th3']) and f"{row['Th3']}" != 'AB' and row['Th3'] >=  int(PASSING_THEORY_MARKS[str(row['Sub3']).zfill(2)]):
                    if pd.notnull(row['Th4']) and f"{row['Th4']}" != 'AB' and row['Th4'] >=  int(PASSING_THEORY_MARKS[str(row['Sub4']).zfill(2)]):
                        if pd.notnull(row['Th5']) and f"{row['Th5']}" != 'AB' and row['Th5'] >=  int(PASSING_THEORY_MARKS[str(row['Sub5']).zfill(2)]):
                            passed_list.append(1)
                            continue
            
    
    elif row['Sub6'] and row['Sub2'] and row['Sub3'] and row['Sub4'] and row['Sub5']:
        if pd.notnull(row['Th6']) and f"{row['Th6']}" != 'AB' and row['Th6'] >=  int(PASSING_THEORY_MARKS[str(row['Sub6']).zfill(2)]):
            if pd.notnull(row['Th2']) and f"{row['Th2']}" != 'AB' and row['Th2'] >=  int(PASSING_THEORY_MARKS[str(row['Sub2']).zfill(2)]):
                if pd.notnull(row['Th3']) and f"{row['Th3']}" != 'AB' and row['Th3'] >=  int(PASSING_THEORY_MARKS[str(row['Sub3']).zfill(2)]):
                    if pd.notnull(row['Th4']) and f"{row['Th4']}" != 'AB' and row['Th4'] >=  int(PASSING_THEORY_MARKS[str(row['Sub4']).zfill(2)]):
                        if pd.notnull(row['Th5']) and f"{row['Th5']}" != 'AB' and row['Th5'] >=  int(PASSING_THEORY_MARKS[str(row['Sub5']).zfill(2)]):
                            passed_list.append(1)
                            continue
    
    passed_list.append(0)
    
df['Raw_passed'] = passed_list

# Generate total based on raw results
x=1
while x < 8:
    total_sub_list = []
    for index, row in df.iterrows():
        if row['Raw_passed'] == 1:
            try:
                total_sub_list.append(row[f"Th{x}"] + int(row[f"Pr{x}"]))
            except ValueError:
                import numpy as np
                total_sub_list.append(np.nan)
        else:
            total_sub_list.append(np.nan)
        
    df[f"Totsub{x}"] = total_sub_list
    x+=1


# Subject wise performace of each student
sub_perf_dict = {}
for index, row in df.iterrows():
    x=1
    while x < 8:
        subject = row[f"Sub{x}"]
        if subject:
            if pd.notnull(row[f"Th{x}"]) and str(row[f"Th{x}"]) != 'AB' and row[f"Th{x}"] >=  int(PASSING_THEORY_MARKS[str(subject).zfill(2)]):
                if subject in sub_perf_dict.keys():
                    sub_perf_dict[subject] += 1
                else:
                    sub_perf_dict[subject] = 1
        x+=1

#Subject wise appearance of each subject
sub_app_dict = {}
for index, row in df.iterrows():
    x=1
    while x < 8:
        subject = row[f"Sub{x}"]
        if subject:
            if pd.notnull(row[f"Th{x}"]) and str(row[f"Th{x}"]) != 'AB':
                if subject in sub_app_dict.keys():
                    sub_app_dict[subject] += 1
                else:
                    sub_app_dict[subject] = 1
        x+=1

#Generate new data frame of passed and appeared students
df1 = pd.DataFrame(list(sub_perf_dict.items()))
df2 = pd.DataFrame(list(sub_app_dict.items()))
df3 = df2.merge(df1, on=0)
df3.columns = ['Subject', 'Appeared', 'Passed']

df3['Pass_percentage'] = (df3['Passed'] / df3['Appeared']) * 100

# Generate award for students not passed above
