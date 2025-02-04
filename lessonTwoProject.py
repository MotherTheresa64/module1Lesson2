score = int(input("Enter your score: "))   

if score > 90:
    print("Excellent")
elif score < 90 and score >= 70:
    print("Good")
else:
    print("Needs improvement")