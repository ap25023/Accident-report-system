class Driver:
    def __init__(self, driver_id: int, name: str, email: str, phone: str, username: str, password: str):
        self.driver_id = driver_id
        self.name = name
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f"{self.driver_id}: {self.name} ({self.email})"


class InsurancePolicy: 
    def __init__(self, policy_code: str, plate_number: str, car_make: str, horsepower: int,
                 coverage_type: str, start_date: str, end_date: str, premium_amount: float, driver: 'Driver'):
        self.policy_code = policy_code
        self.plate_number = plate_number
        self.car_make = car_make
        self.horsepower = horsepower
        self.coverage_type = coverage_type 
        self.start_date = start_date
        self.end_date = end_date
        self.premium_amount = premium_amount
        self.driver = driver

    def __str__(self) -> str:
        return (f"Policy {self.policy_code} - {self.plate_number} ({self.car_make}, "
                f"{self.horsepower} ίπποι) - {self.coverage_type} - Ασφάλιστρα ({self.premium_amount}€)") 


class AccidentReport: 
    def __init__(self, report_id: int, policy: InsurancePolicy, other_company: str,
                 date: str, time: str, street: str, area: str, postal_code: str,
                 photo1: str = None, photo2: str = None):
        self.report_id = report_id
        self.policy = policy
        self.other_company = other_company
        self.date = date
        self.time = time
        self.street = street
        self.area = area
        self.postal_code = postal_code
        self.photo1 = photo1
        self.photo2 = photo2
        self.status = "Ολοκληρωμένη"  

    def __str__(self) -> str:
        photos = f"Φ1: {self.photo1 or 'Κανένα'}, Φ2: {self.photo2 or 'Κανένα'}"
        return (f"Report {self.report_id} - {self.policy.policy_code} "
                f"({self.date} {self.time}, {self.street}, {self.area} {self.postal_code}) "
                f"[{self.other_company}] - {photos}")


class RepairShop: 
    def __init__(self, shop_id: int, name: str, address: str, area: str, postal_code: str,
                 owner_name: str, phone: str, email: str, license_number: str):
        self.shop_id = shop_id
        self.name = name
        self.address = address
        self.area = area
        self.postal_code = postal_code
        self.owner_name = owner_name
        self.phone = phone
        self.email = email
        self.license_number = license_number

    def __str__(self) -> str:
        return (f"{self.shop_id}: {self.name} ({self.area}, {self.address}, {self.postal_code}) - "
                f"Ιδιοκτήτης: {self.owner_name}, Τηλ: {self.phone}")
