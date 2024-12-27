
## Isandla Community Organization {Program Management Software 🏢🎉}

This Python program models the various programs and events of a community organization focused on youth development. It uses Object-Oriented Programming (OOP) principles to manage and display details of different types of programs and events.

## Features 🌟
- **Programs**: Manage workshops, seminars, and other youth development programs.
- **Events**: Track and manage different events, including fundraising and social gatherings.
- **OOP Design**: Built using object-oriented programming to model the real-world organization structure.

## Classes 🧑‍💻

### 1. `Program` class 📝
Represents a general program offered by the organization.
- Attributes: `title`, `description`, `date`
- Method: `get_details()`

### 2. `Workshop` class 🛠️
A subclass of `Program` representing a workshop.
- Additional Attributes: `instructor`, `sessions`
- Method: `get_details()`

### 3. `Seminar` class 🎤
A subclass of `Program` representing a seminar.
- Additional Attributes: `keynote_speaker`
- Method: `get_details()`

### 4. `Event` class 🎪
Represents a general event organized by the organization.
- Attributes: `name`, `location`, `date`
- Method: `get_details()`

### 5. `FundraisingEvent` class 💰
A subclass of `Event` representing a fundraising event.
- Additional Attribute: `goal_amount`
- Method: `get_details()`

### 6. `SocialEvent` class 🥳
A subclass of `Event` representing a social gathering.
- Additional Attribute: `event_type`
- Method: `get_details()`
