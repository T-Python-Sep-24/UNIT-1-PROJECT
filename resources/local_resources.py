from colorama import Fore

def saudi_resources():
    """Return a list of local Saudi mental health resources."""
    resources = [
        {"name": "🏥 Saudi Mental Health Clinic", "website": "https://saudimentalhealth.org"},
        {"name": "🌍 National Awareness Program", "website": "https://awareness.sa"},
        {"name": "🏢 Riyadh Therapy Center", "website": "https://riyadhtherapy.com"},
        {"name": "☎️ Jeddah Emotional Support Line", "website": "https://emotionsupport-jeddah.org"},
        {"name": "🌟 Saudi Well-being Network", "website": "https://wellbeing.sa"},
        {"name": "📞 Mind Care Hotline", "website": "https://mindcare.sa"}
    ]
    return resources

def display_resources():
    """Display the list of local mental health resources."""
    resources = saudi_resources()
    print(Fore.CYAN + "Here are some local Saudi resources for mental health support:")
    for resource in resources:
        print(Fore.GREEN + f"{resource['name']} - Website: {resource['website']}")