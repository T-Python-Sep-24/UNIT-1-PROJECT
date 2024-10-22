# resources/local_resources.py

from colorama import Fore

def saudi_resources():
    resources = [
        {"name": "🏥 Saudi Mental Health Clinic", "contact": "123-456", "website": "https://saudimentalhealth.org"},
        {"name": "🌍 National Awareness Program", "contact": "789-101", "website": "https://awareness.sa"},
        {"name": "🏢 Riyadh Therapy Center", "contact": "112-334", "website": "https://riyadhtherapy.com"},
        {"name": "☎️ Jeddah Emotional Support Line", "contact": "556-789", "website": "https://emotionsupport-jeddah.org"},
        {"name": "🌟 Saudi Well-being Network", "contact": "890-123", "website": "https://wellbeing.sa"},
        {"name": "📞 Mind Care Hotline", "contact": "988-123", "website": "https://mindcare.sa"}
    ]
    return resources

def display_resources():
    resources = saudi_resources()
    print(Fore.CYAN + "Here are some local Saudi resources for mental health support:")
    for resource in resources:
        print(Fore.GREEN + f"{resource['name']} - Contact: {resource['contact']} - Website: {resource['website']}")
