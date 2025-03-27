from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import spacy
import json
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'  # Relative path to create questions.db in the project folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Load the spaCy model for NLP
nlp = spacy.load("en_core_web_sm")

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(20), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    options = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(50), nullable=False)  # New field for topic categorization

# Learning resources for different topics
LEARNING_RESOURCES = {
    'Python': {
        'variables': [
            {'title': 'Python Variables', 'url': 'https://www.w3schools.com/python/python_variables.asp'},
            {'title': 'Variables in Python', 'url': 'https://realpython.com/python-variables/'}
        ],
        'loops': [
            {'title': 'Python Loops', 'url': 'https://www.w3schools.com/python/python_for_loops.asp'},
            {'title': 'Python Loop Tutorials', 'url': 'https://realpython.com/python-for-loop/'}
        ],
        'functions': [
            {'title': 'Python Functions', 'url': 'https://www.w3schools.com/python/python_functions.asp'},
            {'title': 'Python Function Guide', 'url': 'https://realpython.com/defining-your-own-python-function/'}
        ],
        'classes': [
            {'title': 'Python Classes', 'url': 'https://www.w3schools.com/python/python_classes.asp'},
            {'title': 'OOP in Python', 'url': 'https://realpython.com/python3-object-oriented-programming/'}
        ],
        'general': [
            {'title': 'Python Basics', 'url': 'https://www.python.org/about/gettingstarted/'},
            {'title': 'Python Tutorial', 'url': 'https://docs.python.org/3/tutorial/'}
        ]
    },
    'Data Structures': {
        'arrays': [
            {'title': 'Arrays in Python', 'url': 'https://www.geeksforgeeks.org/python-arrays/'},
            {'title': 'Python Lists', 'url': 'https://realpython.com/python-lists-tuples/'}
        ],
        'linked_lists': [
            {'title': 'Linked Lists', 'url': 'https://realpython.com/linked-lists-python/'},
            {'title': 'Implementing Linked Lists', 'url': 'https://www.geeksforgeeks.org/linked-list-set-1-introduction/'}
        ],
        'trees': [
            {'title': 'Tree Data Structure', 'url': 'https://www.geeksforgeeks.org/binary-tree-data-structure/'},
            {'title': 'Python Trees', 'url': 'https://realpython.com/binary-trees-python/'}
        ],
        'general': [
            {'title': 'Data Structures Overview', 'url': 'https://www.geeksforgeeks.org/data-structures/'},
            {'title': 'Python Data Structures', 'url': 'https://docs.python.org/3/tutorial/datastructures.html'}
        ]
    },
    'JavaScript': {
        'variables': [
            {'title': 'JavaScript Variables', 'url': 'https://www.w3schools.com/js/js_variables.asp'},
            {'title': 'Modern JavaScript Variables', 'url': 'https://javascript.info/variables'}
        ],
        'functions': [
            {'title': 'JavaScript Functions', 'url': 'https://www.w3schools.com/js/js_functions.asp'},
            {'title': 'Functions in JavaScript', 'url': 'https://javascript.info/function-basics'}
        ],
        'arrays': [
            {'title': 'JavaScript Arrays', 'url': 'https://www.w3schools.com/js/js_arrays.asp'},
            {'title': 'Working with Arrays', 'url': 'https://javascript.info/array'}
        ],
        'operators': [
            {'title': 'JavaScript Operators', 'url': 'https://www.w3schools.com/js/js_operators.asp'},
            {'title': 'Basic Operators', 'url': 'https://javascript.info/operators'}
        ],
        'general': [
            {'title': 'JavaScript Tutorial', 'url': 'https://www.w3schools.com/js/'},
            {'title': 'Modern JavaScript Tutorial', 'url': 'https://javascript.info/'}
        ]
    },
    'SQL': {
        'queries': [
            {'title': 'SQL SELECT Statement', 'url': 'https://www.w3schools.com/sql/sql_select.asp'},
            {'title': 'SQL Queries Tutorial', 'url': 'https://www.sqlservertutorial.net/sql-server-basics/'}
        ],
        'filtering': [
            {'title': 'SQL WHERE Clause', 'url': 'https://www.w3schools.com/sql/sql_where.asp'},
            {'title': 'Filtering Data in SQL', 'url': 'https://www.sqlservertutorial.net/sql-server-basics/sql-server-where/'}
        ],
        'joins': [
            {'title': 'SQL JOINs', 'url': 'https://www.w3schools.com/sql/sql_join.asp'},
            {'title': 'Understanding SQL Joins', 'url': 'https://www.sqlservertutorial.net/sql-server-basics/sql-server-joins/'}
        ],
        'general': [
            {'title': 'SQL Tutorial', 'url': 'https://www.w3schools.com/sql/'},
            {'title': 'SQL Learning Path', 'url': 'https://www.sqlservertutorial.net/'}
        ]
    },
    'Machine Learning': {
        'fundamentals': [
            {'title': 'Machine Learning Basics', 'url': 'https://www.coursera.org/learn/machine-learning'},
            {'title': 'ML Fundamentals', 'url': 'https://developers.google.com/machine-learning/crash-course'}
        ],
        'model_evaluation': [
            {'title': 'Model Evaluation Methods', 'url': 'https://scikit-learn.org/stable/modules/model_evaluation.html'},
            {'title': 'Evaluating ML Models', 'url': 'https://www.kaggle.com/learn/intro-to-machine-learning'}
        ],
        'preprocessing': [
            {'title': 'Data Preprocessing', 'url': 'https://scikit-learn.org/stable/modules/preprocessing.html'},
            {'title': 'Feature Engineering', 'url': 'https://www.kaggle.com/learn/feature-engineering'}
        ],
        'general': [
            {'title': 'Machine Learning Guide', 'url': 'https://developers.google.com/machine-learning/guides'},
            {'title': 'ML Learning Path', 'url': 'https://www.kaggle.com/learn'}
        ]
    }
}

