from flask import Flask, request, render_template

app = Flask(__name__)


#@app.route('/hello')
#def say_hello():
    #return render_template("madlibs.html")

"""Madlibs Stories."""
class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started



story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/', methods=['GET', 'POST'])
def madlibs():
    if request.method == 'POST':
        # Get user inputs from the form
        place = request.form['place']
        noun = request.form['noun']
        verb = request.form['verb']
        adjective = request.form['adj']
        plural_noun = request.form['plu']

    else:
    
        # If no form submission, try to get parameters from URL
        place = request.args.get('place')
        noun = request.args.get('noun')
        verb = request.args.get('verb')
        adjective = request.args.get('adj')
        plural_noun = request.args.get('plu')

    if place and noun and verb and adjective and plural_noun:
        # Generate the story using the inputs
        user_answers = {
            'place': place,
            'noun': noun,
            'verb': verb,
            'adjective': adjective,
            'plural_noun': plural_noun
        }
        generated_story = story.generate(user_answers)
        
        return render_template('result.html', story=generated_story)

    # If no complete set of parameters, render the form
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

