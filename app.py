from flask import Flask, render_template

app = Flask(__name__)

# Data that would typically come from a database
portfolio_data = {
    'about': {
        'name': 'Ashish Kumar Verma',
        'title': 'Software Engineer',
        'summary': 'Experienced Software Engineer with over 2 years specializing in Python and Django development. Strong foundation in data structures, OOP, and API integration. Proficient in MySQL, MongoDB, Git, and Postman.',
        'social_links': {
            'email': 'ashish20301@gmail.com',
            'linkedin': 'https://linkedin.com/in/ashish-kumar-verma',
            'github': 'https://github.com/ASHISH20301'
        }
    },
    'skills': [
        'Python', 'Django', 'MySQL', 'MongoDB', 'GitHub', 'GitLab',
        'Postman', 'Data Structures', 'OOP', 'Linux', 'RESTful API',
        'Backend Development'
    ],
    'experience': [
        {
            'title': 'Software Engineer',
            'company': 'Vitraya Technologies',
            'period': 'Jul \'22 – Present',
            'achievements': [
                'Optimized code for bill parsing, reducing claims approval time by over 80%.',
                'Led digital transformation projects for medical insurance claims, achieving a 30% increase in speed and a 20% error reduction.',
                'Successfully integrated Vitraya OCR Solutions with the Bill Parser project.',
                'Developed and deployed service suites improving reliability and scalability.'
            ]
        },
        {
            'title': 'R&D Intern',
            'company': 'Nokia Solutions & Networks India Pvt Ltd',
            'period': 'Aug \'21 – May \'22',
            'achievements': [
                'Deployed 50+ virtual machines on Nokia Cloudbase and configured IP settings.',
                'Improved network performance and security compliance.'
            ]
        }
    ],
    'projects': [
        {
            'name': 'Bill Parser',
            'description': 'Developed custom algorithms, server-side scripts, and enhanced database configurations.'
        },
        {
            'name': 'Vendor Management System',
            'description': 'Built a Django-based system for vendor profile management with performance metrics.'
        }
    ],
    'education': {
        'degrees': [
            {
                'title': 'B.Tech in Computer Science',
                'institution': 'Chandigarh Group of Colleges, Landran',
                'period': '2018–2022'
            },
            {
                'title': 'Higher Education (Class 12)',
                'institution': 'KV No.2, Chandigarh',
                'period': '2017–2018'
            }
        ],
        'certifications': [
            'Programming With Python (Udemy)',
            'Programming for Everybody (Coursera, University of Michigan)',
            'Python Data Structures (Coursera, University of Michigan)'
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', about=portfolio_data['about'])
@app.route('/skills')
def skills():
    return render_template('skills.html', skills=portfolio_data['skills'])

@app.route('/experience')
def experience():
    return render_template('experience.html', experience=portfolio_data['experience'])

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=portfolio_data['projects'])

@app.route('/education')
def education():
    return render_template('education.html', education=portfolio_data['education'])

if __name__ == '__main__':
    app.run(debug=True)