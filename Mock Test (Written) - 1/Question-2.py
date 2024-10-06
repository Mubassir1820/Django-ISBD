# Write a Python function analyze_ratings(ratings) that takes a list of customer ratings (integers from 1 to 5) and returns another list containing the highest and lowest rating.


def analyze_ratings(ratings):
    
    numberRatings = int(input("Enter the total number of ratings: "))
    ratings = [numberRatings]

    for i in range(numberRatings):
        rating = int(input("Enter the rating between 1 to 5: "))
        if rating < 1 or rating > 5:
            print("Enter a valid rating(1-5)")
            break
        else:
            ratings.append(rating)
    ratings.sort()
    highest_rating = ratings[-1]
    lowest_rating = ratings[0]
    new_rating = [lowest_rating, highest_rating]
    print(f"The lowest and the highest rating is: {new_rating}")

analyze_ratings([])