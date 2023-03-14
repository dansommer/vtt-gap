import os
import sys
import re
import argparse
from datetime import datetime
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

def generate_ad_vtt(input_filename, output_filename, min_gap_length):
    with open(input_filename, 'r', encoding='utf-8-sig') as input_file:
        lines = input_file.readlines()

    ad_lines = []
    last_end_time = None

    for line in lines:
        if re.match(r'^\d\d:\d\d:\d\d\.\d\d\d', line):
            start_time, end_time = line.split(' --> ')
            if last_end_time is not None and (datetime.strptime(start_time, '%H:%M:%S.%f') - datetime.strptime(last_end_time, '%H:%M:%S.%f')).total_seconds() > min_gap_length:
                # Insert a blank line with the missing time
                ad_lines.append('\n')
                ad_lines.append('{} --> {}\n'.format(last_end_time, start_time))
                ad_lines.append('AD possibility\n')
            last_end_time = end_time.strip()
        elif 'AD possibility' in line:
            ad_lines.append(line)

    with open(output_filename, 'w', encoding='utf-8-sig') as output_file:
        output_file.writelines(ad_lines)


def generate_edited_vtt(input_filename, output_filename, min_gap_length):
    with open(input_filename, 'r', encoding='utf-8-sig') as input_file:
        lines = input_file.readlines()

    new_lines = []
    last_end_time = None

    for line in lines:
        if re.match(r'^\d\d:\d\d:\d\d\.\d\d\d', line):
            start_time, end_time = line.split(' --> ')
            if last_end_time is not None and (datetime.strptime(start_time, '%H:%M:%S.%f') - datetime.strptime(last_end_time, '%H:%M:%S.%f')).total_seconds() > min_gap_length:
                # Insert a blank line with the missing time
                new_lines.append('\n')
                new_lines.append('{} --> {}\n'.format(last_end_time, start_time))
                new_lines.append('AD possibility\n')
            last_end_time = end_time.strip()
            new_lines.append(line)
        else:
            new_lines.append(line)

    with open(output_filename, 'w', encoding='utf-8-sig') as output_file:
        output_file.writelines(new_lines)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file, output filename, and minimum gap length from the form
        input_file = request.files['input_file']
        output_filename = request.form['output_filename']
        min_gap_length = float(request.form['min_gap_length'])

        # Save the uploaded file to disk
        input_filename = input_file.filename
        input_file.save(input_filename)

        # Generate the output files
        if 'edited' in request.form.getlist('output_type'):
            generate_edited_vtt(input_filename, output_filename + '.vtt', min_gap_length)
        if 'ad' in request.form.getlist('output_type'):
            generate_ad_vtt(input_filename, 'ad_' + output_filename + '.vtt', min_gap_length)

        # Delete the uploaded file
        os.remove(input_filename)

        # Generate a download link for the output file(s)
        download_links = []
        if 'edited' in request.form.getlist('output_type'):
            download_links.append({'name': 'Original & AD Potentials', 'url': '/download/' + output_filename + '.vtt'})
        if 'ad' in request.form.getlist('output_type'):
            download_links.append({'name': 'AD Potentials', 'url': '/download/' + 'ad_' + output_filename + '.vtt'})

        # Render the download page with the download link(s)
        return render_template('download.html', download_links=download_links)

    else:
        # Clear any existing download links and return the index page
        return render_template('index.html', download_links=None)


@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':

    app.run(debug=True)
