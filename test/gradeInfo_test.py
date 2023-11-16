import unittest
from main.requestFunctions.gradeInfo import *
from database.models import *

# To run these unit tests enter the following command in the terminal: python manage.py test test.gradeInfo_test
# Note: any method that requires a "request" parameter is not tested here as these will be tested through integration testing and user testing, as it is easier to verify the results.

class GradeInfoTestCases(unittest.TestCase):
    def test_avg_mark_valid(self):
        arr = [{'mark': 75.0}, {'mark': 80.0}, {'mark': 90.0}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 81.66666666666667)  # Calculated as (75.0 + 80.0 + 90.0) / 3

    def test_avg_mark_empty(self):
        arr = []
        result = calcAvgMark(arr)
        self.assertEqual(result, 0)

    def test_avg_mark_single_entry(self):
        arr = [{'mark': 85.0}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 85.0)

    def test_avg_mark_zero_marks(self):
        arr = [{'score': 95.0}, {'score': 88.0}, {'score': 92.0}]  # 'score' instead of 'mark'
        result = calcAvgMark(arr)
        self.assertEqual(result, 0)

    def test_avg_mark_negative_marks(self):
        arr = [{'mark': -75.0}, {'mark': -80.0}, {'mark': -90.0}]
        result = calcAvgMark(arr)
        self.assertEqual(result, -81.66666666666667)  # Calculated as (-75.0 - 80.0 - 90.0) / 3

    def test_module_avg_all_stages_valid(self):
        stages = [
            [
                {'name': 'Databases', 'mark': 72.0, 'weighting': 20, 'assessments': [{'name': 'Class Test', 'mark': 70.0}, {'name': 'Project', 'mark': 70.0}, {'name': 'Timed exam on Computer', 'mark': 75.0}]},
                {'name': 'Fundamentals of Maths for Computing', 'mark': 70.0, 'weighting': 20, 'assessments': [{'name': 'Continual Assessment', 'mark': 70.0}, {'name': 'Timed exam on Computer', 'mark': 70.0}]}
            ],
            [
                {'name': 'Systems Security and Cryptography', 'mark': 94.0, 'weighting': 20, 'assessments': [{'name': 'Class Test 1', 'mark': 98.0}, {'name': 'Class Test 2', 'mark': 90.0}]},
                {'name': 'Modern Web App Development', 'mark': 86.0, 'weighting': 20, 'assessments': [{'name': 'Continual Assessment', 'mark': 70.0}, {'name': 'Project', 'mark': 93.0}]}
            ]
        ]

        result = moduleAvgAllStages(stages)

        self.assertEqual(result, 80.5)  # Calculated as (72.0 + 70.0 + 94.0 + 86.0) / 4

    def test_module_avg_all_stages_empty(self):
        stages = []

        result = moduleAvgAllStages(stages)

        self.assertEqual(result, 0)

    def test_assessment_avg_all_stages_valid(self):
        stages = [
            [
                {'name': 'Databases', 'mark': 72.0, 'weighting': 20, 'assessments': [{'name': 'Class Test', 'mark': 70.0}, {'name': 'Project', 'mark': 70.0}, {'name': 'Timed exam on Computer', 'mark': 75.0}]},
                {'name': 'Fundamentals of Maths for Computing', 'mark': 70.0, 'weighting': 20, 'assessments': [{'name': 'Continual Assessment', 'mark': 70.0}, {'name': 'Timed exam on Computer', 'mark': 70.0}]}
            ],
            [
                {'name': 'Systems Security and Cryptography', 'mark': 94.0, 'weighting': 20, 'assessments': [{'name': 'Class Test 1', 'mark': 98.0}, {'name': 'Class Test 2', 'mark': 90.0}]},
                {'name': 'Modern Web App Development', 'mark': 86.0, 'weighting': 20, 'assessments': [{'name': 'Continual Assessment', 'mark': 70.0}, {'name': 'Project', 'mark': 93.0}]}
            ]
        ]

        result = assessmentAvgAllStages(stages)

        self.assertEqual(result, 79.29166666666667)  # Calculated as (70.0 + 70.0 + 70.0 + 93.0) / 4

    def test_assessment_avg_all_stages_empty(self):
        stages = []

        result = assessmentAvgAllStages(stages)

        self.assertEqual(result, 0)

    def test_assessment_info_for_valid_ids(self):
        student = Student.objects.get(studentID=40294254)
        studentModules = StudentModule.objects.filter(studentID=student.studentID).select_related('moduleID')
        moduleLevels = studentModules.values_list('moduleID', 'moduleID__moduleLevel')
        moduleIds = [moduleId for moduleId, _ in moduleLevels]
        result = assessmentInfoForStudentsModule(studentID=student, moduleID=moduleIds[0])

        compareWith = [{'name': 'Class Test', 'mark': 70.0}, {'name': 'Project', 'mark': 70.0}, {'name': 'Timed exam on Computer', 'mark': 75.0}]

        self.assertEqual(result, compareWith)

    def test_assessment_info_for_nonexistent_student(self):
        result = assessmentInfoForStudentsModule(studentID=999, moduleID=1)
        self.assertEqual(result, [])

    def test_module_info_for_student(self):
        # Replace with your student data
        comparingWith = [[{'name': 'Databases', 'mark': 72.0, 'weighting': 20, 'assessments': [{'name': 'Class Test', 'mark': 70.0}, {'name': 'Project', 'mark': 70.0}, {'name': 'Timed exam on Computer', 'mark': 75.0}]}, {'name': 
'Fundamentals of Maths for Computing', 'mark': 70.0, 'weighting': 20, 'assessments': [{'name': 'Continual Assessment', 'mark': 70.0}, {'name': 'Timed exam on Computer', 'mark': 70.0}]}, {'name': 'Introduction to Computer Architecture', 'mark': 70.0, 'weighting': 20, 'assessments': [{'name': 'Continual Assessment', 'mark': 70.0}]}, {'name': 'Procedural Programming', 'mark': 20.0, 'weighting': 20, 'assessments': [{'name': 'Continual Assessment', 'mark': 20.0}]}, {'name': 'Object Oriented Programming', 'mark': 67.0, 'weighting': 20, 'assessments': [{'name': 'Class Test', 'mark': 67.0}, {'name': 'Project', 'mark': 67.0}, {'name': 'Timed exam on Computer', 'mark': 67.0}]}, {'name': 'Web Technologies', 'mark': 74.0, 'weighting': 20, 'assessments': [{'name': 'Project', 'mark': 75.0}, {'name': 'Continual Assessment', 'mark': 72.0}]}], [{'name': 'Systems Security and Cryptography', 'mark': 94.0, 'weighting': 20, 'assessments': [{'name': 'Class Test 1', 'mark': 98.0}, {'name': 'Class Test 2', 'mark': 90.0}]}, {'name': 'Modern Web App Development', 'mark': 86.0, 'weighting': 20, 'assessments': [{'name': 'Continual Assessment', 'mark': 70.0}, {'name': 'Project', 'mark': 93.0}]}, {'name': 'Networks and Protocols', 'mark': 78.0, 'weighting': 20, 'assessments': [{'name': 'Continual Assessment', 'mark': 78.0}]}, {'name': 'User Experience Design', 'mark': 72.0, 'weighting': 20, 'assessments': [{'name': 'Project', 'mark': 72.0}]}, {'name': 'Introduction to Enterprise Computing', 'mark': 56.0, 'weighting': 20, 'assessments': [{'name': 'Project', 'mark': 56.0}, {'name': 'Timed exam on Computer', 'mark': 56.0}]}, {'name': 'Server Side Web Development', 'mark': 34.0, 'weighting': 20, 'assessments': [{'name': 'Project', 'mark': 34.0}]}]]

        # Replace with your module information
        student = Student.objects.get(studentID=40294254)
        moduleInfo = moduleInfoForStudent(student, 2)

        # Perform your assertions based on the expected module information
        self.assertEqual(moduleInfo, comparingWith)

    def test_empty_list(self):
        arr = []
        result = calcAvgMark(arr)
        self.assertEqual(result, 0)

    def test_single_grade(self):
        arr = [{'mark': 90}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 90.0)

    def test_multiple_grades(self):
        arr = [{'mark': 80}, {'mark': 90}, {'mark': 70}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 80.0)

    def test_zero_mark(self):
        arr = [{'mark': 0}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 0.0)

    def test_mixed_grades_and_zeros(self):
        arr = [{'mark': 75}, {'mark': 0}, {'mark': 85}, {'mark': 60}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 55.0)

    def test_invalid_input(self):
        arr = [{'score': 80}, {'mark': 90}]  # One dictionary is missing the 'mark' key
        result = calcAvgMark(arr)
        self.assertEqual(result, 0)

    def test_left_to_earn(self):
        student = Student.objects.get(studentID=40294254)
        result = calcLeftToEarn(2, student)
        self.assertEqual(result, 60)

    # def setUp(self):
    #     print("setup")
    #     # Create Careers
    #     self.career1 = Career.objects.create(jobTitle='Software Engineer', companyName='TechCorp', jobDescription='Developing software applications')
    #     self.career2 = Career.objects.create(jobTitle='Data Scientist', companyName='DataCo', jobDescription='Analyzing and interpreting complex data sets')
    #     self.career1.save()
    #     self.career2.save()

    #     # Create Pathways
    #     self.pathway1 = Pathway.objects.create(pathwayID='P123', pathwayName='Computer Science', pathwayLevels=3)
    #     self.pathway2 = Pathway.objects.create(pathwayID='P456', pathwayName='Data Science', pathwayLevels=3)
    #     self.pathway1.save()
    #     self.pathway2.save()

    #     # Create Modules
    #     self.module1 = Module.objects.create(moduleID='M123456', moduleName='Web Development', moduleSemester=3, moduleDescription='Introduction to web development', moduleLevel=1, moduleWeight=20)
    #     self.module2 = Module.objects.create(moduleID='M789012', moduleName='Data Analysis', moduleSemester=3, moduleDescription='Introduction to data analysis', moduleLevel=1, moduleWeight=20)
    #     self.module1.save()
    #     self.module2.save()

    #     # Add Careers to Modules
    #     self.module1.careers.add(self.career1)
    #     self.module2.careers.add(self.career2)

    #     # Create Assessments
    #     self.assessment1 = Assessment.objects.create(assessmentID='A1234567', moduleID=self.module1, assessmentType='Assignment', assessmentWeight=20)
    #     self.assessment2 = Assessment.objects.create(assessmentID='A8901234', moduleID=self.module2, assessmentType='Exam', assessmentWeight=30)
    #     self.assessment1.save()
    #     self.assessment2.save()

    #     # Create Students
    #     self.student1 = Student.objects.create(studentID=1001, pathwayID=self.pathway1, studentCurrentLevel=2, studentCurrentSemester=2, currentPathwayMark=75)
    #     self.student2 = Student.objects.create(studentID=1002, pathwayID=self.pathway2, studentCurrentLevel=2, studentCurrentSemester=2, currentPathwayMark=80)
    #     self.student1.save()
    #     self.student2.save()

    #     # Create StudentModules
    #     self.student_module1 = StudentModule.objects.create(studentID=self.student1, moduleID=self.module1, stuModMark=85)
    #     self.student_module2 = StudentModule.objects.create(studentID=self.student2, moduleID=self.module2, stuModMark=90)
    #     self.student_module1.save()
    #     self.student_module2.save()

    #     # Create StudentInterests
    #     self.student_interest1 = StudentInterest.objects.create(studentID=self.student1, interestName='Web Development', interestImportance=3)
    #     self.student_interest2 = StudentInterest.objects.create(studentID=self.student2, interestName='Data Analysis', interestImportance=4)
    #     self.student_interest1.save()
    #     self.student_interest2.save()

    #     stuModule1 = StudentModule.objects.filter(studentID=self.student1)[0]
    #     stuModule2 = StudentModule.objects.filter(studentID=self.student2)[0]

    #     assessment1 = Assessment.objects.filter(assessmentID='A1234567')[0]
    #     assessment2 = Assessment.objects.filter(assessmentID='A8901234')[0]

    #     # Create StudentModuleAssessments
    #     self.student_module_assessment1 = StudentModuleAssessment.objects.create(studentModuleID=stuModule1, assessmentID=assessment1, assessmentMark=90)
    #     self.student_module_assessment2 = StudentModuleAssessment.objects.create(studentModuleID=stuModule2, assessmentID=assessment2, assessmentMark=85)
    #     self.student_module_assessment1.save()
    #     self.student_module_assessment2.save()



    # def tearDown(self):
    #     print("tearDown: Deleting test data...")
    #     # Delete Careers
    #     self.career1.delete()
    #     self.career2.delete()

    #     # Delete Assessments
    #     self.assessment1.delete()
    #     self.assessment2.delete()

    #     # Delete Pathways
    #     self.pathway1.delete()
    #     self.pathway2.delete()

    #     # Delete StudentModules
    #     if self.student_module1 and self.student_module1.studentModuleID:
    #         self.student_module1.delete()
    #     if self.student_module2 and self.student_module2.studentModuleID:
    #         self.student_module2.delete()

    #     # # Delete StudentModuleAssessments
    #     # if self.student_module_assessment1 and self.student_module_assessment1.studentModuleID:
    #     #     self.student_module_assessment1.delete()
    #     # if self.student_module_assessment2 and self.student_module_assessment2.studentModuleID:
    #     #     self.student_module_assessment2.delete()

    #     # Delete StudentInterests
    #     # if self.student_interest1 and self.student_interest1.studentID:
    #     #     self.student_interest1.delete()
    #     # if self.student_interest2 and self.student_interest2.studentID:
    #     #     self.student_interest2.delete()

    #     # Delete Students
    #     self.student1.delete()
    #     self.student2.delete()

    #     # Delete Modules
    #     self.module1.delete()
    #     self.module2.delete()


if __name__ == '__main__':
    unittest.main()
