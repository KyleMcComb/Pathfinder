from database.models import *
import unittest

# Create your tests here.

class DatabaseTestCase(unittest.TestCase):
    def test_module_table(self):
        fields = [field.name for field in Module._meta.get_fields()]
        self.assertEqual(fields, ['assessment', 'modulelecturer', 'modulepathway', 'studentmodule', 'moduleID', 'moduleName', 'moduleSemester', 'moduleDescription', 'moduleLevel', 'moduleWeight'])
       
    def test_pathway_table(self):
        fields = [field.name for field in Pathway._meta.get_fields()]
        self.assertEqual(fields, ['modulepathway', 'student', 'pathwayID', 'pathwayName', 'pathwayLevels'])
    
    def test_student_table(self):
        fields = [field.name for field in Student._meta.get_fields()]
        self.assertEqual(fields, ['studentmodule', 'studentinterest', 'studentID', 'pathwayID', 'studentCurrentLevel', 'studentCurrentSemester', 'currentPathwayMark'])

    def test_lecturer_table(self):
        fields = [field.name for field in Lecturer._meta.get_fields()]
        self.assertEqual(fields, ['modulelecturer', 'lecturerID', 'lecturerName', 'lecturerEmail'])

    def test_assessment_table(self):
        fields = [field.name for field in Assessment._meta.get_fields()]
        self.assertEqual(fields, ['studentmoduleassesment', 'assessmentID', 'moduleID', 'assessmentType', 'assessmentWeight'])

    def test_module_pathway_table(self):
        fields = [field.name for field in ModulePathway._meta.get_fields()]
        self.assertEqual(fields, ['modulePathwayID', 'moduleID', 'pathwayID', 'mpCore'])

    def test_student_module_table(self):
        fields = [field.name for field in StudentModule._meta.get_fields()]
        self.assertEqual(fields, ['studentmoduleassesment', 'studentModuleID', 'studentID', 'moduleID', 'stuModMark'])

    def test_student_module_assessment_table(self):
        fields = [field.name for field in StudentModuleAssesment._meta.get_fields()]
        self.assertEqual(fields, ['studentModuleAssesmentID', 'studentModuleID', 'assessmentID', 'assesmentMark'])
    
if __name__ == '__main__':
    unittest.main()

