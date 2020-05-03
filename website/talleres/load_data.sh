# Load Data
python manage.py loaddata businesses_basic_info.json
echo "Done Business"
python manage.py loaddata reviews_2019.json
echo "Done Reviews 2019"
python manage.py loaddata user_basic_info.json
echo "Done Users"
echo "Done All"