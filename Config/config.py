import random

class TestData:
    CHROME_EXECUTABLE_PATH = "C:/Users/juanj/Downloads/chromedriver"

    BASE_URL = "https://quote-qa.edgelogistics.com/login"
    USER_NAME = "jospinad+salesperson@lean-tech.io"
    PASSWORD = "Juanjose1,.-"

    URL_CAPACITY = 'https://capacity-qa.edgelogistics.com/main/loads/all'
    USER_NAME_CAPACITY = 'jospinad@lean-tech.io'
    PASSWORD_CAPACITY = 'juanjose1,.-'

    LOGIN_PAGE_TITLE = "Quote Portal"

    """Data to create a quote"""

    """Load Infomation"""
    CUSTOMER = "EDGE LOGISTICS LLC"
    EQUIPMENT_TYPE = "Auto Hauler"
    WEIGTH = "2306"
    COMMODITY = "Liquid Fertilizer"
    COMMENT = "Quote created from automation test"

    """Shipping Information"""
    ORIGIN1 = " Bakerhill, AL"
    DESTINATION1 = " Birmingham, IA"

    ORIGIN2 = "New York, FL"
    num1 = random.randrange(1000, 10000, 2)
    ORIGIN_ZIP_CODE = f"{num1}"
    DESTINATION2 = " Washington Hill, AL"
    num2 = random.randrange(1000, 10000, 2)
    DESTINATION_ZIP_CODE = f"{num2}"

    EXAMPLE = {
        'customer': 'EDGE LOGISTICS LL',
        'equipment': 'Auto Hauler',
        'commodity': 'Liquid Fertilizer'
    }


