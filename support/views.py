from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'support/home.html')

def response(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Get the user's name
        feeling = request.POST.get('feeling')  # Get the user's feeling
        message = get_encouragement(feeling)  # Get the encouragement message
        return render(request, 'support/response.html', {'name': name, 'feeling': feeling, 'message': message})
    return render(request, 'support/home.html')


def get_encouragement(feeling):
    encouragements = {
        'happy': 'Stay in the moment and enjoy your success. As Marcus Aurelius said, "The happiness of your life depends upon the quality of your thoughts."',
        'sad': 'Remember, "You have power over your mind, not outside events. Realize this, and you will find strength." – Marcus Aurelius.',
        'anxious': '"We suffer more often in imagination than in reality." – Seneca. Take it slow, one step at a time.',
        'angry': 'Epictetus reminds us, "It is not events that disturb us, but our view of them." Find peace within yourself.',
        'tired': 'Remember, "The impediment to action advances action. What stands in the way becomes the way." – Marcus Aurelius.',
        
        'alone': "The greatest thing in the world is to know how to belong to oneself. — Michel de Montaigne",
        'depressed': "Your present circumstances don’t determine where you can go; they merely determine where you start. — Nido Qubein",
        'addicted': "Recovery is not a race. You don’t have to feel guilty if it takes you longer than you thought it would. — Anonymous",
        'stressed': "It’s not stress that kills us, it is our reaction to it. — Hans Selye",
        'cheated': "When someone betrays you, it’s like a death in the family. — Unknown",
        'experiencing_conflict': "In the middle of difficulty lies opportunity. — Albert Einstein",
        'considering_suicide': "You are not a drop in the ocean. You are the entire ocean in a drop. — Rumi",
        'hope': "Hope is the thing with feathers that perches in the soul. — Emily Dickinson",
        'peace': "Peace begins with a smile. — Mother Teresa",
        'joy': "The joy of living is the joy of giving. — William E. Gladstone",
        'comfort': "In the midst of movement and chaos, keep stillness inside of you. — Deepak Chopra",
        'purpose': "Your purpose in life is to find your purpose and give your whole heart and soul to it. — Buddha",
        'forgiveness': "Forgiveness liberates the soul. It removes fear. That is why it is such a powerful weapon. — Nelson Mandela",
        'god': "Faith is taking the first step even when you don’t see the whole staircase. — Martin Luther King Jr.",
        'fear': "The only thing we have to fear is fear itself. — Franklin D. Roosevelt",
        'anxiety': "Do not anticipate trouble, or worry about what may never happen. Keep in the sunlight. — Benjamin Franklin",
        'loss': "To weep is to make less the depth of grief. — William Shakespeare",
        'change': "Change is hard at first, messy in the middle, and gorgeous at the end. — Robin Sharma",
        'healing': "Healing takes time, and asking for help is a courageous step. — Mariska Hargitay",
        'courage': "Courage is not the absence of fear, but the triumph over it. — Nelson Mandela",
        'resilience': "Resilience is accepting your new reality, even if it’s less good than the one you had before. — Elizabeth Edwards",
        'gratitude': "Gratitude turns what we have into enough. — Aesop",
        'self_love': "You yourself, as much as anybody in the entire universe, deserve your love and affection. — Buddha",
        'kindness': "No act of kindness, no matter how small, is ever wasted. — Aesop",
        'patience': "Patience is not simply the ability to wait – it’s how we behave while we’re waiting. — Joyce Meyer",
        'faith': "Now faith is confidence in what we hope for and assurance about what we do not see. — Hebrews 11:1",
        'joyful': "The most wasted of days is one without laughter. — E.E. Cummings",
        'encouragement': "Encouragement is like water to the soul; it helps you grow. — Anonymous",
        'acceptance': "Acceptance is the first step to recovery. — Anonymous",
        'surrender': "Sometimes surrender means giving up trying to understand and becoming comfortable with not knowing. — Eckhart Tolle",
        'strength': "Strength doesn’t come from what you can do. It comes from overcoming the things you once thought you couldn’t. — Rikki Rogers",
        'love': "Love is the only force capable of transforming an enemy into a friend. — Martin Luther King Jr.",
        'guidance': "In times of trouble, don’t worry. God is always with you. — Anonymous",
    }
    
    return encouragements.get(feeling, 'Stay strong. Every day is a new chance to grow.')
