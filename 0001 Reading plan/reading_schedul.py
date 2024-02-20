from datetime import datetime, timedelta

def calculate_pages_per_book_by_date(input_date_str):
    # Pages per book
    pages_per_day = {
        "Algorithms and Data Structures": 27,
        "Linear Algebra": 12,
        "Computer Architecture": 17,
        "Computer Networking": 16,
        "Operating Systems": 12
    }

    # Start date of reading sessions
    start_date = datetime(2024, 2, 19)
    try:
        # Convert input string to date
        input_date = datetime.strptime(input_date_str, "%d-%m-%Y")
        
        # Set reading days distances
        days_difference = (input_date - start_date).days
        reading_sessions_up_to_date = days_difference // 2
        
        # Calculate total pages up to the input date or by the next session for each book
        if days_difference % 2 == 0:  # Input date = reading session
            message = f"By {input_date_str}, you should have read:\n"
        else:  # Input date is not a reading session
            message = f"{input_date_str} is not a reading session. By the next session, you need to have reached:\n"
            reading_sessions_up_to_date += 1  # Adjust for calculating pages by the next session
        
        # Append pages per book to the output
        for book, pages in pages_per_day.items():
            total_pages = pages * reading_sessions_up_to_date
            message += f"- {book}: {total_pages} pages\n"

        return message
    except ValueError as e:
        return "Invalid input date. Please enter the date in DD-MM-YYYY format."

# Usage
input_date_str = "21-02-2024"  # Replace with the date you want to check
print(calculate_pages_per_book_by_date(input_date_str))
