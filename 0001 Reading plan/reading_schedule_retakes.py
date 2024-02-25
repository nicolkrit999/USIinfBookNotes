from datetime import datetime, timedelta

def calculate_pages_per_book_by_date(input_date_str):
    # Pages per book
    pages_per_day = {
        "Computer Architecture": 9,
    }

    # Start date of reading sessions
    start_date = datetime(2024, 2, 25)
    try:
        # Convert input string to date
        input_date = datetime.strptime(input_date_str, "%d-%m-%Y")
        
        # Calculate days difference and adjust reading sessions to start from the first session for all books
        days_difference = (input_date - start_date).days
        reading_sessions_up_to_date = (days_difference // 2)  # Include the first session
        
        # Check if the previous target was reached
        previous_target_reached = input("Did you reach the previous target? (true/false): ").strip().lower()
        if previous_target_reached == "false":
            for book, pages in pages_per_day.items():
                actual_pages_read = int(input(f"How many pages did you read from {book}? "))
                expected_pages = pages * reading_sessions_up_to_date
                # Evaluate if you read more pages than the target
                if actual_pages_read > expected_pages:
                    if 'message' not in locals():
                        message = ""  # Initialize message if not already done
                    message += "You are up to date.\n"  # Adding a newline for clarity
                # Calculate the new target based on pages not read
                if actual_pages_read < expected_pages:
                    # Calculate the shortfall and adjust future targets accordingly
                    shortfall = expected_pages - actual_pages_read
                    # Adjust the pages per day for this book to catch up over the remaining sessions
                    remaining_sessions = reading_sessions_up_to_date - (actual_pages_read // pages)
                    if remaining_sessions > 0:
                        additional_pages_needed_per_session = (shortfall + pages - 1) // remaining_sessions
                        pages_per_day[book] += additional_pages_needed_per_session
        
        message = f"By {input_date_str}, your targets adjusted for progress are:\n"
        for book, pages in pages_per_day.items():
            # Calculate new total pages target considering the adjustment
            total_pages = pages * reading_sessions_up_to_date
            message += f"- {book}: {total_pages} pages (adjusted for current progress)\n"
        
        return message
    except ValueError as e:
        return "Invalid input date. Please enter the date in DD-MM-YYYY format."

# Usage example
input_date_str = "19-02-2024"  # Example date for checking
print(calculate_pages_per_book_by_date(input_date_str))
