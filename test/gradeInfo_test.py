import unittest  # You can use the unittest library for writing test cases
from main.requestFunctions.gradeInfo import *
from database.models import *

class ModuleInfoForStudentTestCase(unittest.TestCase):

    def setUp(self):
        print("setup")
        # Create Careers
        self.career1 = Career.objects.create(jobTitle='Software Engineer', companyName='TechCorp', jobDescription='Developing software applications')
        self.career2 = Career.objects.create(jobTitle='Data Scientist', companyName='DataCo', jobDescription='Analyzing and interpreting complex data sets')
        self.career1.save()
        self.career2.save()

        # Create Pathways
        self.pathway1 = Pathway.objects.create(pathwayID='P123', pathwayName='Computer Science', pathwayLevels=3)
        self.pathway2 = Pathway.objects.create(pathwayID='P456', pathwayName='Data Science', pathwayLevels=3)
        self.pathway1.save()
        self.pathway2.save()

        # Create Modules
        self.module1 = Module.objects.create(moduleID='M123456', moduleName='Web Development', moduleSemester=3, moduleDescription='Introduction to web development', moduleLevel=1, moduleWeight=20)
        self.module2 = Module.objects.create(moduleID='M789012', moduleName='Data Analysis', moduleSemester=3, moduleDescription='Introduction to data analysis', moduleLevel=1, moduleWeight=20)
        self.module1.save()
        self.module2.save()

        # Add Careers to Modules
        self.module1.careers.add(self.career1)
        self.module2.careers.add(self.career2)

        # Create Assessments
        self.assessment1 = Assessment.objects.create(assessmentID='A1234567', moduleID=self.module1, assessmentType='Assignment', assessmentWeight=20)
        self.assessment2 = Assessment.objects.create(assessmentID='A8901234', moduleID=self.module2, assessmentType='Exam', assessmentWeight=30)
        self.assessment1.save()
        self.assessment2.save()

        # Create Students
        self.student1 = Student.objects.create(studentID=1001, pathwayID=self.pathway1, studentCurrentLevel=2, studentCurrentSemester=2, currentPathwayMark=75)
        self.student2 = Student.objects.create(studentID=1002, pathwayID=self.pathway2, studentCurrentLevel=2, studentCurrentSemester=2, currentPathwayMark=80)
        self.student1.save()
        self.student2.save()

        # Create StudentModules
        self.student_module1 = StudentModule.objects.create(studentID=self.student1, moduleID=self.module1, stuModMark=85)
        self.student_module2 = StudentModule.objects.create(studentID=self.student2, moduleID=self.module2, stuModMark=90)
        self.student_module1.save()
        self.student_module2.save()

        # Create StudentInterests
        self.student_interest1 = StudentInterest.objects.create(studentID=self.student1, interestName='Web Development', interestImportance=3)
        self.student_interest2 = StudentInterest.objects.create(studentID=self.student2, interestName='Data Analysis', interestImportance=4)
        self.student_interest1.save()
        self.student_interest2.save()

        stuModule1 = StudentModule.objects.filter(studentID=self.student1)[0]
        stuModule2 = StudentModule.objects.filter(studentID=self.student2)[0]

        assessment1 = Assessment.objects.filter(assessmentID='A1234567')[0]
        assessment2 = Assessment.objects.filter(assessmentID='A8901234')[0]

        # Create StudentModuleAssessments
        self.student_module_assessment1 = StudentModuleAssessment.objects.create(studentModuleID=stuModule1, assessmentID=assessment1, assessmentMark=90)
        self.student_module_assessment2 = StudentModuleAssessment.objects.create(studentModuleID=stuModule2, assessmentID=assessment2, assessmentMark=85)
        self.student_module_assessment1.save()
        self.student_module_assessment2.save()



    def tearDown(self):
        print("tearDown: Deleting test data...")
        # Delete Careers
        self.career1.delete()
        self.career2.delete()

        # Delete Assessments
        self.assessment1.delete()
        self.assessment2.delete()

        # Delete Pathways
        self.pathway1.delete()
        self.pathway2.delete()

        # Delete StudentModules
        if self.student_module1 and self.student_module1.studentModuleID:
            self.student_module1.delete()
        if self.student_module2 and self.student_module2.studentModuleID:
            self.student_module2.delete()

        # # Delete StudentModuleAssessments
        # if self.student_module_assessment1 and self.student_module_assessment1.studentModuleID:
        #     self.student_module_assessment1.delete()
        # if self.student_module_assessment2 and self.student_module_assessment2.studentModuleID:
        #     self.student_module_assessment2.delete()

        # Delete StudentInterests
        # if self.student_interest1 and self.student_interest1.studentID:
        #     self.student_interest1.delete()
        # if self.student_interest2 and self.student_interest2.studentID:
        #     self.student_interest2.delete()

        # Delete Students
        self.student1.delete()
        self.student2.delete()

        # Delete Modules
        self.module1.delete()
        self.module2.delete()

    def test_module_info_for_student(self):
        # Replace with your student data
        student_data = {
            'studentID': 1001,
            'pathwayID': 'P123',
            'studentCurrentLevel': 2,
            'studentCurrentSemester': 2,
            'currentPathwayMark': 75
        }

        # Replace with your current stage
        current_stage = 2

        # Create a student
        student = Student.objects.create(**student_data)

        # Replace with your module information
        module_info = moduleInfoForStudent(self.student1, current_stage)

        # Perform your assertions based on the expected module information
        self.assertEqual(len(module_info), current_stage)


class CalcAvgMarkTestCase(unittest.TestCase):

    def test_empty_list(self):
        # Test with an empty list
        arr = []
        result = calcAvgMark(arr)
        self.assertEqual(result, 0)

    def test_single_grade(self):
        # Test with a list containing a single grade
        arr = [{'mark': 90}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 90.0)

    def test_multiple_grades(self):
        # Test with a list containing multiple grades
        arr = [{'mark': 80}, {'mark': 90}, {'mark': 70}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 80.0)

    def test_zero_mark(self):
        # Test with a list containing a zero mark
        arr = [{'mark': 0}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 0.0)

    def test_mixed_grades_and_zeros(self):
        # Test with a list containing mixed grades and zeros
        arr = [{'mark': 75}, {'mark': 0}, {'mark': 85}, {'mark': 60}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 55.0)

    def test_invalid_input(self):
        # Test with a list containing an invalid dictionary (missing 'mark' key)
        arr = [{'score': 80}, {'mark': 90}]  # One dictionary is missing the 'mark' key
        with self.assertRaises(KeyError):
            calcAvgMark(arr)

if __name__ == '__main__':
    unittest.main()
