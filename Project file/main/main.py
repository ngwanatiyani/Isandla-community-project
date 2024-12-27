
from program import Workshop, Seminar  # Importing classes from program.py
from event import FundraisingEvent, SocialEvent  # Importing classes from event.py

def main():
    # Create a Workshop instance
    workshop = Workshop("Python Programming Workshop", "Learn Python programming from scratch.", "2024-01-10", "Tiyani Ngwana", 5)
    print(workshop.get_details())
    print()  # Add a space between outputs

    # Create a Seminar instance
    seminar = Seminar("Tech Trends Seminar", "Explore the latest trends in technology.", "2024-02-20", "Amanda Msutu")
    print(seminar.get_details())
    print()  # Add a space between outputs

    # Create a FundraisingEvent instance
    fundraising_event = FundraisingEvent("Charity Gala", "Grand Hall", "2024-03-15", 10000)
    print(fundraising_event.get_details())
    print()  # Add a space between outputs

    # Create a SocialEvent instance
    social_event = SocialEvent("Community Picnic", "Central Park", "2024-04-20", "Casual Gathering")
    print(social_event.get_details())
    print()  # Add a space between outputs

if __name__ == "__main__":
    main()
