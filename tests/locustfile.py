import time
from locust import HttpUser, task


class QuickStartUser(HttpUser):

    @task
    def show_summary(self):
        self.client.post('/showSummary', data={'email': 'admin@irontemple.com'})
        time.sleep(1)

    @task
    def points_total_update(self):
        self.client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Spring Festival',
                                                  'places': 1})
        time.sleep(1)
