import os
import openai
from flask import Flask, render_template, request
'''

@app.route('/process_text', methods=['POST'])
def c():
    input_text = request.form['input_text']
    # Process the input text in some way
    output_text = input_text.upper()
    return output_text

if __name__ == '__main__':
    app.run(debug=True)

'''
app = Flask(__name__)

@app.route('/process_text', methods=['POST'])
def process_text():
    key = 'sk-openailczUHLXxpLnaSVkDTZKwT3BlbkFJ6hLt70qy4mnDNHDXugxs'
    openai.api_key = key

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
    return output_text


if __name__ == '__main__':
    app.run(debug=True)
