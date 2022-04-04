#!/usr/bin/env python3
import helpers

def main():
    assignments = helpers.findAssignments(helpers.getStudents(), helpers.getTeachers())
    helpers.writeToJSON(assignments)

if __name__ == '__main__':
    main()