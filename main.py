from services import InsuranceSystem

def main():
    system = InsuranceSystem()
    print("Καλωσήρθατε στο Σύστημα Διαχείρισης Δηλώσεων Ατυχήματος Οχημάτων")

    username = input("Username οδηγού: ")
    password = input("Password: ")
    
    driver = system.authenticate_driver(username, password)
    if not driver:
        print("Λάθος username ή password. Έξοδος.")
        return
    
    while True:
        print("\n--- Μενού ---")
        print("1. Νέα δήλωση ατυχήματος")
        print("2. Προβολή δηλώσεών μου")
        print("3. Αναζήτηση συνεργείου και κράτηση ραντεβού")
        print("4. Προβολή προσωπικού συμβολαίου")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")

        if choice == "1":
            
            policy_code = input("Κωδικός συμβολαίου: ")
            other_company = input("Ασφαλιστική εταιρεία άλλου οχήματος: ")
            date = input("Ημερομηνία (YYYY-MM-DD): ")
            time = input("Ώρα (HH:MM): ")
            street = input("Οδός: ")
            area = input("Περιοχή: ")
            postal_code = input("Ταχυδρομικός κώδικας: ")
            photo1 = input("Φωτογραφία 1 (path ή 'κανένα'): ") or "κανένα"
            photo2 = input("Φωτογραφία 2 (path ή 'κανένα'): ") or "κανένα"

            report = system.create_accident_report(driver, policy_code, other_company, 
                                                 date, time, street, area, postal_code, photo1, photo2)
            if report:
                print("Η δήλωση ολοκληρώθηκε:")
                print(report)
                system.send_email_to_driver(report)

        elif choice == "2":
            reports = system.list_reports_for_driver(driver)
            if not reports:
                print("Δεν έχετε δηλώσεις.")
            else:
                for r in reports:
                    print(r)

        elif choice == "3":
            area = input("Περιοχή για αναζήτηση συνεργείου: ")
            shops = system.search_repair_shops(area)
            if shops:
                print("\nΔιαθέσιμα συνεργεία στην περιοχή σας:")
                for shop in shops:
                    print(shop)
                    
                try:
                    shop_id = int(input("Επιλογή id συνεργείου: "))
                    shop = system.find_shop_by_id(shop_id)
                    
                    if not shop:
                        print("Μη έγκυρο id συνεργείου.")   
                        continue
                
                    report_id = int(input("Επιλογή id δήλωσης για ραντεβού: "))            
                    result = system.choose_repair_shop(report_id, shop_id)
                
                    if result:
                        print(f"Το ραντεβού στο {shop.name} έχει καταχωρηθεί.")
                        print(result)
                        system.send_email_to_repair_shop(result, shop)
                    
                    else:
                        print("Μη έγκυρο id συνεργείου ή δήλωσης.")     
                        
                except ValueError:
                    print("Μη έγκυρη ID συνεργείου ή δήλωσης.")
            else :
                    print("Δεν βρέθηκαν συνεργεία στην περιοχή σας.")
                    
            
        elif choice == "4":
                policies = system.list_policies_for_driver(driver)
                if not policies:
                    print("Δεν έχετε συμβόλαια.")
                else:         
                    print("\nΤα συμβόλαιά σας:")
                for p in policies:
                    print(p)

        elif choice == "0":
            print("Έξοδος από το σύστημα. Αντίο!")
            break

        else:
            print("Μη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()
