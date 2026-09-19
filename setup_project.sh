#!/bin/bash
# Setup script for Grade System Project

#exit on error
set e-

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

pip install -e .

python -c "import grade_system; print('Grade System package installed successfully')"

# Run tests
pytest tests/

#verify new commands
echo "Testing new CLI commands..."
grade-system add-student TestStudent 90,85
grade-system update-student TestStudent 95,90
grade-system add-course Math "Alice:90, Bob:85"
grade-system delete-course Math
grade-system export-summary summary.txt

echo "Project setup complete. Run "source venv/bin/activate' to activate the virtual environment."

