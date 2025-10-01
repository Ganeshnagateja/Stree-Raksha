from flask import Flask, render_template, request, jsonify, redirect, url_for
import re

app = Flask(__name__)

# Example question-answer pairs
qa_pairs = {
    "what is stree raksha": "Stree Raksha is a women's safety initiative.",
    "how can i contact you": "You can contact us via the 'Contact' page.",
    "what services do you offer": "We offer various services related to women's safety.",
    "what is the emergency helpline number for women in my state": "The emergency helpline number for women varies by state. You can usually find it on your local government or law enforcement website, or by contacting local women's organizations.",
    "how can i report harassment or violence against women": "You can report harassment or violence by contacting local law enforcement, visiting a police station, or using dedicated hotlines for reporting such incidents. Many organizations also offer anonymous reporting options.",
    "are there any mobile apps specifically designed for women's safety": "Yes, there are several mobile apps designed for women's safety, including personal safety apps that feature emergency contacts, location tracking, and alert systems. Examples include bSafe, Circle of 6, and SafeTrek.",
    "what self defense techniques are recommended for women": "Recommended self-defense techniques include awareness of surroundings, assertiveness training, and physical techniques like strikes to vulnerable areas (eyes, throat, groin). Local self-defense classes can provide practical training.",
    "where can i find women's shelters or support services near me": "To ensure safety while traveling, stay aware of your surroundings, avoid isolated areas, keep emergency contacts handy, use reputable transportation options, and share your itinerary with trusted friends or family.",
    "what steps can i take to ensure my safety while traveling": "To ensure safety while traveling, stay aware of your surroundings, avoid isolated areas, keep emergency contacts handy, use reputable transportation options, and share your itinerary with trusted friends or family.",
    "how can i recognize the signs of an abusive relationship": "Signs of an abusive relationship can include controlling behavior, frequent criticism, isolation from friends and family, and fear of your partner's reactions. Emotional abuse can be as damaging as physical abuse.",
    "what should i do if i feel unsafe in a public place": "If you feel unsafe, try to move to a well-lit and populated area, seek help from security personnel, or call a friend or family member. Trust your instincts and don't hesitate to ask for assistance.",
    "what legal protections are available for women against harassment": "Legal protections include restraining orders, anti-harassment laws, and workplace protections. Familiarize yourself with local laws and regulations regarding harassment and seek legal advice if needed.",
    "are there any workshops or training programs available for personal safety": "Many community organizations and local law enforcement agencies offer workshops and training programs on personal safety, self-defense, and awareness strategies. Check local listings for available programs.",
    "how can i safely share my location with trusted contacts": "You can share your location through mobile apps that allow location sharing, such as Google Maps, Find My Friends, or specific safety apps. Ensure that you only share your location with trusted contacts and disable sharing when not needed.",
    "what resources are available for mental health support for women": "Resources for mental health support include hotlines, counseling services, and therapy provided by community organizations, non-profits, or healthcare providers. Online resources and support groups can also be beneficial.",
    "how can i educate my community about women's safety issues": "You can educate your community through workshops, informational campaigns, social media, and collaboration with local organizations. Hosting events and discussions can also raise awareness.",
    "what are the signs of a potentially dangerous situation": "Signs of a potentially dangerous situation can include aggressive behavior, excessive jealousy, verbal threats, or any situation that feels uncomfortable or makes you wary. Trust your instincts and remove yourself if possible."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/self')
def self_service():
    questions = list(qa_pairs.keys())
    return render_template('self.html', questions=questions)

@app.route('/track', methods=['GET', 'POST'])
def tracking():
    if request.method == 'POST':
        username = request.form['username']
        start_location = request.form['start-location']
        end_location = request.form['end-location']
        emergency_phone1 = request.form['emergency-phone1']
        emergency_phone2 = request.form['emergency-phone2']
        return redirect(url_for('tracking'))

    return render_template('track.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.json
    question = data.get('question', '').strip().lower()  # Normalize input
    
    # Remove punctuation from the question
    question = re.sub(r'[^\w\s]', '', question)
    
    # Check if the question exists in the qa_pairs
    answer = qa_pairs.get(question, "Sorry, I don't have an answer for that.")
    
    # Debugging: Print the question and answer for verification
    print(f"Question: '{question}' - Answer: '{answer}'")
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
