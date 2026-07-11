import re


def normalize_year(year):

    if year is None:
        return None

    year = str(year)

    result = re.search(r"\d{4}", year)

    if result:
        return int(result.group())

    return None



def normalize_ticker(ticker):

    if ticker is None:
        return None

    ticker = str(ticker)

    ticker = ticker.upper()
    ticker = ticker.strip()

    ticker = re.sub(
        r"[^A-Z0-9]",
        "",
        ticker
    )

    return ticker
