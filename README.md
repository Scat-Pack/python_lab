# pStudent Grade Management System

A python CLI application to manage student grades using OOP, abstract classes, and CSV storage.

## Setup

1. Clone the respitory from Github Classroom.
2. Run the setup script: "bash setup_project.sh"
3. Activate the virtual environment: 'Source venv/bin/activate
4.. Run the application: 'grade-system --help'

## Commands
- grade-system add-student <name> <grades>: Add a student with comma-seperated-grades
- grade-system add-course <name> <student_grades>: Add a course with name:grade pairs
- grade-system add-student <name> <grades>: Update grades for an existing student.
- grade-system delete-course <name>: Delete a course by name.
- grade-system view-all: View all students and courses.
- grade-system average <type> <name>: Calculate average grade for a student or course.
- grade-system export-summary <output_files>: Export a summary of all records to a file.


## Development
- Code in 'src/grade_system/'.
- Tests in 'tests/'.
- Run Tests: 'pytest tests/'.