with app.app_context():
    db.create_all()

# Store user progress (in-memory for simplicity; use a database for production)
user_progress = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_questions/<skill>/<level>')
def get_questions(skill, level):
    # Get all questions for the given skill and level
    questions = Question.query.filter_by(skill=skill, level=level).all()
    
    # Randomly select 10 questions (or all if less than 10)
    selected_questions = random.sample(questions, min(10, len(questions)))
    
    questions_data = []
    for q in selected_questions:
        # Debug print for raw options
        print(f"\nProcessing Question {q.id}: {q.text}")
        print(f"Raw options string: {q.options}")
        
        # Split and clean options
        options = [opt.strip() for opt in q.options.split(',')]
        options = [opt for opt in options if opt]
        
        # Randomize the order of options
        random.shuffle(options)
        
        print(f"Processed options: {options}")
        
        question_data = {
            'id': q.id,
            'skill': q.skill,
            'level': q.level,
            'text': q.text,
            'options': options,
            'topic': q.topic
        }
        questions_data.append(question_data)
    
    # Randomize the order of questions
    random.shuffle(questions_data)
    
    # Print final JSON response for debugging
    print("\nFinal response data:")
    print(json.dumps(questions_data, indent=2))
    
    return jsonify(questions_data)

@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    data = request.get_json()
    answers = data['answers']
    skill = data['skill']
    level = data['level']
    user_id = data.get('user_id', 'default_user')

    if user_id not in user_progress:
        user_progress[user_id] = {}

    # Get only the questions that were answered
    question_ids = [int(qid) for qid in answers.keys()]
    questions = Question.query.filter(Question.id.in_(question_ids)).all()
    
    total_score = 0
    max_score = len(questions)  # This will be 10 or less
    topic_scores = {}

    for q in questions:
        user_answer = answers.get(str(q.id), "")
        if user_answer:
            doc1 = nlp(user_answer.lower())
            doc2 = nlp(q.answer.lower())
            similarity = doc1.similarity(doc2)
            
            # Track scores by topic
            if q.topic not in topic_scores:
                topic_scores[q.topic] = {'correct': 0, 'total': 0}
            topic_scores[q.topic]['total'] += 1
            
            if similarity > 0.8:
                total_score += 1
                topic_scores[q.topic]['correct'] += 1

    level_score = (total_score / max_score) * 100 if max_score > 0 else 0

    # Calculate topic proficiency
    topic_proficiency = {
        topic: (scores['correct'] / scores['total']) * 100
        for topic, scores in topic_scores.items()
    }

    # Determine areas for improvement
    improvements_needed = [
        {'topic': topic, 'score': score}
        for topic, score in topic_proficiency.items()
        if score < 70
    ]

    # Get learning resources for topics that need improvement
    learning_recommendations = []
    # First add resources for topics that need improvement
    for improvement in improvements_needed:
        topic = improvement['topic']
        if topic in LEARNING_RESOURCES.get(skill, {}):
            learning_recommendations.extend(LEARNING_RESOURCES[skill][topic])
    
    # Then add resources for all other topics
    for topic in topic_proficiency.keys():
        if topic in LEARNING_RESOURCES.get(skill, {}) and topic not in [imp['topic'] for imp in improvements_needed]:
            learning_recommendations.extend(LEARNING_RESOURCES[skill][topic])
    
    # Always include general resources
    if 'general' in LEARNING_RESOURCES.get(skill, {}):
        learning_recommendations.extend(LEARNING_RESOURCES[skill]['general'])

    # Remove duplicate resources
    seen_urls = set()
    unique_recommendations = []
    for rec in learning_recommendations:
        if rec['url'] not in seen_urls:
            seen_urls.add(rec['url'])
            unique_recommendations.append(rec)
    learning_recommendations = unique_recommendations

    if skill not in user_progress[user_id]:
        user_progress[user_id][skill] = {'Beginner': 0, 'Intermediate': 0, 'Advanced': 0}
    user_progress[user_id][skill][level] = level_score

    next_level = None
    if level_score >= 70:  # Only proceed to next level if score is 70% or higher
        if level == 'Beginner':
            next_level = 'Intermediate'
        elif level == 'Intermediate':
            next_level = 'Advanced'

    return jsonify({
        'level_score': level_score,
        'next_level': next_level,
        'proficiency': {skill: level_score},
        'progress': user_progress[user_id],
        'topic_scores': topic_proficiency,
        'improvements_needed': improvements_needed,
        'learning_recommendations': learning_recommendations
    })

