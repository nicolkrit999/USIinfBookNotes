from datetime import datetime, timedelta

def calculate_pages_per_book_by_date(input_date_str):
    # Pages per book
    pages_per_day = {
        "Algorithms and Data Structures": 27,
        "Linear Algebra": 12,
        "Computer Architecture": 9, # Retake, target set to finish on the 31 of october 2024
        "Computer Networking": 16,
        "Operating Systems": 12,
    }

    # Start date of reading sessions
    start_date = datetime(2024, 2, 19)
    try:
        # Convert input string to date
        input_date = datetime.strptime(input_date_str, "%d-%m-%Y")
        
        # Calculate days difference and adjust reading sessions to start from the first session for all books
        days_difference = (input_date - start_date).days
        reading_sessions_up_to_date = (days_difference // 2) + 1  # Include the first session
        
        message = f"By {input_date_str}, your reading targets are:\n"
        
        # Check if the previous target was reached
        previous_target_reached = input("Did you reach the previous target? (true/false): ").strip().lower()
        if previous_target_reached == "false":
            for book, pages in pages_per_day.items():
                actual_pages_read = int(input(f"How many pages did you read from {book}? "))
                expected_pages = pages * reading_sessions_up_to_date
                
                if actual_pages_read < expected_pages:
                    shortfall = expected_pages - actual_pages_read
                    remaining_sessions = reading_sessions_up_to_date - (actual_pages_read // pages)
                    if remaining_sessions > 0:
                        additional_pages_needed_per_session = (shortfall + pages - 1) // remaining_sessions
                        adjusted_pages = additional_pages_needed_per_session + pages
                        message += f"- {book}: {adjusted_pages} pages (adjusted for current progress)\n"
                elif actual_pages_read > expected_pages:
                    message += f"- {book}: You are up to date.\n"
                else:  # Exactly on target
                    message += f"- {book}: {expected_pages} pages (on target).\n"
        else:
            for book, pages in pages_per_day.items():
                total_pages = pages * reading_sessions_up_to_date
                message += f"- {book}: {total_pages} pages\n"
        
        return message
    except ValueError as e:
        return "Invalid input date. Please enter the date in DD-MM-YYYY format."

# Usage example
input_date_str = "25-02-2024"  # Example date for checking
print(calculate_pages_per_book_by_date(input_date_str))
