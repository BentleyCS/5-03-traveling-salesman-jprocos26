#  analytics  

def get_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def get_highest(numbers):
    return max(numbers) if numbers else 0

def apply_markup(price, percentage):
    return price * (1 + percentage)

def clean_text(words_list):
    cleaned_list = []
    for word in words_list:
        clean_word = word.strip().lower()
        cleaned_list.append(clean_word)
    return cleaned_list

def filter_threshold(numbers, limit):
    filtered_results = []
    for n in numbers:
        if n > limit:
            filtered_results.append(n)
    return filtered_results


#  helper stuff

def linearSearch(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

def binarySearch(items, target):
    left = 0
    right = len(items) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if items[middle] == target:
            return middle
        elif items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1

def inOrder(items):
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


#  assignment  

# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    newPrices = []
    for price in rawPrices:
        newPrice = apply_markup(price, 0.15)
        newPrices.append(newPrice)
    return newPrices


# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    scores = []
    for i in range(n):
        score = int(input("Enter a score: "))
        scores.append(score)
    highest = get_highest(scores)
    average = get_average(scores)
    return highest, average


# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
# and all letters lower case.
def sanitize_usernames(usernames):
    return clean_text(usernames)


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(items):
    return filter_threshold(items, 100)


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
# Sanitize the list to only be lower case words with no extra spaces
# Then return the location of the word using binary search if the list is in order and linear search if it is not.
# example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(items):
    cleanItems = clean_text(items)
    target = input("What item are you looking for? ")
    target = target.strip().lower()
    if inOrder(cleanItems):
        result = binarySearch(cleanItems, target)
    else:
        result = linearSearch(cleanItems, target)
    return result


#  test

print("Test 1: process_expenses")
result = process_expenses([100, 200])
print(result)  
print("Expected: [115.0, 230.0]")

print("\nTest 2: sanitize_usernames")
result = sanitize_usernames(["  Alice  ", "BOB"])
print(result) 
print("Expected: ['alice', 'bob']")

print("\nTest 3: identify_outliers")
result = identify_outliers([50, 150, 80, 200])
print(result)  
print("Expected: [150, 200]")

print(" All tests completed!")