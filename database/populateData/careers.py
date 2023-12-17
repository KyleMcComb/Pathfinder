from ..models import *

### Could use chatgpt to search through and create reasoning of how the module and career link together
### Look at partial name or full name as link

# from database.models import *
# from database.populateData.careers import populateAllModuleCareers, clearAllModuleCareers
# clearAllModuleCareers()
# populateAllModuleCareers()

# Function to clear all career relationships from every module.
def clearAllModuleCareers():
    all_modules = Module.objects.all()
    for module in all_modules:
        module.careers.clear() # Remove all associated careers from this module.

# Function to populate all modules with relevant careers.
def populateAllModuleCareers():
    all_careers = Career.objects.all()
    for career in all_careers:
        addCareerModuleRelationship(career) # Add a career to the careers field in modules.

# Function to add a new career and link it to modules.
def addCareers(jobTitle, companyName, jobDescription):
    # Create a new Career instance.
    career = Career(jobTitle=jobTitle, companyName=companyName, jobDescription=jobDescription)
    try:
        career.save() # Attempt to save the new career.
    except Exception as e:
        print(f"Error saving career: {e}") # Error handling for the save operation.
    addCareerModuleRelationship(career) # Link the new career to relevant modules.

# Function to tokenize a string for analysis.
def tokenize_string(s):
    # Tokenize the string into individual words, and convert to lowercase.
    return set(s.lower().split())

# Function to calculate similarity between a module and a career.
def calculate_similarity(module, career):
    # Define a set of stop words to be excluded from analysis.
    stop_words = set(["to", "and", "of", "in", "for", "the","this","an", "on", "with","is","a","into","will","as","their","use","or","at","all","how"])
    
    # Tokenize and clean module and career information.
    module_name_tokens = tokenize_string(module.moduleName)
    module_desc_tokens = tokenize_string(module.moduleDescription)
    job_desc_tokens = tokenize_string(career.jobDescription)

    # Remove stop words from the tokens.
    module_name_tokens -= stop_words
    module_desc_tokens -= stop_words
    job_desc_tokens -= stop_words

    # Combine tokens from module name and description.
    module_tokens = module_name_tokens.union(module_desc_tokens) # The union method returns a set that contains all the items from both sets, without duplicates.

    # Calculate the similarity score based on common tokens.
    score = len(module_tokens.intersection(job_desc_tokens)) # The intersection method returns a set containing all the items that are present in both sets.
    
    print(f"Module: {module.moduleName}")
    print(f"Career: {career.jobTitle}")
    print(f"Common Tokens: {module_tokens.intersection(job_desc_tokens)}")
    print(f"Score: {score}")

    return score

# Function to link module and career based on a similarity threshold.
def link_module_to_career(module, career, threshold):
    score = calculate_similarity(module, career)

    # Link if the similarity score meets the threshold.
    if score >= threshold:
        print(f"Linking {module.moduleName} with {career.jobTitle}")
        module.careers.add(career)

# Function to establish relationships between careers and modules.
def addCareerModuleRelationship(career):
    all_modules = Module.objects.all() # Fetch all modules.
    similarity_threshold = 5  # Set the threshold for linking.

    # Process each module for a potential link.
    for module in all_modules:
        if calculate_similarity(module, career) >= similarity_threshold:
            link_module_to_career(module, career, similarity_threshold)

# Main execution block to start the module-career population process.
if __name__ == '__main__':
    populateAllModuleCareers()
