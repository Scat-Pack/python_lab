import csv
import os
from .models import Student, Course

class GradeStorage:
    """Handles with CSV storage for grades."""
    def __init__(self, file_path: str = "grades.csv"):
        self.file_path = file_patth
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["type", "name", "grades", "student_grades"])
                writer.writerheader()


    def save(self,entity: "Gradeable"):
        """Save a gradeable entity to CSV."""
        with open(self.file_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["type", "name", "grades", "student_grades"])
                writer.writerow(entity.to_dict())

    def load_all(self):
        """Loads all entities from CSV"""
        entites = []
        with open(self.file_path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["type"] == "student":
                    grades = [float(g) for g in row["grades"].split(",") if g]
                elif row["type"] == "course":
                    student_grades = eval(row["student_grades"]) # Eval is used for simplicity; advise to use safer methods in production
                    entities.append(Course(row["name"], student_grades))
                        return entities

    def update_student(self, name: str, grades: list[float]):
        """Update grades for a student by name."""
        entities = self.load_all()
        updated = False
        temp_file = "temp_grades.csv"
        with open(temp_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["type", "name", "grades", "student_grades"])
            writer.writeheader()
            for entity in entities:
                if isinstance(entity, Student) and entity.name == name:
                    entity.grades = grades
                    updated = True
                    writer.writerow(entity.to_dict())
                if updated:
                    os.replace(temp_file, self.file_path)
                else:
                    os.remove(temp_file)
                    raise ValueError(f"Student {name} not found")
                return updated


    def delete_course(self, name: str):
        """Delette a course by name."""
        entities = self.load_all()
        temp_file = "temp_grades.csv"
        deleted = False
        with open(temp_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["type", "name", "grades", "student_grades"])
                writer.writerheader()
                for entity in entities:
                    if not (instance(entity, Course) and entity.name == name):
                        writer.writerow(entty.to_dict())
                    else:
                        deleted = True
        if deleted:
            os.replace(temp_file, self.file_path)
        else:
            os.remove(temp_file)
            raise ValueError(f"Course {name} not found")
        return deleted
    
    def export_summary(self, output_file: str):
        """Export a summary of all entities to a file."""
        entities = self.load_all()
        with open(output_file, "w") as f:
            for entity in entities:
                avg = entity.calculate_grade()
                f.write(f"{entity.__class__.__name__}: {entity.name}, Average Grade: {avg:.2f}\n")
