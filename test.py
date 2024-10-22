


def send_message(self,violation_id:int,message:str)->None:
            if self.violations:                     
                for violation in self.violations:
                    if violation_id==violation['Violation_id']:
                        violation['Message']=f'from {self.get_user_name()}\n{message}'
                        break
                else:
                    print("there is no violation with this ID")                           
            else:
                print(f"there is no violations! for {self.get_id()}")
            
        
def get_objection(self,resident_id:str):
            residents:Resident=Data_management.load_file('Residents.pkl')
            if resident_id in residents:
                for resident in  residents[resident_id].violations:
                    if resident['Ministry']==self.get_ministry_name()and resident['Message']:
                        print(f" {resident['Message']}")
            else:
                print("there is no resident with this ID!")
            
def send_response(self,resident_id:str):
            residents:Resident=Data_management.load_file('Residents.pkl')
            if resident_id in residents:
                for resident in  residents[resident_id].violations:
                    if resident['Ministry']==self.get_ministry_name()and resident['Message']:
                        print(resident['Message'])
            else:
                print("there is no resident with this ID!")

amont=4000*(50.0/100)
print(amont)