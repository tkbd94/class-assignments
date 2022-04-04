import json
import pandas as pd

#functions necessary for execution of run.py

def getStudents():
    ## Prompt user for file with student data. ##
    '''Takes in void; returns file object.'''
    #while True:
    #    f = input('Enter the name of the file: ')
    #    try:
    #        students = open(f, 'r').readlines()
    #    except FileNotFoundError:
    #        print('The file was not found -- please try again.')
    #    else:
    #        return f
    #studentsFile = r'D:\_doc\_coding\_python\SingleStoneExercise\app\students.csv'
    studentsFile = r'/app/students.csv'
    return studentsFile

def getTeachers():
    ## Prompt user for file with teacher data. ##
    '''Takes in void; returns file object.'''
    #while True:
    #    f = input('Enter the name of the file: ')
    #    try:
    #        teachers = open(f, 'r').readlines()
    #    except FileNotFoundError:
    #        print('The file was not found -- please try again.')
    #    else:
    #        return f
    #teachersFile = r'D:\_doc\_coding\_python\SingleStoneExercise\app\teachers.parquet'
    teachersFile = r'/app/teachers.parquet'
    return teachersFile

def findAssignments(studentsFile, teachersFile):
    ## Find student-teacher pairs and their class assignments. ##
    '''Takes in 2 file objects; returns returns list of dictionary objects.'''
    assignments = []
    studentsDF = pd.read_csv(studentsFile, delimiter='_', engine='pyarrow')
    teachersDF = pd.read_parquet(teachersFile, engine='pyarrow')

    for csvIndex, csvRow in studentsDF.iterrows():
        for parIndex, parRow in teachersDF.iterrows():
            if csvRow[6] == parRow[6]:
                schedule = {
                    'Student': csvRow[2] + ", " + csvRow[1],
                    'Teacher': parRow[2] + ", " + parRow[1],
                    'Class': parRow[6]
                }
                assignments.append(schedule)
    return assignments

def writeToJSON(output):
    ## Write student-teacher pairs and their class assignments to a JSON file. ##
    '''Takes in list of dictionary objects; writes list to external JSON file; returns void.'''
    jOut = json.dumps(output)
    with open('output.json', 'w') as f:
        f.write(jOut)
        f.close()