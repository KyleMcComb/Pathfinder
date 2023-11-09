from ..models import *

### Could use chatgpt to search through and create reasoning of how the module and career link together
### Look at partial name or full name as link

def clearAllModuleCareers():
    all_modules = Module.objects.all()
    for module in all_modules:
        module.careers.clear()

def populateAllModuleCareers():
    all_careers = Career.objects.all()
    for career in all_careers:
        addCareerModuleRelationship(career)

def addCareers(jobTitle, companyName, jobDescription):
    career = Career(jobTitle=jobTitle, companyName=companyName, jobDescription=jobDescription)
    try:
        career.save()
    except Exception as e:
        print(f"Error saving career: {e}")
    addCareerModuleRelationship(career)

def tokenize_string(s):
    # Tokenize the string into individual words, and convert to lowercase
    return set(s.lower().split())

def calculate_similarity(module, career):
    stop_words = set(["to", "and", "of", "in", "for"])

    module_name_tokens = tokenize_string(module.moduleName)
    module_desc_tokens = tokenize_string(module.moduleDescription)
    job_desc_tokens = tokenize_string(career.jobDescription)

    # Remove stop words from the tokens
    module_name_tokens -= stop_words
    module_desc_tokens -= stop_words
    job_desc_tokens -= stop_words

    # Combine tokens from module name and description
    module_tokens = module_name_tokens.union(module_desc_tokens) # The union method returns a set that contains all the items from both sets, without duplicates.

    # Calculate the similarity score
    score = len(module_tokens.intersection(job_desc_tokens)) # The intersection method returns a set containing all the items that are present in both sets.
    
    print(f"Module: {module.moduleName}")
    print(f"Career: {career.jobTitle}")
    print(f"Common Tokens: {module_tokens.intersection(job_desc_tokens)}")
    print(f"Score: {score}")

    return score

def link_module_to_career(module, career, threshold):
    score = calculate_similarity(module, career)

    if score >= threshold:
        print(f"Linking {module.moduleName} with {career.jobTitle}")
        module.careers.add(career)

def addCareerModuleRelationship(career):
    # Fetch all the Module instances from the database
    all_modules = Module.objects.all()
    similarity_threshold = 2  # this can be adjusted based on your requirements

    for module in all_modules:
        if calculate_similarity(module, career) >= similarity_threshold:
            link_module_to_career(module, career, similarity_threshold)

if __name__ == '__main__':
    populateAllModuleCareers()
