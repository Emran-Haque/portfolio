from django.shortcuts import render
from django.views import View

# Home page view
def home(request):
    return render(request, 'home.html')

# About page view
def about(request):
    about_data = {
        'name': 'ASH Emran',
        'title': 'Full Stack Developer & Competitive Programmer',
        'bio': 'Computer Science & Engineering student with a passion for problem solving, web development, and competitive programming. Currently mentoring at NEU Programming Club.',
        'location': 'Sherpur, Bangladesh',
        'email': 'emranhaquee@gmail.com',
        'phone': '+8801521742124',
    }
    return render(request, 'about.html', about_data)

# Education page view
def education(request):
    education_data = {
        'degrees': [
            {
                'degree': 'B.Sc. in Computer Science & Engineering',
                'university': 'Netrokona University, Netrokona',
                'duration': 'Jan 2020 - Nov 2025',
                'cgpa': '3.71/4.0',
                'courses': ['Data Structures', 'Algorithms', 'Database Management', 'Web Technologies']
            }
        ]
    }
    return render(request, 'education.html', education_data)

# Skills page view
def skills(request):
    skills_data = {
        'domain_expertise': ['Problem Solving', 'Data Structures', 'Algorithms', 'Machine Learning'],
        'programming_languages': ['C', 'C++', 'Dart', 'Python'],
        'web_technologies': ['HTML', 'CSS', 'Bootstrap', 'Django', 'Tailwind CSS', 'JavaScript'],
        'software_tools': ['GitHub', 'VS Code', 'Git'],
        'familiar_with': ['SQA', 'Selenium WebDriver', 'Basic Software Testing (Manual & Automation)'],
    }
    return render(request, 'skills.html', skills_data)

# Projects page view
def projects(request):
    projects_data = {
        'projects': [
            {
                'name': 'E-Commerce Website With Django',
                'description': 'Developed a responsive e-commerce web application with Django.',
                'technologies': ['HTML', 'CSS', 'Bootstrap', 'JavaScript', 'Python', 'Django'],
                'github': 'https://github.com',
                'order': 1
            },
            {
                'name': 'SHU-Transport',
                'description': 'Developed a mobile application to show the live location of the university bus.',
                'technologies': ['Flutter'],
                'github': 'https://github.com',
                'order': 2
            },
            {
                'name': 'Netrokona Online',
                'description': 'Developed a mobile application where people can get the information of Netrokona District.',
                'technologies': ['Flutter'],
                'github': 'https://github.com',
                'order': 3
            },
            {
                'name': 'Brain Tumor Detection',
                'description': 'Developed a machine learning based application to detect Brain Tumor.',
                'technologies': ['Machine Learning', 'Python'],
                'github': 'https://github.com',
                'order': 4
            }
        ]
    }
    return render(request, 'projects.html', projects_data)

# Competitive Programming page view
def competitive_programming(request):
    cp_data = {
        'contests': [
            {
                'name': 'SUST CSE Carnival 2024 IUPC',
                'organization': 'SUST',
                'team': 'Rebooters_SHU',
                'status': 'Participated'
            },
            {
                'name': 'ICPC Dhaka Regional 2023',
                'organization': 'ICPC',
                'team': 'Rebooters_SHU',
                'status': 'Ranked 147th'
            }
        ]
    }
    return render(request, 'competitive_programming.html', cp_data)

# Contact page view
def contact(request):
    contact_data = {
        'email': 'emranhaquee@gmail.com',
        'phone': '+8801521742124',
        'location': 'Sherpur, Bangladesh',
        'linkedin': 'https://www.linkedin.com/in/ahta-shamul-hoque-emran-a56775367/',
        'github': 'https://github.com/Emran-Haque',
    }
    return render(request, 'contact.html', contact_data)
