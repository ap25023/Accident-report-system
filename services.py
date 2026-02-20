
from models import Driver, InsurancePolicy, AccidentReport, RepairShop


class InsuranceSystem:
    def __init__(self):
        self.drivers = []  
        self.policies = [] 
        self.reports = []  
        self.repair_shops = []  

        self._next_driver_id = 1
        self._next_report_id = 1

        self._seed_demo_data()

    def _seed_demo_data(self) -> None:
        driver1 = Driver(self._next_driver_id, "Δημήτρης Λεϊμονής", "ap25023@hua.gr", "6901234567", "dimitris", "123456")
        self.drivers.append(driver1)
        self._next_driver_id += 1
        
        driver2 = Driver(self._next_driver_id, "Κώστας Γεωργίου", "kostas@gmail.com", "6907654321", "kostas", "abc123")
        self.drivers.append(driver2)
        self._next_driver_id += 1


        policy1 = InsurancePolicy("10", "ΙΧΥ3722", "Peugeot", 90, "Απλή", "2025-01-01", "2025-12-31", 250.0, driver1)
        policy2 = InsurancePolicy("20", "ΤΡΚ568", "Maclaren", 600, "Μικτή", "2025-02-01", "2025-12-31", 800.0, driver2)
        self.policies.extend([policy1, policy2])

    
        shop1 = RepairShop(1, "MOTODROMOS", "Μεσογείων 161", "Αθηνα", "11526", "Δημήτρης Γούναρης", "2107101882", "motodromos@gmail.com", "1")
        shop2 = RepairShop(2, "SmartService", "Βενιζέλου 24", "Θεσσαλονικη", "54628", "Νίκος Γεωργίου", "23104008474", "smartservice@gmail.com", "2")
        shop3 = RepairShop(3, "PatrasAuto", "Πανεπιστημίου", "Πατρα", "26443", "Κώστας Τσιμπούκης", "2105556666", "patraauto@gmail.com", "3")
        self.repair_shops.extend([shop1, shop2, shop3])

    def authenticate_driver(self, username: str, password: str) -> Driver | None:
        for d in self.drivers:
            if d.username == username and d.password == password:
                return d
        return None

    def find_policy_by_code(self, policy_code: str) -> InsurancePolicy | None:
        for p in self.policies:
            if p.policy_code == policy_code:
                return p
        return None


    def create_accident_report(self, driver: Driver, policy_code: str, other_company: str,
                               date: str, time: str, street: str, area: str, postal_code: str,
                               photo1: str = None, photo2: str = None) -> AccidentReport | None:
        policy = self.find_policy_by_code(policy_code)
        if not policy or policy.driver != driver:
            print("Δεν βρέθηκε έγκυρο συμβόλαιο για αυτόν τον οδηγό.")
            return None

        report = AccidentReport(self._next_report_id, policy, other_company, date, time,
                                street, area, postal_code, photo1, photo2)
        self.reports.append(report)
        self._next_report_id += 1
        return report

    def list_reports_for_driver(self, driver: Driver) -> list[AccidentReport]:
                return [r for r in self.reports if r.policy.driver == driver]

    def search_repair_shops(self, area: str) -> list[RepairShop]:
        input_area = area.lower()
        result = []
        for s in self.repair_shops:           
            if input_area in s.area.lower():
                result.append(s)
        return result

    def find_shop_by_id(self, shop_id: int) -> RepairShop | None:
        for s in self.repair_shops:
            if s.shop_id == shop_id:
                return s
        return None


    def send_email_to_driver(self, report: AccidentReport):
        print(f"\n EMAIL ΣΤΟΝ ΟΔΗΓΟ ({report.policy.driver.email}):")
        print("Θέμα: Επιβεβαίωση Δήλωσης Ατυχήματος")
        print(f"Η δήλωσή σας {report.report_id} ολοκληρώθηκε επιτυχώς.")
        print("Θα επικοινωνήσουμε σύντομα μαζί σας.")

    def send_email_to_repair_shop(self, report: AccidentReport, shop: RepairShop):
        print(f"\n EMAIL ΣΤΟ ΣΥΝΕΡΓΕΙΟ ({shop.email}):")
        print("Θέμα: Νέο Ραντεβού Επισκευής")
        print(f"Οδηγός: {report.policy.driver.name} ({report.policy.driver.phone})")
        print(f"Συμβόλαιο: {report.policy.policy_code}, Πινακίδα: {report.policy.plate_number}")
        print(f"{report.policy.car_make}, {report.policy.horsepower} ίπποι")
        print(f"Ατύχημα: {report.date} {report.time}, {report.area}")

    def list_policies_for_driver(self, driver: Driver) -> list[InsurancePolicy]:
        return [p for p in self.policies if p.driver == driver] 
    
    
    def choose_repair_shop(self, report_id: int, shop_id: int) -> AccidentReport | None:
        report = next((r for r in self.reports if r.report_id == report_id), None)
        shop = self.find_shop_by_id(shop_id)
        
        if report and shop:
            report.status += f" - Συνεργείο: {shop.name}"
            return report
        return None
