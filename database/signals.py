import math
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from .models import StudentModuleAssessment, StudentModule

"""
@Author: @DeanLogan
@Description: Signal handler function triggered after saving a StudentModuleAssessment instance.
Recalculates and updates the total mark for the associated StudentModule.
@param: sender - The sender of the signal (StudentModuleAssessment model).
@param: instance - The instance of the StudentModuleAssessment that was saved.
@param: **kwargs - Additional keyword arguments.
"""
@receiver(post_save, sender=StudentModuleAssessment)
def resetStuModMarks(sender, instance, **kwargs):
    studentModule = instance.studentModuleID
    
    # Get all assessments associated with the given StudentModule
    assessments =  StudentModuleAssessment.objects.filter(studentModuleID=studentModule)
    
    # Initialize the total mark
    totalMark = 0.0
    
    # Calculate the weighted sum of assessment marks
    for assessment in assessments:
        totalMark += assessment.assessmentMark * (assessment.assessmentID.assessmentWeight / 100)

    # Update the StudentModule's stuModMark attribute with the new total mark
    studentModule.stuModMark = round(totalMark)
    studentModule.save()

"""
@Author: @DeanLogan
@Description: Signal handler function triggered after saving a StudentModule instance. 
Recalculates and updates the current pathway mark for the associated student.
@param: sender - The sender of the signal (StudentModule model).
@param: instance - The instance of the StudentModule that was saved.
@param: **kwargs - Additional keyword arguments.
"""
@receiver(post_save, sender=StudentModule)
def resetCurrentPathwayMarks(sender, instance, **kwargs):
    # Dictionary to store year weightings based on pathway levels
    yearWeightings = {
        3: [10, 30, 60],
        4: [10, 50, 20, 20]
    }

    student = instance.studentID

    # Get all modules associated with the student
    modules = StudentModule.objects.filter(studentID=student)
    
    # Initialize the total mark
    totalMark = 0.0

    # Calculate the weighted sum of module marks
    for module in modules:
        totalMark += (
            (module.stuModMark * (module.moduleID.moduleWeight / 120) * 
            (yearWeightings[student.pathwayID.pathwayLevels][module.moduleID.moduleLevel - 1])) / 100
        )

    # Update the student's currentPathwayMark attribute with the new total mark
    student.currentPathwayMark = math.trunc(totalMark)
    student.save()


# TODO - Talk to team about the current functionality of how editing primary keys works, currently when a primary key is changed, it creates a new record and keeps the old one, this means that the old one will still have all of the links to it and the new one will have nothing. We could delete the old one and resign all of the links (which the function below will help with) but not sure if it's the greatest idea as this default functionality is probably there for a reason.

# TODO - Add docstring
# @receiver(pre_save)
# def updateForeignKey(sender, instance, **kwargs):
#     # Check if the instance is being added or updated
#     if instance._state.adding:
#         return

#     # Get a list of all foreign key fields in the model
#     foreignKeyFields = [field for field in sender._meta.get_fields() if isinstance(field, models.ForeignKey)]

#     for field in foreignKeyFields:
#         relatedModel = field.related_model  # Get the related model
#         relatedFieldName = field.name  # Get the name of the foreign key field
#         primaryKeyFieldName = relatedModel._meta.pk.name  # Get the name of the primary key field in the related model

#         # Check if the related field has changed
#         if field.attname in instance.__dict__:
#             oldValue = instance.__dict__[field.attname]
#             newValue = getattr(instance, field.name)

#             if oldValue != newValue:
#                 # Find all related instances and update their foreign keys
#                 relatedInstances = relatedModel.objects.filter(**{relatedFieldName: oldValue})
#                 for relatedInstance in relatedInstances:
#                     setattr(relatedInstance, relatedFieldName, newValue)
#                     relatedInstance.save()