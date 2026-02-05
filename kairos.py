name: Ghilofos Plan B Auto

on:
  schedule:
    - cron: '*/15 * * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write # ΕΔΩ ΕΙΝΑΙ ΤΟ ΚΛΕΙΔΙ
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          
      - name: Install Requests
        run: pip install requests
        
      - name: Run Weather Script
        run: python kairos.py
        
      - name: Commit and Push changes
        run: |
          git config --global user.name "GitHub Action"
          git config --global user.email "action@github.com"
          git add weather_data.json
          git commit -m "Update weather data" || exit 0
          git push
    
