from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


def add_days(start_date: str, days_forward: int) -> str:
    """
    Calculate the date after a given number of days from the starting date.

    Parameters:
    start_date (str): The starting date in the format 'YYYY-MM-DD'.
    days_forward (int): The number of days to add to the starting date.

    Returns:
    str: The resulting date in the format 'YYYY-MM-DD'.
    """
    # Parse the starting date
    date_obj = datetime.strptime(start_date, '%Y-%m-%d')

    # Add the specified number of days
    future_date = date_obj + timedelta(days=days_forward)

    # Format the resulting date back to string
    return future_date.strftime('%Y-%m-%d')


def add_months(start_date: str, months_forward: int) -> str:
    """
    Calculate the date after a given number of months from the starting date.

    Parameters:
    start_date (str): The starting date in the format 'YYYY-MM-DD'.
    months_forward (int): The number of months to add to the starting date.

    Returns:
    str: The resulting date in the format 'YYYY-MM-DD'.
    """
    # Parse the starting date
    date_obj = datetime.strptime(start_date, '%Y-%m-%d')

    # Add the specified number of months
    future_date = date_obj + relativedelta(months=months_forward)

    # Format the resulting date back to string
    return future_date.strftime('%Y-%m-%d')