--- What is this ---

This is a simple Python application (hosted in Docker containers) that, given a csv text file with student data and a csv with teacher data, generates a JSON file reporting each student, the teacher assigned to each student, and the unique class ID for the class each student is scheduled for.

--- How to use this application --

To use this application locally, do the following:
-- clone/download the github repository into the directory of your choosing.
-- open powershell (may have to run as administrator as this application contains write operations to files)
-- navigate to the directory where you cloned/downloaded
-- run the following command "python /app/main.py" without the quotations

To use this application in Docker, do the following:
-- In Docker desktop, create a new dev environment by clicking on Dev Environments (left sidebar) and then create
-- In the "Enter the Git Repository" window, paste the following address https://github.com/tkbd94/class-assignments.git
-- Wait for the clone to finish
-- In powershell, run the following command "docker build -t class-assignments ." (no quotations)
-- When that command finishes, add the following command and execute as well "docker run class-assignments" (no quotations)

--- Testing ---
-- To test this application, use the test_findassignments.py file as such "python test_findassignments.py" (no quotations)

--- Future development and improvements ---
-- There is room for potential improvement, most obviously regarding user-input for the given student and teacher files (already exists but has been commented out) in addition to accomodating different delimiter types

--- Dependencies ---
-- You will need Python to run this application locally, and Docker to run it in a Docker container
--- Docker comes with its own set of preconditions if you wish to install
--- Docker runs on Windows, Mac, and Linux systems, though the installation varies depending on the operating system