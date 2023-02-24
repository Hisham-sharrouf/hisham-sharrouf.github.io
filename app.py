import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    key = 'sk-openailczUHLXxpLnaSVkDTZKwT3BlbkFJ6hLt70qy4mnDNHDXugxs'
    openai.api_key = key
    if request.method == 'POST':
        input_text = request.form['input_text']
        # Process the input text in some way
        try:
            response = openai.Completion.create(
              model="text-davinci-003",
              prompt=f"Correct this formal English: {input_text}",
              temperature=0,
              max_tokens=60,
              top_p=1.0,
              frequency_penalty=0.0,
              presence_penalty=0.0
            )
             
        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 429:
                # Handle rate limit error
                print('Rate limit exceeded. Waiting for one minute...')
                time.sleep(5)
            else:
                # Handle other types of errors
                print(f'Request error: {e}')
                raise
                
        output_text = response['choices'][-1]['text']
        return render_template('index.html', output_text=output_text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
