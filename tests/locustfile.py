from locust import HttpUser, task


class QuickStartUser(HttpUser):

    @task
    def show_summary(self):
        self.client.post('/showSummary', json={'email': 'admin@irontemple.com'})

    @task
    def points_total_update(self):
        self.client.post('/purchasePlaces', json={'name': 'Iron Temple', 'competition': 'Spring Festival',
                                                  'places': 4})
