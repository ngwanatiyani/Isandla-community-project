# event.py

class Event:
    def __init__(self, name, location, date):
        self.name = name
        self.location = location
        self.date = date

    def get_details(self):
        return f"Event Name: {self.name}\nLocation: {self.location}\nDate: {self.date}"

class FundraisingEvent(Event):
    def __init__(self, name, location, date, goal_amount):
        super().__init__(name, location, date)
        self.goal_amount = goal_amount

    def get_details(self):
        return super().get_details() + f"\nGoal Amount: {self.goal_amount}"

class SocialEvent(Event):
    def __init__(self, name, location, date, event_type):
        super().__init__(name, location, date)
        self.event_type = event_type

    def get_details(self):
        return super().get_details() + f"\nEvent Type: {self.event_type}"
