from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StudentModuleAssesment

"""
@Author: @DeanLogan
@Description: Signal handler function triggered after saving a StudentModuleAssessment instance.
Recalculates and updates the total mark for the associated StudentModule.
@param: sender - The sender of the signal (StudentModuleAssessment model).
@param: instance - The instance of the StudentModuleAssessment that was saved.
@param: **kwargs - Additional keyword arguments.
"""
@receiver(post_save, sender=StudentModuleAssesment)
def resetStuModMarks(sender, instance, **kwargs):
    studentModule = instance.studentModuleID
    
    # Get all assessments associated with the given StudentModule
    assessments =  StudentModuleAssesment.objects.filter(studentModuleID=studentModule)
    
    # Initialize the total mark
    totalMark = 0.0
    
    # Calculate the weighted sum of assessment marks
    for assessment in assessments:
        totalMark += assessment.assesmentMark * (assessment.assessmentID.assessmentWeight / 100)

    # Update the StudentModule's stuModMark attribute with the new total mark
    studentModule.stuModMark = totalMark
    studentModule.save()
    print(studentModule.stuModMark)  # Print the updated student module mark after recalculation

