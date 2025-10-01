# Pet Age Calculator
pet_real_age = 0

try:
    pet_type = input("Enter pet type (dog/cat/bird/hamster): ")
    pet_age_in_human_year = int(input("Enter your pet's age in human years: "))

    if (pet_type.lower() != "dog" and pet_type != "cat" and pet_type != "bird" and pet_type != "hamster"):
        print("Wrong pet type (dog/cat/bird/hamster), try again...")
        exit() 
    elif pet_age_in_human_year < 0:
        print("Pet's age can not be under 0, try again...")
        exit() 
    else:
        if pet_type.lower() == "dog" or pet_type.lower() == "cat":
            if pet_age_in_human_year <= 2:
                pet_real_age = pet_age_in_human_year * 12
            else:
                pet_real_age = ((pet_age_in_human_year - 2) * 4) + 24
        elif pet_type.lower() == "bird":
            pet_real_age = pet_age_in_human_year * 9
        else:
            pet_real_age = pet_age_in_human_year * 25

    print("=== PET AGE CONVERSION ===")
    print(f"Pet Type: {pet_type.upper()}")
    print(f"Human Age: {pet_age_in_human_year} year(s)")
    print(f"Pet Age: {pet_real_age} pet years")
    print("-----------------------------")
    print(f"Fun Fact: Your {pet_type.upper()} is like a {pet_real_age}-year-old human!")

except ValueError:
    print("Please Enter valid number for pet's age...")
except Exception as e:
    print(f"Something unexpected happens, ERROR: {e}")