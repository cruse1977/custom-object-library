python -m venv .venv
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Building catalog..."
python mkcatalog.py --path=../library
