from datetime import date, timedelta


def transform_post_date(post_date_array):
    digit_post_date = convert_to_digit(post_date_array)
    post_date = convert_to_date(digit_post_date)
    return post_date


def convert_to_digit(post_date_array):
    transform_digit_post_date = []

    for item in post_date_array:
        item = item.replace("PostedAujourd'hui", "0")
        item = item.replace("30+", "30")

        for subitem in item.split():
            if (subitem.isdigit()):
                transform_digit_post_date.append(int(subitem))

    return transform_digit_post_date


def convert_to_date(digit_post_date):
    post_date = []

    for digit in digit_post_date:
        post_date.append(date.today() - timedelta(days=digit))

    return post_date
