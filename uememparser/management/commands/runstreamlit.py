import subprocess
from pathlib import Path

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run the Streamlit app - Unreal Engine memory report parser."

    def handle(self, *args, **kwargs):
        base_dir = Path(__file__).resolve().parent.parent.parent
        streamlit_app_path = base_dir / 'uememparser.py'
        subprocess.run(["streamlit", "run", streamlit_app_path])
