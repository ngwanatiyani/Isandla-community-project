class Program:
    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date

    def get_details(self):
        return f"Program Title: {self.title}\nDescription: {self.description}\nDate: {self.date}"


class Workshop(Program):
    def __init__(self, title, description, date, instructor, sessions):
        super().__init__(title, description, date)
        self.instructor = instructor
        self.sessions = sessions

    def get_details(self):
        return super().get_details() + f"\nInstructor: {self.instructor}\nSessions: {self.sessions}"


class Seminar(Program):
    def __init__(self, title, description, date, keynote_speaker):
        super().__init__(title, description, date)
        self.keynote_speaker = keynote_speaker

    def get_details(self):
        return super().get_details() + f"\nKeynote Speaker: {self.keynote_speaker}"