@app.route('/get_recommended_jobs', methods=['POST'])
def get_recommended_jobs():
    proficiency = request.get_json()
    
    # Only consider skills where the user has passed Advanced level (score > 70)
    skills = [skill for skill, score in proficiency.items() if score > 70]
    
    if not skills:
        return jsonify([{
            "title": "Complete the Advanced level assessment to see job recommendations.",
            "company": {"display_name": "N/A"},
            "location": {"display_name": "N/A"},
            "redirect_url": "#"
        }])
    
    # Determine experience level based on proficiency
    # Since we're only considering Advanced level passes, we'll use senior/mid-level
    avg_proficiency = sum(proficiency.values()) / len(proficiency)
    if avg_proficiency >= 90:
        level = "senior"
    else:
        level = "mid-level"

    search_terms = [f"{skill} {level}" for skill in skills]
    jobs = get_jobs(search_terms)
    return jsonify(jobs)

def get_jobs(search_terms):
    app_id = os.getenv('ADZUNA_APP_ID')
    app_key = os.getenv('ADZUNA_APP_KEY')
    
    if not app_id or not app_key:
        print("Adzuna API credentials not found in environment variables")
        return [{
            "title": "API configuration required",
            "company": {"display_name": "N/A"},
            "location": {"display_name": "N/A"},
            "redirect_url": "#"
        }]

    # Base URL for Adzuna API
    base_url = 'https://api.adzuna.com/v1/api/jobs'
    country = 'gb'  # You can change this to target different countries (gb, us, au, etc.)
    
    params = {
        'app_id': app_id,
        'app_key': app_key,
        'what': ' '.join(search_terms),
        'results_per_page': 10,
        'content-type': 'application/json',
        'sort_by': 'relevance',  # You can change this to 'date', 'salary', etc.
        'max_days_old': 30  # Only show jobs posted in the last 30 days
    }

    try:
        response = requests.get(f"{base_url}/{country}/search/1", params=params)
        print(f"Adzuna API request URL: {response.url}")
        print(f"Adzuna API response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            jobs = data.get('results', [])
            
            if not jobs:
                return [{
                    "title": "No jobs found matching your skills",
                    "company": {"display_name": "Keep improving your skills!"},
                    "location": {"display_name": "Worldwide"},
                    "redirect_url": "#"
                }]

            # Process and clean job data
            processed_jobs = []
            for job in jobs:
                processed_job = {
                    "title": job.get('title', 'No title available'),
                    "company": {
                        "display_name": job.get('company', {}).get('display_name', 'Company not specified')
                    },
                    "location": {
                        "display_name": job.get('location', {}).get('display_name', 'Location not specified')
                    },
                    "description": job.get('description', 'No description available'),
                    "redirect_url": job.get('redirect_url', '#'),
                    "salary_min": job.get('salary_min', 'Not specified'),
                    "salary_max": job.get('salary_max', 'Not specified'),
                    "created": job.get('created', 'Date not specified')
                }
                processed_jobs.append(processed_job)
            
            return processed_jobs
            
        elif response.status_code == 401:
            print("Authentication failed. Check your API credentials.")
            return [{
                "title": "API Authentication Failed",
                "company": {"display_name": "Please check API credentials"},
                "location": {"display_name": "N/A"},
                "redirect_url": "#"
            }]
        else:
            print(f"API request failed with status code: {response.status_code}")
            print(f"Response text: {response.text}")
            return [{
                "title": f"Error fetching jobs (Status: {response.status_code})",
                "company": {"display_name": "Try again later"},
                "location": {"display_name": "N/A"},
                "redirect_url": "#"
            }]
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {str(e)}")
        return [{
            "title": "Error connecting to job search service",
            "company": {"display_name": "Network or service error"},
            "location": {"display_name": "N/A"},
            "redirect_url": "#"
        }]

if __name__ == '__main__':
    app.run(debug=True)