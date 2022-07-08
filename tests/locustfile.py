import time

from locust import HttpUser, task, between


class QuickStartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def show_summary(self):
        self.client.post('/showSummary', data={'email': 'admin@irontemple.com'})
        time.sleep(1)

    @task
    def points_total_update(self):
        self.client.post('/purchasePlaces', data={'name': 'Iron Temple', 'competition': 'Spring Festival',
                                                  'places': 4})
        time.sleep(1)
