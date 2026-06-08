from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):
    def get(self, request):
        return Response({
            'name': 'ASH Emran',
            'title': 'Full Stack Developer & Competitive Programmer',
            'bio': 'Computer Science & Engineering student with a passion for problem solving, web development, and competitive programming.',
            'stats': {'projects': 4, 'contests': 2, 'cgpa': '3.71'},
        })


class AboutView(APIView):
    def get(self, request):
        return Response({
            'name': 'ASH Emran',
            'title': 'Full Stack Developer & Competitive Programmer',
            'bio': 'Computer Science & Engineering student with a passion for problem solving, web development, and competitive programming. Currently mentoring at NEU Programming Club.',
            'location': 'Sherpur, Bangladesh',
            'email': 'emranhaquee@gmail.com',
            'phone': '+8801521742124',
        })


class EducationView(APIView):
    def get(self, request):
        return Response({
            'degrees': [
                {
                    'degree': 'B.Sc. in Computer Science & Engineering',
                    'university': 'Netrokona University, Netrokona',
                    'duration': 'Jan 2020 - Nov 2025',
                    'cgpa': '3.71/4.0',
                    'courses': ['Data Structures', 'Algorithms', 'Database Management', 'Web Technologies'],
                }
            ]
        })


class SkillsView(APIView):
    def get(self, request):
        return Response({
            'domain_expertise': ['Problem Solving', 'Data Structures', 'Algorithms', 'Machine Learning'],
            'programming_languages': ['C', 'C++', 'Dart', 'Python'],
            'web_technologies': ['HTML', 'CSS', 'Bootstrap', 'Django', 'Tailwind CSS', 'JavaScript'],
            'software_tools': ['GitHub', 'VS Code', 'Git'],
            'familiar_with': ['SQA', 'Selenium WebDriver', 'Basic Software Testing (Manual & Automation)'],
        })


class ProjectsView(APIView):
    def get(self, request):
        return Response({
            'projects': [
                {
                    'name': 'E-Commerce Website With Django',
                    'description': 'Developed a responsive e-commerce web application with Django.',
                    'technologies': ['HTML', 'CSS', 'Bootstrap', 'JavaScript', 'Python', 'Django'],
                    'github': 'https://github.com/Emran-Haque',
                    'order': 1,
                },
                {
                    'name': 'SHU-Transport',
                    'description': 'Developed a mobile application to show the live location of the university bus.',
                    'technologies': ['Flutter'],
                    'github': 'https://github.com/Emran-Haque',
                    'order': 2,
                },
                {
                    'name': 'Netrokona Online',
                    'description': 'Developed a mobile application where people can get the information of Netrokona District.',
                    'technologies': ['Flutter'],
                    'github': 'https://github.com/Emran-Haque',
                    'order': 3,
                },
                {
                    'name': 'Brain Tumor Detection',
                    'description': 'Developed a machine learning based application to detect Brain Tumor.',
                    'technologies': ['Machine Learning', 'Python'],
                    'github': 'https://github.com/Emran-Haque',
                    'order': 4,
                },
            ]
        })


class CompetitiveProgrammingView(APIView):
    def get(self, request):
        return Response({
            'contests': [
                {
                    'name': 'SUST CSE Carnival 2024 IUPC',
                    'organization': 'SUST',
                    'team': 'Rebooters_SHU',
                    'status': 'Participated',
                },
                {
                    'name': 'ICPC Dhaka Regional 2023',
                    'organization': 'ICPC',
                    'team': 'Rebooters_SHU',
                    'status': 'Ranked 147th',
                },
            ]
        })


class ContactView(APIView):
    def get(self, request):
        return Response({
            'email': 'emranhaquee@gmail.com',
            'phone': '+8801521742124',
            'location': 'Sherpur, Bangladesh',
            'linkedin': 'https://www.linkedin.com/in/ash-emran/',
            'github': 'https://github.com/Emran-Haque',
        })
