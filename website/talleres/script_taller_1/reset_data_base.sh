python delete_everything.py
python manage.py loaddata users.yaml
echo "Done Users"
python manage.py loaddata artists.json
echo "Done Artists"
python manage.py loaddata homologacion_artist.json
echo "Done H Artists"
python manage.py loaddata homologacion_user.json
echo "Done H Users"
python manage.py loaddata ratings.json
echo "Done Ratings"
python manage.py loaddata reproductions.json
echo "Done Repro"
python manage.py loaddata user_info.json
echo "Done Users Info"
echo "Done All"


