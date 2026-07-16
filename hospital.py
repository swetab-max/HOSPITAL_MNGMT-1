# Hospital Appointment Booking System

# Dictionary of doctors and their specialties
doctors = {
    1: {"name": "Dr. Sharma", "specialty": "Cardiologist"},
    2: {"name": "Dr. Mehta", "specialty": "Dermatologist"},
    3: {"name": "Dr. Rao", "specialty": "Orthopedic"},
    4: {"name": "Dr. Patel", "specialty": "Pediatrician"}
}

appointments = []

def display_doctors():
    print("\nAvailable Doctors")
    print("-" * 40)
    for key, value in doctors.items():
        print(f"{key}. {value['name']} - {value['specialty']}")
    print("-" * 40)

def book_appointment():
    patient_name = input("Enter Patient Name: ")
    age = input("Enter Age: ")

    display_doctors()

    try:
        choice = int(input("Select Doctor ID: "))

        if choice in doctors:
            date = input("Enter Appointment Date (DD/MM/YYYY): ")
            time = input("Enter Appointment Time (HH:MM): ")

            appointment = {
                "Patient": patient_name,
                "Age": age,
                "Doctor": doctors[choice]["name"],
                "Specialty": doctors[choice]["specialty"],
                "Date": date,
                "Time": time
            }

            appointments.append(appointment)

            print("\nAppointment Booked Successfully!")
            print("-" * 40)
            print(f"Patient : {patient_name}")
            print(f"Doctor  : {doctors[choice]['name']}")
            print(f"Specialty: {doctors[choice]['specialty']}")
            print(f"Date    : {date}")
            print(f"Time    : {time}")
            print("-" * 40)

        else:
            print("Invalid Doctor ID.")

    except ValueError:
        print("Please enter a valid number.")

def view_appointments():
    if len(appointments) == 0:
        print("\nNo appointments booked yet.")
    else:
        print("\nBooked Appointments")
        print("=" * 60)
        for i, appointment in enumerate(appointments, start=1):
            print(f"\nAppointment {i}")
            print(f"Patient    : {appointment['Patient']}")
            print(f"Age        : {appointment['Age']}")
            print(f"Doctor     : {appointment['Doctor']}")
            print(f"Specialty  : {appointment['Specialty']}")
            print(f"Date       : {appointment['Date']}")
            print(f"Time       : {appointment['Time']}")
        print("=" * 60)

# Main Menu
while True:
    print("\nHospital Appointment Booking System")
    print("1. View Doctors")
    print("2. Book Appointment")
    print("3. View Appointments")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_doctors()
    elif choice == "2":
        book_appointment()
    elif choice == "3":
        view_appointments()
    elif choice == "4":
        print("Thank you for using the Hospital Appointment Booking System.")
        break
    else:
        print("Invalid choice. Please try again.")
