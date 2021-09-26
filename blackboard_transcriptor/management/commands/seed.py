from django.utils import translation
from core.models import School
from django.core.management.base import BaseCommand
import random
import json

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Address instances")
    School.objects.all().delete()
    Program.objects.all().delete()
    Course.objects.all().delete()
    Videos.objects.all().delete()

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    gbc = School(name="George Brown College", website="https://georgebrown.ca")
    gbc.save()
    
    t177 = Program(name="Computer Programmer Analyst", code="T177", school=gbc)
    t177.save()

    mobile_development = Course(name="MOBILE APPL. DEVELOPMENT I", program=t177, semester=5, code="COMP3074")
    mobile_development.save()

    lecture_1_transcript = json.load(open('MobileAppDevelopment-Lecuture-1.json', 'r'))
    lecture_1_video = Video(title="Lecture 1", url="https://blackboard-transcriptor.s3.us-east-2.amazonaws.com/GeorgeBrownCollege/MobileApplicationDevelopment/MADL1.mp4", video_number=1, transcription=lecture_1_transcript, course=mobile_development)
    lecture_1_video.save()