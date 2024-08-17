# WhatsAppSender
_____________________
<ol>
<li>Install The Script to your Laptop</li>
<ol>
<li>Clone The Script</li>
<li>Install The Requirements</li>
</ol>
</ol>

# Clone The Script
```bash
# clone the script to your directory
git clone https://github.com/9-shen/whatsAppSender.git
```
# Install The Requirement
```bash
# cd to your Directory ' whatsappsender '
# Install the requirement
pip install requirements.txt
```
________________________
<ol>
<li>Prepare The Contact List</li>
<li>Prepare The Messages</li>
</ol>

# Prepare The Contact list
Make sure the contact list is listed in Contacts folder<br>
if you have a huge list you can use 'split_file_number.py' to split into small listes

<ol>
<li>Put The Contact lits into Contacts folder</li>
<li>Run The File split_file_numbers.py</li>

```bash
# run this file split_file_numbers.py
python split_file_numbers.py
```
</ol>

PS: the Script will take all contacts list end with .csv <br>
and split them into 20 small files. <br>
If you want more or less file you can update this line :

```bash
# Line 9, update the num_splits
def split_csv_file(file_path, output_dir, num_splits=20, encoding='ISO-8859-1'):

```
# Prepare The Messages

You can add many Messages file into Folder Message <br>
The script will take randomly message each time to avoid spam.

## RUN THE SCRIPT

<ol>
<li>Make sure the web whatsapp already open</li>
<li>Run the main.py</li>
</ol>

You can run the script by call this main.py file

```bash
# run this file main.py
python main.py
```